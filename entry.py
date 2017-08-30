from datetime import datetime
import calendar
import pickle 
import os


def define_expense_categories():
  category = {'Travel/Transportation':['Gas','Car Maintenance','Airfare','Bus/Train Tickets','Lodging','Parking','Fees','Tolls','Car Purchase','Insurance'],
              'Housing':              ['Rent','Mortgage','Maintenance/Repairs','Insurance'],
              'Health Care':          ['Co-Pays','Co-Insurance','Deductible','Dental','Vision','NFP'],
              'Utilities':            ['Electric','Water','Trash','Phone','Cable','Internet'],
              'Food':                 ['Groceries','Restaurants','Take-Out','Coffee'],
              'Entertainment':        ['Admission/Tickets','Alcohol','Desert/Treats'],
              'Personal':             ['Clothes','Shoes','Salon','Cosmetics','Laundry','Hygiene Products','Subscriptions','Shopping'],
              'Giving':               ['Tithing','Charity','Gifts']}
  
###############################################################################################################################################    
  
def input_num(prompt,minimum,maximum,default=""):
  num = raw_input(prompt+" ")
  if default and num == "":
    print "  Default value selected: "+str(default)
    return default  
  while test_int(num) == False or int(num) < minimum or int(num) > maximum:
    print "  Error: entry must be an integer between "+str(minimum)+" and "+str(maximum)
    num = raw_input(prompt+" ") 
    
  print ""  
  return int(num)
  
##############################################################################################################################################  

def input_yes_no(prompt):
  ans = raw_input(prompt+" ")
  while ans != "y" and ans != "n":
    print '  Error: entry must be either "y" or "n"'
    ans = raw_input(prompt+" ")
  
  print ""
  return ans
  
##############################################################################################################################################    
  
def make_entries():
  print "Make entries"
  
  now = datetime.now()  
  year = input_num("Enter year:",2017,now.year,now.year)
  month = input_num("Enter month:",1,12,now.month)
  expense_list = load_file("month",month,year)
  merchant_list = load_file("merchant")
  
  keep_going = "y"
  while keep_going == "y":
    entry = make_entry(month,year,expense_list,merchant_list)
    keep_going = input_yes_no("Enter another expense? ")
    
    
  
##############################################################################################################################################

def make_entry(month,year,expense_list,merchant_list):
  end_day = calendar.monthrange(year,month)[1]
  now = datetime.now()    
  date = input_num("Enter date:",1,end_day,now.day)
  
  
############################################################################################################################################## 

def load_file(ftype,month="",year=""):
  if ftype == "month":
    fname = "./month_archive/"+calendar.month_name[month] + "_" + str(year) + ".p"
  elif ftype == "merchant":
    fname = "./month_archive/merchants.p"
    
  if not os.path.isfile(fname):
    ans = input_yes_no("Month file does not exist. Would you like to create it (y/n):")
    if ans == "y":
      listobj = []
      pickle.dump(listobj,open(fname,"wb"))
    else:
      print "Exiting..."
      stop()
      
  listobj = pickle.load(open(fname,"rb"))
  return listobj
  
  
##############################################################################################################################################    
  
def test_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
    
  
##############################################################################################################################################  
  
def stop():
  raise SystemExit(0)
  