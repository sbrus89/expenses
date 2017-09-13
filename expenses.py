import user_input
import entry
import show


def main_menu():
 
  options = [['Make entries',      entry.make_entries],
             ['Edit an entry',     entry.edit_entry],
             ['Show month',        show.month],
             ['Show range',        show.month_range],
             ['Show merchant list',show.merchant_list],
             ['Exit',              user_input.stop]]
     
     
  [idx,opt] = user_input.from_menu("Main Menu:",[opt[0] for opt in options],"Choose option:") 
  options[idx][1]()
    
  
  
  
while 1:
  main_menu()    