
import sys

# count the arguments
arguments = len(sys.argv) - 1
print ("the script is called with %i arguments" % (arguments))
print("partha")
a= arguments[0]
b= arguments[1]

if (arguments[2] == "add"):
    c=a+b
elif (arguments[2] == "sub"):
    c=a-b
elif (arguments[2] == "mul"):
    c=a*b
elif (arguments[2] == "div"):
    c=a/b
print(c)