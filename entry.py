from datetime import datetime
import calendar
import user_input
import categorize
import files
import merchant

##############################################################################################################################################    

def init_entries():
  
  now = datetime.now()  
  get_input = user_input.user_input(1)
  year = get_input.option_num("Enter year:",2017,now.year,now.year)
  month = get_input.option_num("Enter month:",1,12,now.month)
  
  expense_list = files.manage("Month","load",month,year)
  merchant_list = files.manage("Merchant","load")
  merch = merchant.input_merchant(merchant_list)  
  
  end_day = calendar.monthrange(year,month)[1]
  now = datetime.now()   
  
  cat = categorize.category()
  people = ["Aleshia","Steven","Both"]  
  
          # dictionary key # function                 # function arguments                                         #result 
  info = [["month",        month,                     [],                                                          month],
          ["year",         year,                      [],                                                          year ],
          ["date",         get_input.option_num,      ["Enter date:",1,end_day,now.day],                           None ],          
          ["category",     cat.get_category,          [],                                                          None ],
          ["sub-category", cat.get_sub_category,      [],                                                          None ],
          ["merchant",     merch.get_seller,          [],                                                          None ],
          ["amount",       get_input.amount,          ["Enter amount:",0.0,20000.0],                               None ],
          ["for",          get_input.from_menu,       ["Enter person purchase is for:",people,"Choose person:",1], None ],
          ["note",         raw_input,                 ["Enter note: "],                                            None ]]    
          
  return month,year,expense_list,merchant_list,info 

##############################################################################################################################################    

  
def make_entries():
  print "Make entries"
  
  month,year,expense_list,merchant_list,info = init_entries()
  get_input = user_input.user_input(0)
  
  keep_going = "y"
  while keep_going == "y":
    entry = make_entry(expense_list,info)
    keep_going = get_input.yes_no("Enter another expense?")
    
  save = get_input.yes_no("Save entries?","y")  
  if save == "y":
    files.manage("Month","dump",month,year,expense_list)
    files.manage("Merchant","dump",obj=merchant_list)
    
  
##############################################################################################################################################

def make_entry(expense_list,info):
       
  i = 0
  while i < len(info):
    
    inquiry = info[i]
    
    if callable(inquiry[1]):
      response = inquiry[1](*inquiry[2])
      if response == "redo":
	i = 0
      elif response == "undo":
	if i > 0:  
	  i = i-2
      else:
        inquiry[3] = response
        
    i = i+1
    
  entry = {}
  for i in info:
    entry[i[0]] = i[3]
    
  print entry
  expense_list.append(entry)
  print expense_list
  
############################################################################################################################################## 

def edit_entry():
  
  month,year,expense_list,merchant_list,info = init_entries()
  
  menu = make_expense_menu(expense_list)
  
  get_input = user_input.user_input(0)
    
  idx,opt = get_input.from_menu("Enter expense number:",menu,"Choose expense:",2)
  
  
  for inquiry in info:
    if callable(inquiry[1]):
      ans = get_input.yes_no('Edit '+inquiry[0]+'?')
      if ans == 'y':
        response = inquiry[1](*inquiry[2])
        inquiry[1] = response
      else:
        inquiry[1] = expense_list[idx][inquiry[0]]
  
  for i in info:
    expense_list[idx][i[0]] = i[1] 
    
  files.manage("Month","dump",month,year,expense_list)
  files.manage("Merchant","dump",obj=merchant_list)    
  
############################################################################################################################################## 

def delete_entry():
    
  month,year,expense_list,merchant_list,info = init_entries()
  
  menu = make_expense_menu(expense_list)
  
  get_input = user_input.user_input(0)  
    
  idx,opt = get_input.from_menu("Enter expense number:",menu,"Choose expense:",2)

  item = expense_list.pop(idx)
  
  print item
  ans = get_input.yes_no("Delete_entry? ")
  if ans == "y":
    files.manage("Month","dump",month,year,expense_list)  
  
############################################################################################################################################## 
  
def make_expense_menu(expense_list):

  menu = []
  for expense in expense_list:
    
    exp = {}
    for key in expense:
      exp[key] = str(expense[key])
      
    item = exp['month']+'/'+exp['date']+'/'+exp['year']+' $'+exp['amount']+' at '+exp['merchant'] + '\n'  \
           '           category: '+exp['category']+'\n'\
           '           sub-category: '+exp['sub-category']+'\n' \
           '           for: '+exp['for']+'\n' \
           '           note: '+exp['note']
           
    menu.append(item)
    
  return menu
  
############################################################################################################################################## 
  