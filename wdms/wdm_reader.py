# -*- coding: utf-8 -*-

#------------Import Python Modules-----------#
import os
from wdmtoolbox import wdmtoolbox
import pandas as pd
#--------------------------------------------#
# Documentation is at https://timcera.bitbucket.io includes the following:
# wdmtoolbox.extract(*wdmpath, **kwds) - print DSN data to screen
# wdmtoolbox.cleancopywdm(inwdmpath,outwdmpath, overwrite=False)
# wdmtoolbox.csvtowdm(wdmpath,dsn,input=None, start_date=None,end_date=None,columns=None, input_ts='-'/)
#----Assign Directory & file paths
directory = "C:\\workspace\lffs_public\wdms"
wdm_file = "DIV_PM7_4580_4820.wdm"
ps_file = "PM7_4580_4820.DIV"


#----Create a string variabe combining the filename & filepath
f1 = os.path.join(directory,wdm_file)

#----Read in wdm file
#raw_data = wdmtoolbox.extract(f1,1) #1 is the number of column values in the file
#wdmtoolbox.listdsns(f1)
wdmtoolbox.listdsns("DIV_PM7_4580_4820.wdm")
#wdmtoolbox.createnewwdm("test.wdm")
#----Print the top few rows of the dataframe object to the console
#print(raw_data.head())

#----Get Description of the wdm file contents
#print("\n File Contents: \n")
#wdmtoolbox.describedsn(wdm_file,1)

#----Write the contents of the original wdm file (in dataframe format) to a text file
#raw_data.to_csv('wdm_file.txt')

#----Create a new wdm dataframe & change all values to 500:
#col_name = wdm_file + "_DSN_1" #Default column name is file name + _DSN_1
#new_file = raw_data
#new_file[col_name] = 500.0

#----Write the contents of the new wdm file (in dataframe format) to a text file
#new_file.to_csv(os.path.join(directory,'new_file.txt'))
