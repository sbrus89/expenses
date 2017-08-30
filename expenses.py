import entry


def main_menu():
 
  options = [['Make entries'   ,entry.make_entries],
             ['Edit and entry' ,''],
             ['Show month'     ,''],
             ['Show range'     ,''],
             ['Exit',entry.stop]]
   
  print ""
  print "Main Menu:"
  for i,opt in enumerate(options):
    print "  ",i+1," - ",opt[0]
    
  num = entry.input_num("Choose an option:",1,len(options))
  options[num-1][1]()
    
  
    
    
while 1:
  main_menu()    