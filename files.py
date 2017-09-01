import user_input
import pickle   
import os
import calendar

############################################################################################################################################## 

def manage(ftype,task,month="",year="",obj=""):
  if ftype == "Month":
    fname = "./month_archive/"+calendar.month_name[month] + "_" + str(year) + ".p"
  elif ftype == "Merchant":
    fname = "./month_archive/merchants.p"
  
  if task == "load":
    if not os.path.isfile(fname):
      ans = user_input.yes_no(ftype+" file does not exist. Would you like to create it (y/n):")
      if ans == "y":
        listobj = []
        pickle.dump(listobj,open(fname,"wb"))
      else:
        print "Exiting..."
        stop()
      
    listobj = pickle.load(open(fname,"rb"))
    return listobj
    
  elif task == "dump":
    pickle.dump(obj,open(fname,"wb"))

##############################################################################################################################################