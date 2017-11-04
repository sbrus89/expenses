import user_input

class category:
  
##############################################################################################################################################      
  
  def __init__(self):

    self.categories = {'Travel/Transportation':['Gas','Car Maintenance','Airfare','Bus/Train Tickets','Lodging','Parking','Fees','Tolls','Car Purchase','Insurance'],
                       'Housing':              ['Rent','Mortgage','Maintenance/Repairs','Insurance'],
                       'Health Care':          ['Co-Pays','Co-Insurance','Deductible','Dental','Vision','NFP','Medicines'],
                       'Utilities':            ['Electric','Water','Trash','Phone','Cable','Internet'],
                       'Food':                 ['Groceries','Restaurants','Take-Out','Coffee'],
                       'Entertainment':        ['Admission/Tickets','Alcohol','Desert/Treats'],
                       'Personal':             ['Clothes','Shoes','Salon','Cosmetics','Laundry','Hygiene Products','Subscriptions','Shopping','Home'],
                       'Giving':               ['Tithing','Charity','Gifts','Hosting'],
                       'Investments':          ['IRA','Taxable'],
                       'Education':            ['Loans','Books','Fees']}
                       
    self.current_category = ''  
    self.get_input = user_input.user_input(1)
    
##############################################################################################################################################                     
                     
  def get_category(self):
    cat = self.get_input.from_menu("Enter category:",sorted(self.categories.keys()),"Choose category:",1)
    self.current_category = cat
    return cat
    
##############################################################################################################################################        
    
  def get_sub_category(self):
    scat = self.get_input.from_menu("Enter sub-category:",sorted(self.categories[self.current_category]),"Choose sub-category",1)
    return scat
    
##############################################################################################################################################        
##############################################################################################################################################        

def extract_category(category,sub_category,expense_list):    
  
  category_list = []
  for expense in expense_list:
    if expense["category"] == category or category == "All":
      if expense["sub-category"] == sub_category or sub_category == "All":
        category_list.append(expense)

  return category_list

##############################################################################################################################################        
    