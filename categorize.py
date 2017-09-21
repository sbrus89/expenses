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
    
##############################################################################################################################################                     
                     
  def get_category(self):
    cat = user_input.from_menu("Enter category:",sorted(self.categories.keys()),"Choose category:",1)
    self.current_category = cat
    return cat
    
##############################################################################################################################################        
    
  def get_sub_category(self):
    scat = user_input.from_menu("Enter sub-category:",sorted(self.categories[self.current_category]),"Choose sub-category",1)
    return scat
    