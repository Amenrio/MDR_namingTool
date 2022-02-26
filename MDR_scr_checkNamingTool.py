import os
import logging
import libraries.MDR_library_variableNames_v01 as VARS
LIST_ERRORS = []
def run():
    for root, dirs, files in os.walk("P:/"):
        for f in files:
            file_name, file_ext = os.path.splitext(f)
            print(file_name)
            if check_id(file_name,file_ext) == 1:
                LIST_ERRORS.append(os.path.join(root,f))
            check_spaces(root, f)
    for e in LIST_ERRORS:
        print(e)        
def check_spaces(root,file):
    if(file.find(" "))>0:
        LIST_ERRORS.append(os.path.join(root,file))

def check_id(file,extension):
    file_formatted = VARS.get_nice_name(file)
    if file_formatted[0] not in VARS.proyect_id.values():
        return 1
    else:
        return 0

run()

