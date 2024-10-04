# 4. Write a python program to print the contents of a directory using the os module. 
# Search online for the function which does that.  


# 5. Label the program written in problem 4 with comments. 

import os

# Select the directory whose content you want to list 
directory_path = '/'

# Use the os module to list the directory content 
contents = os.listdir(directory_path)

# Print the contents of the directory 
print(contents)
