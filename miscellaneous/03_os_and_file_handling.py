
import os

#### ------- dir(os) -------
'''
Returns a list of all names (functions, constants, submodules) defined in the os module at runtime.
'''
print(dir(os))
print(dir(os)[:15])


#### ------- os.listdir(path='.') -------
'''
Returns a Python list of filenames (and directory names) present in path. Default is the current directory '.'.
'''

# print(os.listdir())

files = os.listdir('.')
print(files)


#### ------- os.getcwd() -------

'''
Returns the absolute path to the process's current working directory.
'''

cwd = os.getcwd()
print("We are in: ", cwd)


#### ------- os.chdir(path) -------

'''
Changes the current working directory to path.
'''
## print(os.chdir(r"C:/LearningVault/Python/miscellaneous"))
## print(os.getcwd())

## os.chdir(r"C:/LearningVault/Python")
## print(os.getcwd())


#### ------- os.mkdir(path, mode=0o777, *, dir_fd=None) -------

'''
Creates a single new directory named path.
'''

## new_dir = 'reports'
## if new_dir not in os.listdir('.'):
##     os.mkdir(new_dir)


#### ------- os.rename(src, dst) -------

'''
Renames a file or directory
'''
##os.rename('old.pdf', 'archive_2025.txt')
##print('renamed successfully.')


#### ------- os.remove(path) (alias os.unlink) -------

'''
Deletes a file (not a directory). Fails if the file is open on Windows. os.rmdir() is used to remove directory.
'''
## os.remove('archive_2025.txt')


#### ------- os.path.join() -------

'''
Builds paths portably using the right separator.
'''

# full = os.path.join('logs', '2025', 'app.log')
# print(full)


#### ------- oos.path.exists() -------

'''
Quick existence check for files or dirs.
'''

# if not os.path.exists('config.ini'):
#     print("This file doesn't exists")


#### ------- os.makedirs() -------

'''
Recursively create nested dirs (mkdir -p).
'''

##os.makedirs('data/raw/2025', exist_ok=True)


#### ------- os.environ -------

'''
Dict-like access to environment variables.
'''

##token = os.environ.get('API_TOKEN', '')   ## from .env file




#### ---------- File Handling --------------------


#### ------------Opening and Closing Files-----------

'''
open(file, mode='r', encoding=None, newline=None, buffering=-1)
Creates and returns a file object.


Mode        Meaning                     Notes
'r' 	    read text                   default; file must exist
'w'	        write text, truncate	    creates or overwrites
'a'     	append text	                creates if absent
'r+'    	read and write	            pointer at start
'''

# variable = open('04_text.txt','r')
# print(variable.read())
# variable.close()


# var = open('04_text.txt', 'a')
# var.write("hello")
# var.close()


# var_1 = open('04_text.txt', 'r')
# print(var_1.read())
# var_1.close()


# var3 = open('04_text.txt', 'w')
# var3.write('Hello')
# var3.close()


# var4 = open('04_text.txt', 'w')
# var4.write('new text')
# var4.close()


## -------------------------------------------------------------

# with open('04_text.txt','r') as variable:
#    print(variable.read())


# with open('04_text.txt','a') as variable:
#    print('\n')
#    variable.write('\n')
#    variable.write('baby')
#    print('\n')


with open("04_text.txt", 'r+') as text:
    print(text.read())
    text.write("\n New text added")
    print("New text added successfully")

## ------------------------------------------------------------------------------------------------

'''
read(): Reads the whole file as a single string. Use read() if you want the entire file content in one go.

readline(): Reads one line at a time from the file.
Useful when you want to process each line individually and maintain the line structure.

readlines(): Reads all lines from the file and returns them as a list of strings.
Useful when you want to process each line individually and maintain the line structure.
'''

# with open('04_text.txt', 'r') as a:
#    print(a.read())


# with open('04_text.txt', 'r') as a:
#     lines = a.readlines()

# cleaned_list = [line.strip() for line in lines]
# print(cleaned_list)


