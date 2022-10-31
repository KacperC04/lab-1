#1
from __future__ import print_function
import os
import sys
import platform
import sysconfig


print("os.name                    ",    os.name)
print("sys.platform                    ",    sys.platform)
print("platform.system()                    ",    platform.system())
print("sysconfig.get_platform()                    ",    sysconfig.get_platform())
print("platform.machine()                    ",    sysconfig.get_platform())
print("platform.architecture()                    ",    platform.architecture())



#2
import sys
n = len(sys.argv)
print("the total arguments whihc have been passeed", n)

print("\nName of python script:", sys.argv[0])
print("\nArguments passed:", end = " ")
for i in range(1, n):
    print(sys.argv[i], end = " ")

sum = 0
for i in range(1, n):
    sum += int(sys.argv[i])
print("\n\nResult:", sum)

#3
import sys
import numpy
#need too ewrite code here
def main():
    script = sys.argv[0]
    filename = sys.argv[1]
    data = numpy.loadtxt(filename, delimiter=',')
    for m in numpy.mean(data, axis=1):
        print(m)

if __name__ == '__main__':
   main()

#4
import webbrowser
url = 'https://youtube.com'
webbrowser.open_new_tab(url)
if webbrowser = True:
    print("website works")
else:
    print("website does not work")

#5


