import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if((n%2==1) or (n%2==0 and n>=6 and n<=20)):
        print("Weird")
    elif(n%2==0 and n>20):
        print("Not Weird")
    else:
        print("Not Weird")
