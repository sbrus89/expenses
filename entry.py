from datetime import datetime
import calendar
import user_input
import categorize
import files
import merchant

  

##############################################################################################################################################    
  
def make_entries():
  print "Make entries"
  
  now = datetime.now()  
  year = user_input.option_num("Enter year:",2017,now.year,now.year)
  month = user_input.option_num("Enter month:",1,12,now.month)
  
  expense_list = files.manage("Month","load",month,year)
  merchant_list = files.manage("Merchant","load")
  merch = merchant.input_merchant(merchant_list)  
  
  keep_going = "y"
  while keep_going == "y":
    entry = make_entry(month,year,expense_list,merch)
    keep_going = user_input.yes_no("Enter another expense? ")
  files.manage("Month","dump",month,year,expense_list)
  files.manage("Merchant","dump",obj=merchant_list)
    
  
##############################################################################################################################################

def make_entry(month,year,expense_list,merch):
  
  end_day = calendar.monthrange(year,month)[1]
  now = datetime.now()   
  
  cat = categorize.category()
  people = ["Aleshia","Steven","Both"]
  
  info = [["month",        month,                     []],
          ["year",         year,                      []],
          ["date",         user_input.option_num,     ["Enter date:",1,end_day,now.day]],
          ["note",         raw_input,                 ["Enter note: "]],          
          ["category",     cat.get_category,          []],
          ["sub-category", cat.get_sub_category,      []],
          ["merchant",     merch.get_seller,          []],
          ["amount",       user_input.amount,         ["Enter amount:",0.0,20000.0]],
          ["for",          user_input.from_menu,      ["Enter person purchase is for:",people,"Choose person:",1]]]
     
  for inquiry in info:
    if callable(inquiry[1]):
      response = inquiry[1](*inquiry[2])
      inquiry[1] = response
  
  entry = {}
  for i in info:
    entry[i[0]] = i[1]
    
  print entry
  expense_list.append(entry)
  print expense_list
  
############################################################################################################################################## 

  
  

  