#!/usr/bin/python
import zipfile
import sys 
import os
import time
output_filename=sys.argv[1]
source_dir=sys.argv[2]

zipf=zipfile.ZipFile(output_filename,'w',allowZip64=True,compression=zipfile.ZIP_DEFLATED)
for path,sondir,filenames in os.walk(source_dir):
    print path,sondir,filenames
    time.sleep(1)
    if filenames:
        for filename in filenames:
            print 'Adding ',path+"/"+filename
            if filename == output_filename :
				continue
                zipf.write(path+os.path.sep+filename)
zipf.close()