#!/usr/bin/python3
#command testing python
import os
print("enter something: ",end="")
x=input()
while x:
    if x:
        print("Type command: ",end="")
        cmd=input()
        os.system(cmd)