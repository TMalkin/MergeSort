
# def factorial(x):
#     if(x == 1):
#         return 1
#     else:
#         return factorial(x-1) * x
# print(factorial(74))

# def fibonacci(y):
#     if(y == 1):
#         return 1
#     elif(y == 2):
#         return 2
#     else:
#         return fibonacci(y-1) + fibonacci(y-2)
# print(fibonacci(736))
def merge(sar1,sar2):
    new_array = []
    x = 0
    y = 0
    while(len(sar1) >= x+1 and len(sar2) >= y+1):
        if(sar1[x] > sar2[y]):
            new_array.append(sar2[y])
            y = y+1
        else:
            new_array.append(sar1[x])
            x = x+1
    if(len(sar1) >= x+1):
        for v in range(0, len(sar1)- x):
            new_array.append(sar1[x])
    else:
        for e in range(0, len(sar2) - y):
            new_array.append(sar2[y+e])
    return new_array
def merge_sort(originali):
    coriginali = []
    for n in range(0, len(originali)):
        coriginali.append(originali[n])
    if(len(originali) == 1 or len(originali) == 0):
        return coriginali
    Fhalf = originali[:len(originali) //2]
    Shalf = originali[len(originali) //2:]
    r1 = merge_sort(Fhalf)
    r2 = merge_sort(Shalf)
    finito = merge(r1,r2)
    return finito

l = [6,3,4,7,2,5,7,3,5,2,9,4,6]
print(merge_sort(l))
