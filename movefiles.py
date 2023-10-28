# -*- coding: utf-8 -*-

import os
import fnmatch
import shutil
import random
import math

query_number_percent = 0.5 

directory = "Final_Database"  
databaseClasses = 'Data_PNG'

if not os.path.exists(directory):
    os.makedirs(directory)

newImgDBPath = os.path.abspath(directory)

# walk through the folder
f = open("dataClasses.txt", "w")
g = open("queryImages.txt", "w")
for root, dirs, files in os.walk(databaseClasses):
    for i, str_each_folder in enumerate(dirs):
        # we get the directory path
        str_the_path = '/'.join([root, str_each_folder])

        files_number = len((os.listdir(str_the_path))) 
        
        index = random.sample(range(0, files_number), int(math.floor(query_number_percent*files_number)))
        # list all the files using directory path
        for ind, str_each_file in enumerate(os.listdir(str_the_path)):
            # now add the new one
            str_new_name = '{0:03}'.format(i+1) +'_'+ str_each_folder + '_' + str_each_file
            if ind in index:
                g.writelines('%s\n' % str_new_name)
                # full path for both files
            str_old_name = '/'.join([str_the_path, str_each_file])
            str_new_name = '/'.join([newImgDBPath, str_new_name])

            # now rename using the two above strings and the full path to the files
            # os.rename(str_old_name, str_new_name) 
            shutil.copy2(str_old_name, str_new_name) 

        #  we can print the folder name so we know that all files in the folder are done
        print('%s, %d images' % (str_each_folder, files_number))
        f.writelines('%s %d\n' % ('{0:03}'.format(i+1)+'_'+str_each_folder, files_number))
g.close
f.close