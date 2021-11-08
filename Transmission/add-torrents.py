import os


file = open('input.txt', 'r')
lines = file.readlines()

for index, line in enumerate(lines):
    # print('transmission-remote -a', line)
    os.system('transmission-remote -a "%s"' % line)
    
file.close()