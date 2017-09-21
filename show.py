import sys
from PyQt4 import QtGui
import user_input
import datetime
import files
import pprint
import categorize
import entry

class window(QtGui.QWidget):
  
  def __init__(self,expense_list):
    
    super(window,self).__init__()
    self.expense_list = expense_list
    self.initUI()   
    
  def initUI(self):
    
    #screen = QtGui.QDesktopWidget().screenGeometry()
    #self.setGeometry(0,0,screen.width(),screen.height())
    #self.setGeometry(300,300,250,150)
    self.setWindowTitle('Expenses')
    
    self.cat = categorize.category()
    self.catlist = QtGui.QComboBox()
    self.catlist.addItem("All")
    for key in self.cat.categories:
      self.catlist.addItem(key)
    self.catlist.currentIndexChanged.connect(self.change_subcat)  
    
    self.subcatlist = QtGui.QComboBox()
    self.subcatlist.addItem("All") 
    
    self.grid = QtGui.QGridLayout()
    self.setLayout(self.grid)
    table = self.create_table()

    self.grid.addWidget(self.catlist,0,0)
    self.grid.addWidget(self.subcatlist,1,0)    

    
    
    self.showMaximized()
    
  def create_table(self):
    table = QtGui.QTableWidget()
    table.setRowCount(len(self.expense_list))
    table.setColumnCount(3)
    table.setHorizontalHeaderLabels(["date","merchant","amount"])
    #table.resize(400,250)    
    
    self.current_cat = str(self.catlist.currentText())
    self.current_subcat = str(self.subcatlist.currentText())
    
    print self.current_cat,self.current_subcat
    
    self.category_list = categorize.extract_category(self.current_cat,self.current_subcat,self.expense_list)
    self.category_list.sort(key=lambda x: x["date"], reverse=False)

    
    for row,expense in enumerate(self.category_list):    
      date = QtGui.QTableWidgetItem(str(expense["month"])+"/"+str(expense["date"])+"/"+str(expense["year"]))
      merchant = QtGui.QTableWidgetItem(expense["merchant"])
      amount = QtGui.QTableWidgetItem(str(expense["amount"]))
      table.setItem(row,0,date)
      table.setItem(row,1,merchant)
      table.setItem(row,2,amount)
          
    self.grid.addWidget(table,2,0)
    
  def change_subcat(self):
    print "index changed"
    self.subcatlist = QtGui.QComboBox()
    category = str(self.catlist.currentText())
    self.subcatlist.currentIndexChanged.connect(self.create_table)    
    self.subcatlist.addItem("All")
    if category == "All":
      pass
    else:  
      for item in self.cat.categories[category]:
        print item
        self.subcatlist.addItem(item)
    self.grid.addWidget(self.subcatlist,1,0)
    print ""
    self.create_table()
  
def main(expense_list):
  
  app = QtGui.QApplication(sys.argv)
  w = window(expense_list)
  app.exec_()
  
def month():
    
  min_date,max_date = files.find_range() 
  now = datetime.datetime.now()   
  year = user_input.option_num("Enter year:",2017,max_date[1],now.year)
  month = user_input.option_num("Enter month:",1,12,now.month)  
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