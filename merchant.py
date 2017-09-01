import readline
import files
import user_input

class input_merchant:
  
  def __init__(self,merchant_list):
      self.ls = merchant_list
      
  def get_seller(self):
    readline.parse_and_bind("tab: complete")
    readline.set_completer(self.complete)    
    name = raw_input("Enter merchant name: ")
    if name not in self.ls:
      ans = user_input.yes_no("  Selected merchant not in list. Would you like to add it?")
      if ans == "y":
        self.ls.append(name)
        print self.ls
      else:
        self.get_seller()
     
    return name
        
        
  def complete(self,text,state):
    if state == 0:
      if text:
        self.matches = [s for s in self.ls if s.startswith(text)]
      else:
        self.matches = self.ls[:]
    try:    
      return self.matches[state]
    except:
      return None