import sys
from PyQt4 import QtGui
import user_input
import datetime
import files
import pprint
import categorize
import entry
import calculate
import numpy
import matplotlib.pyplot
import matplotlib.backends.backend_qt4agg

class window(QtGui.QWidget):
  
  def __init__(self,expense_list):
    
    super(window,self).__init__()
    self.expense_list = expense_list
    self.cat = categorize.category()    
    self.initUI()   
    
  def initUI(self):
    
    #screen = QtGui.QDesktopWidget().screenGeometry()
    #self.setGeometry(0,0,screen.width(),screen.height())
    #self.setGeometry(300,300,250,150)
    self.setWindowTitle('Expenses')
    
    self.catlist = QtGui.QComboBox()
    self.catlist.addItem("All")
    for key in self.cat.categories:
      self.catlist.addItem(key)
    self.catlist.currentIndexChanged.connect(self.change_subcat)  
    
    self.subcatlist = QtGui.QComboBox()
    self.subcatlist.addItem("All") 
    
    self.grid = QtGui.QGridLayout()
    self.setLayout(self.grid)
    self.create_list_table()

    self.grid.addWidget(self.catlist,0,1)
    self.grid.addWidget(self.subcatlist,1,1) 
    
    self.figure  = matplotlib.pyplot.figure()
    self.drawing = self.figure.add_subplot(111)
    self.canvas  = matplotlib.backends.backend_qt4agg.FigureCanvasQTAgg(self.figure)

    self.create_total_table()
    self.create_pie_chart()
    
    self.showMaximized()
    
  def create_list_table(self):
    table = QtGui.QTableWidget()
    table.setRowCount(len(self.expense_list)+1)
    table.setColumnCount(7)
    table.setHorizontalHeaderLabels(["date","merchant","amount"])
    #table.resize(400,250)    
    
    self.current_cat = str(self.catlist.currentText())
    self.current_subcat = str(self.subcatlist.currentText())
    
    print self.current_cat,self.current_subcat
    
    self.category_list = categorize.extract_category(self.current_cat,self.current_subcat,self.expense_list)
    self.category_list.sort(key=lambda x: x["date"], reverse=False)
    total = calculate.sum_list(self.category_list)
    print total
    
    row = 0
    for expense in self.category_list:    
      date = QtGui.QTableWidgetItem(str(expense["month"])+"/"+str(expense["date"])+"/"+str(expense["year"]))
      merchant = QtGui.QTableWidgetItem(expense["merchant"])
      amount = QtGui.QTableWidgetItem(str(expense["amount"]))
      note = QtGui.QTableWidgetItem(expense["note"])
      person = QtGui.QTableWidgetItem(expense["for"])
      category = QtGui.QTableWidgetItem(expense["category"])
      sub_category = QtGui.QTableWidgetItem(expense["sub-category"])       
      table.setItem(row,0,date)
      table.setItem(row,1,merchant)
      table.setItem(row,2,amount)
      table.setItem(row,3,person)
      table.setItem(row,4,category)      
      table.setItem(row,5,sub_category)
      table.setItem(row,6,note)      
      row = row + 1
          
    table.setItem(row,0,QtGui.QTableWidgetItem("Total"))
    table.setItem(row,2,QtGui.QTableWidgetItem(str(total)))
    
    self.grid.addWidget(table,2,1,2,1)
    
  def change_subcat(self):
    print "index changed"
    self.subcatlist = QtGui.QComboBox()
    category = str(self.catlist.currentText())
    self.subcatlist.currentIndexChanged.connect(self.create_list_table)    
    self.subcatlist.addItem("All")
    if category == "All":
      pass
    else:  
      for item in self.cat.categories[category]:
        print item
        self.subcatlist.addItem(item)
    self.grid.addWidget(self.subcatlist,1,1)
    print ""
    self.create_list_table()
    
  def create_total_table(self):
    table = QtGui.QTableWidget()
    table.setRowCount(len(self.cat.categories)+1)
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["category","total","percent"])
    
    all_total = calculate.sum_list(self.expense_list)

    row = 0
    if all_total > 0.00:
      for category in self.cat.categories:
        category_list = categorize.extract_category(category,"All",self.expense_list)
        category_total = calculate.sum_list(category_list)
        category_percent = round(category_total/all_total*100.0,2)
        table.setItem(row,0,QtGui.QTableWidgetItem(category))
        table.setItem(row,1,QtGui.QTableWidgetItem(str(category_total)))
        table.setItem(row,2,QtGui.QTableWidgetItem(str(category_percent)))
        row = row + 1      
      
    table.setItem(row,0,QtGui.QTableWidgetItem("Total"))
    table.setItem(row,1,QtGui.QTableWidgetItem(str(all_total)))
    table.setItem(row,2,QtGui.QTableWidgetItem("100.00"))      
      
    self.grid.addWidget(table,0,0,3,1)      
    
  def create_pie_chart(self):
    labels = []
    totals = []
    for category in self.cat.categories:      
      category_list = categorize.extract_category(category,"All",self.expense_list)
      category_total = calculate.sum_list(category_list)
      labels.append(category)
      totals.append(category_total)
      
    self.drawing.pie(totals,labels=labels,autopct='%1.1f%%')
    self.drawing.axis('equal')
    self.canvas.draw ()
    self.grid.addWidget(self.canvas,3,0)
    
##############################################################################################################################################      
  
def main(expense_list):
  
  app = QtGui.QApplication(sys.argv)
  w = window(expense_list)
  app.exec_()
  
def month():
    
  min_date,max_date = files.find_range() 
  now = datetime.datetime.now()   
  get_input = user_input.user_input(0)
  year = get_input.option_num("Enter year:",2017,max_date[1],now.year)
  month = get_input.option_num("Enter month:",1,12,now.month)  
  expense_list = files.manage("Month","load",month,year)  
  menu = entry.make_expense_menu(expense_list)
  
  for i,item in enumerate(menu):
    print "  ",i+1," - ",item
  
  main(expense_list)
  
def month_range():  

  min_date,max_date = files.find_range() 
  start_year = user_input.option_num("Enter starting year:",2017,min_date[1],min_date[1])
  start_month = user_input.option_num("Enter starting month:",1,12,min_date[0])
  end_year = user_input.option_num("Enter ending year:",2017,max_date[1],max_date[1])
  end_month = user_input.option_num("Enter ending month:",1,12,max_date[0])
  
  main(expense_list)
  
def merchant_list():
  
  merchant_list = files.manage("Merchant","load")
  pprint.pprint(merchant_list)