import sys


S = input().strip()

try:
    print (int(S))
except ValueError:
    print ("Bad String")


class Calculator(object):
    def __init__(self):
        self.object = object
    def power(self,n,p):
        self.n = n
        self.p = p
        try:
            return(n**p)
        except ValueError:
            print('n and p should be non-negative')
