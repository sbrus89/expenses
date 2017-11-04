

class user_input:
  
  def __init__(self,allow_exceptions):
    
    if allow_exceptions:
      self.exceptions = ["undo","redo"]
    else: 
      self.exceptions = []    
  

  ###############################################################################################################################################    
  
  def option_num(self,prompt,minimum,maximum,default="-1"):
    if default != "-1":
      initial_prompt = prompt+" "+"(default: "+str(default)+")"
    else:  
      initial_prompt = prompt    
    
    num = raw_input(initial_prompt+" ")  
    if default != "-1" and num == "":
      print "  Default value selected: "+str(default)
      return int(default)
    
    while 1:
      if num in self.exceptions:
	print ""
	return num
      elif self.test_int(num) == False or int(num) < minimum or int(num) > maximum:
	print "  Error: entry must be an integer between "+str(minimum)+" and "+str(maximum)
        num = raw_input(prompt+" ") 
      else:
	print ""
	return int(num)
	
    #while num not in self.exceptions or self.test_int(num) == False or int(num) < minimum or int(num) > maximum: 
      #print "  Error: entry must be an integer between "+str(minimum)+" and "+str(maximum)
      #num = raw_input(prompt+" ") 
    
    #print ""  
    #return int(num)
  
  ##############################################################################################################################################  

  def amount(self,prompt,minimum,maximum):
    amnt = raw_input(prompt+" ")
    while 1:
      if amnt in self.exceptions:
	print ""
	return amnt
      elif self.test_float(amnt) == False or float(amnt) <= minimum or float(amnt) > maximum:
        print "  Error: entry must be a float between "+str(minimum)+" and "+str(maximum)
        amnt = raw_input(prompt+" ")  	
      else:
	print ""
	return float(amnt)
    
    #while test_float(amnt) == False or float(amnt) <= minimum or float(amnt) > maximum:
      #print "  Error: entry must be a float between "+str(minimum)+" and "+str(maximum)
      #amnt = raw_input(prompt+" ")            
    
    #print ""
    #return float(amnt)
  
  ##############################################################################################################################################  

  def yes_no(self,prompt,default="-1"):
    if default != "-1":
      initial_prompt = prompt+" "+"(default: "+str(default)+")"
    else:  
      initial_prompt = prompt
    
    ans = raw_input(initial_prompt+" ")
    if default != "-1" and ans == "":
      print "  Default value selected: "+str(default)
      return default    
    
    while 1:
      if ans in self.exceptions:
	print ""
	return ans
      elif ans != "y" and ans != "n":
        print '  Error: entry must be either "y" or "n"'
        ans = raw_input(prompt+" ")    
      else:
	print ""
	return ans
	        
    #while ans != "y" and ans != "n":
      #print '  Error: entry must be either "y" or "n"'
      #ans = raw_input(prompt+" ")
  
    #print ""
    #return ans
  
  ##############################################################################################################################################  

  def from_menu(self,header,options,prompt,rtrn_opt=2):
    print ""
    print header
    for i,opt in enumerate(options):
      print "  ",i+1," - ",opt
    
    num = self.option_num(prompt,1,len(options))   
    idx = num-1
    opt = options[idx]
  
    if rtrn_opt == 1:
      return opt     
    else:
      return [idx,opt] 
  
  ##############################################################################################################################################    
  
  def test_int(self,s):
    try:
      int(s)
      return True
    except ValueError:
      return False    
    
  ##############################################################################################################################################    
  
  def test_float(self,s):
    try:
      float(s)
      return True
    except ValueError:
      return False    
  
##############################################################################################################################################  
  
def stop():
  raise SystemExit(0)  