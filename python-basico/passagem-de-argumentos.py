import sys


arg = sys.argv


def sum(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

if arg[1] == "soma":
    resp = sum(float(arg[2]), float(arg[3]))
elif arg[1] == 'sub':
    resp = sub(float(arg[2]), float(arg[3]))

print(resp)