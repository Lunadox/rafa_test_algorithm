a=10
b=1

try:
    c=a/b
except ZeroDivisionError:
    c=a/1

print(c)