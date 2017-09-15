import user_input
import pickle   
import os
import calendar
import datetime
import shutil

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
    shutil.copyfile(fname,fname+'-backup')
    pickle.dump(obj,open(fname,"wb"))

##############################################################################################################################################

def find_range():

  files = os.listdir("./month_archive/")
  
  min_start = datetime.datetime(2200,1,1)
  max_end = datetime.datetime(1950,1,1)
  for f in files:
    if f.find("_") > 0 and f.find("-backup") < 0:
      
      name = f.split(".")[0]
      month,year = name.split("_")
      month = datetime.datetime.strptime(month,'%B').month
      year = int(year)
      last_day = calendar.monthrange(year,month)[1]      
      start = datetime.datetime(year,month,1)
      end = datetime.datetime(year,month,last_day)


      if start < min_start:
        min_start = start
        min_month = month
        min_year = year
      if end > max_end:
        max_end = end
        max_month = month
        max_year = year

  return [[min_month,min_year],[max_month,max_year]]


##############################################################################################################################################