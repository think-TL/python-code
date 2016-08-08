import os

ls = os.linesep
while True:
    file_name = raw_input('Please input filename: ')
    try:
        file_open = open(file_name, 'r')
    except IOError, e:
        file_content = []
        print "\nEnter lines('.' by itself to quit).\n"
        while True:
            entry = raw_input('----> ')
            if entry == '.':
                break
            else:
                file_content.append(entry)
        file_open = open(file_name, 'w')
        file_open.writelines(['%s%s' % (x, ls) for x in file_content])
        print 'DOWN!'
        break
    else:
        print "ERROR:'%s'already exists" % file_name
    finally:
        file_open.close()

"""
    widow 64 os.linesep \r\n
    ubuntu linux 64 \n
    Centos7 64 \n
    mac os \n
"""