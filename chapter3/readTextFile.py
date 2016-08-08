import os

file_name = raw_input('Enter filename:')
if os.path.exists(file_name):
    file_name = open(file_name, 'r')
    for eachLine in file_name:
        print eachLine.strip()
else:
    print 'no file'