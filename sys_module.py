import sys

# sys.stdin: standard input
inputStatement = sys.stdin.readline()
inputStatement1 = sys.stdin.readline(10) # only reads the 10 first chars

sys.stdout.write('This module is nice.\n')

print('Version and stuff: ' + sys.version) # gives the version of python, the date and other stuff