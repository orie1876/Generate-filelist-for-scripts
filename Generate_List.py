# -*- coding: utf-8 -*-
"""
Spyder Editor
This is a temporary script file.
"""

import os

def init():
    fp = (r"/Users/Mathew/Desktop/Craig_media/Files from Craig/")
    print_dirs(3, fp)

def print_dirs(step, fp):
    print('\n\n')
    count = 0
    done = []
    for root, dirs, files in os.walk(fp):
        for name in files:
            if step == 1:
                if 'allfitswithheader_cluster.txt' in name:
                    for_ij = r'path[{0}]="{1}\";'.format(count, root)
                    if root not in done:
                        done.append(root)
                        print(for_ij.replace('\\', '/'))
                        count += 1
            elif step == 2:
                if 'Fitresults' in name:
                    for_py = 'pathList.append(r"{0}")'.format(root)
                    print(for_py)
            elif step == 3:

                if 'Fitresults' in name:
                    for_igor = r'filelist[{0}]="{1}\"'.format(count, root)
                    for_igor = for_igor.replace('/',':')
                    for_igor = for_igor.replace(':Users','Macintosh HD:Users')
                    print(for_igor.replace('\\', ':'))
                    
                    count += 1
            elif step == 4:
                if 'All_Localisation_Information.txt' in name:
                    for_py = 'pathList.append(r"{0}")'.format(root)
                    print(for_py)
                    #print name
init()