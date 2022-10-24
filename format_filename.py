import os
import re

"""
 This is a script that renames all file names in a directory.
 substitutes " " for _
 subsittutes - for _
 renames filename to all lowercase. 
"""


if __name__ == '__main__':
    os.chdir('/Users/tylercranmer/Dev')



    for index, name in enumerate(os.listdir()):
        
        new_name = re.sub(" ", "_", name)
        new_name = re.sub("-","_", new_name)
        new_name = new_name.lower()
        if name != new_name:
            os.rename(name, new_name)
    print(os.listdir())