import os

def make_text_file():
    ls = os.linesep
    while True:
        file_name = raw_input('Please input filename: ')
        try:
            file_open = open(file_name, 'r')
        except IOError as e:
            file_content = []
            print "\nEnter lines('.' by itself to quit).\n"
            while True:
                entry = raw_input('>>')
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


def read_text_file():
    file_name = raw_input('Enter filename:')
    if os.path.exists(file_name):
        file_name = open(file_name, 'r')
        for eachLine in file_name:
            print eachLine.strip()
    else:
        print 'no file'

