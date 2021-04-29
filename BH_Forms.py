import pandas as pd
import os
import fnmatch
import re
import shutil
import glob


#match_directory = [glob.glob("/home/matchdirectory/*.tif"))]
path = r'V:\syshr'
dest_path = r'V:\BH Forms'
#match_directory = "v:/BH Forms"
csv = pd.read_csv(r'C:\Users\u370443\PycharmProjects\Files.csv')
file_list = csv.values.T[3].tolist()
# There were some NULL values
file_list = [str(i) for i in file_list]
# Returns V:\SYSHR\97037\C3G1LZ013592030U8.TIF as C3G1LZ013592030U8.TIF
file_extension = [re.findall("[a-z0-9A-Z_]+\.\w+", i) for i in file_list]
TIF_files = [i[0] for i in file_extension if i]
#matches TIF_files to those in match_directory
#result = [i for i in match_directory if i.endswith(tuple(TIF_files))]
for root, dirs, files in os.walk(path):
    for dir in dirs:
        if dir[0] == '9':
            sub = [n for n in dir]
                if files in TIF_files:
                    copy_file = os.path.join(root, files )
                    shutil.copy(copy_file, dest_path)
#
# for i in result:
#
