import sys
from PyQt4 import QtGui
import user_input
import datetime
import files
import pprint

class window(QtGui.QWidget):
  
  def __init__(self,expense_list):
    
    super(window,self).__init__()
    self.initUI(expense_list)
    
  def initUI(self,expense_list):
    
    #screen = QtGui.QDesktopWidget().screenGeometry()
    #self.setGeometry(0,0,screen.width(),screen.height())
    #self.setGeometry(300,300,250,150)
    self.setWindowTitle('Test')
    
    grid = QtGui.QGridLayout()
    self.setLayout(grid)
    table = self.create_table(expense_list)
    table.setHorizontalHeaderLabels(["date","merchant","amount"])
    table.resize(400,250)
    grid.addWidget(table,0,0)
    grid.addWidget(table,0,1)
    
    self.showMaximized()
    
  def create_table(self,expense_list):
    table = QtGui.QTableWidget()
    table.setRowCount(len(expense_list))
    table.setColumnCount(3)
    
    for row,expense in enumerate(expense_list):
      date = QtGui.QTableWidgetItem(str(expense["month"])+"/"+str(expense["date"])+"/"+str(expense["year"]))
      merchant = QtGui.QTableWidgetItem(expense["merchant"])
      amount = QtGui.QTableWidgetItem(str(expense["amount"]))
      table.setItem(row,0,date)
      table.setItem(row,1,merchant)
      table.setItem(row,2,amount)
    return table
  
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
  pprint.pprint(expense_list)
  
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