import sys
from PyQt4 import QtGui
import user_input
import datetime
import files
import pprint

class window(QtGui.QWidget):
  
  def __init__(self):
    
    super(window,self).__init__()
    self.initUI()
    
  def initUI(self):
    
    #self.setGeometry(300,300,250,150)
    self.setWindowTitle('Test')
    
    self.show()
    
def main():
  
  app = QtGui.QApplication(sys.argv)
  w = window()
  app.exec_()
  
def month():
  
  
  min_date,max_date = files.find_range() 
  now = datetime.datetime.now()   
  year = user_input.option_num("Enter year:",2017,max_date[1],now.year)
  month = user_input.option_num("Enter month:",1,12,now.month)  
  expense_list = files.manage("Month","load",month,year)  
  pprint.pprint(expense_list)
  
def month_range():  

  min_date,max_date = files.find_range() 
  start_year = user_input.option_num("Enter starting year:",2017,min_date[1],min_date[1])
  start_month = user_input.option_num("Enter starting month:",1,12,min_date[0])
  end_year = user_input.option_num("Enter ending year:",2017,max_date[1],max_date[1])
  end_month = user_input.option_num("Enter ending month:",1,12,max_date[0])
  
  main()
  
def merchant_list():
  
  merchant_list = files.manage("Merchant","load")
  pprint.pprint(merchant_list)