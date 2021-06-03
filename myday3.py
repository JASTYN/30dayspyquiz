import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    if N%2 != 0:
        print("Weird")
    elif N%2==0 and N in range(1,6):
        print("Not weird")
    elif N%2==0 and N in range(6,20):
        print("Weird")
    elif N%2==0 and N>20:
        print("Not weird")