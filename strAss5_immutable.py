s="Python"

try:
    s[0]='python'
except TypeError as e:
    print("Error:",e)