x=0
while(True):
    st=input("Enter a string:")
    if (st[0]=='Z' or st[-1]=='Z'):
        break
    if (st[0]=='X' and st[-1]=='X'):
        x+=1
print(x)
    