

###############################################################################################################################################    
  
def option_num(prompt,minimum,maximum,default="-1"):
  num = raw_input(prompt+" ")
  if default != "-1" and num == "":
    print "  Default value selected: "+str(default)
    return default  
  while test_int(num) == False or int(num) < minimum or int(num) > maximum:
    print "  Error: entry must be an integer between "+str(minimum)+" and "+str(maximum)
    num = raw_input(prompt+" ") 
    
  print ""  
  return int(num)
  
##############################################################################################################################################  

def amount(prompt,minimum,maximum):
  amnt = raw_input(prompt+" ")
  while test_float(amnt) == False or float(amnt) <= minimum or float(amnt) > maximum:
    print "  Error: entry must be a float between "+str(minimum)+" and "+str(maximum)
    amnt = raw_input(prompt+" ")
    
  print ""
  return float(amnt)
  
##############################################################################################################################################  

def yes_no(prompt):
  ans = raw_input(prompt+" ")
  while ans != "y" and ans != "n":
    print '  Error: entry must be either "y" or "n"'
    ans = raw_input(prompt+" ")
  
  print ""
  return ans
  
##############################################################################################################################################  

def from_menu(header,options,prompt,rtrn_opt=2):
  print ""
  print header
  for i,opt in enumerate(options):
    print "  ",i+1," - ",opt
    
  num = option_num(prompt,1,len(options))   
  idx = num-1
  opt = options[idx]
  
  if rtrn_opt == 1:
    return opt     
  else:
    return [idx,opt] 
  
##############################################################################################################################################    

#def from_list():
  #ans = raw_input(prompt+" ")
  #match == "n"
  #while match == "n":
    #if ans in ls:
      #match == "y"
    #else:
      
      

##############################################################################################################################################    

  
def test_int(s):
  try:
    int(s)
    return True
  except ValueError:
    return False
    
    
##############################################################################################################################################    
  
def test_float(s):
  try:
    float(s)
    return True
  except ValueError:
    return False    
  
##############################################################################################################################################  
  
def stop():
  raise SystemExit(0)  