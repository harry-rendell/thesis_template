import os

# Get the current working directory
root_directory = os.getcwd()

# Start printing directories with 'graphics' as a separate directory
print('\\graphicspath{')
for root, dirs, files in os.walk(root_directory):
    for dir_ in dirs:
        if ('draft_graphics' in dir_) or ('draft_graphics' in root):
            directory_path = os.path.relpath(os.path.join(root, dir_), root_directory)
            print('{'+directory_path+'}')
print('}')
print('\\graphicspath{')
# Start printing directories with 'graphics' as a separate directory
for root, dirs, files in os.walk(root_directory):
    for dir_ in dirs:
        if (('graphics' in dir_) or ('graphics' in root)) and not (('draft_graphics' in dir_) or ('draft_graphics' in root)):
            directory_path = os.path.relpath(os.path.join(root, dir_), root_directory)
            print('{'+directory_path+'}')
print('}')
