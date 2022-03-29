import os
import logging
import libraries.MDR_library_variableNames_v01 as VARS
LIST_ERRORS = []
def run():
    for root, dirs, files in os.walk("P:/"):
        if "99_tools" in dirs:
            dirs.remove("99_tools")
        if "workspace.mel" in files:
            files.remove("workspace.mel")
        for f in files:
            file_name, file_ext = os.path.splitext(f)
            check_id(root, file_name, file_ext)
                
            check_spaces(root, f)
    for e in LIST_ERRORS:
        print(e)        
def check_spaces(root,file):
    if(file.find(" "))>0:
        LIST_ERRORS.append(os.path.join(root,file))

def check_id(root,file,extension):
    file_formatted = VARS.get_nice_name(file)
    if file_formatted[0] not in VARS.project_id.values():
        LIST_ERRORS.append(os.path.join(root,file))

run()

