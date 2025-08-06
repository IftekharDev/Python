
import os

#### ------- dir(os) -------
'''
Returns a list of all names (functions, constants, submodules) defined in the os module at runtime.
'''
# print(dir(os))
# print(dir(os)[:15])


#### ------- os.listdir(path='.') -------
'''
Returns a Python list of filenames (and directory names) present in path. Default is the current directory '.'.
'''

# print(os.listdir())

# files = os.listdir('.')
# print(files)


#### ------- os.getcwd() -------

'''
Returns the absolute path to the process's current working directory.
'''

# cwd = os.getcwd()
# print("We are in: ", cwd)


#### ------- os.chdir(path) -------

'''
Changes the current working directory to path.
'''
# print(os.chdir(r"C:/LearningVault/Python/miscellaneous"))
# print(os.getcwd())

# os.chdir(r"C:/LearningVault/Python")
# print(os.getcwd())


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
# os.remove('archive_2025.txt')


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