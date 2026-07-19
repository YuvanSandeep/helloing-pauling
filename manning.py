def absolute_value (num):
    if num >= 0:
        return num
    else:
        return -num
    
print (absolute_value(2))
print (absolute_value(-4))
print (absolute_value(int(input("What number do you want to make positive?"))))