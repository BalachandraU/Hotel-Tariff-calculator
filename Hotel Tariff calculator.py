mon=int(input())
rent=int(input())
days=int(input())
a=0
if mon in [4,5,6,11,12]:
    a=[rent*(100+20)//100]*days
    print(a)
elif mon in[1,2,3,7,8,9,10]:
    a=rent*days
    print(a)
else:
    print("Invalid Input")
