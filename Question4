an={'tiger':1990, 'lion':1995,'bear':2005}



anNames=list(an.keys())
anYrs=list(an.values())

firstYr=3000
firstNm=""

lastYr=0
lastNm=""

for i in anNames:
    if an[i]<firstYr:
        firstYr=an[i]
        firstNm=i
    if an[i]>lastYr:
        lastYr=an[i]
        lastNm=i


print("The FIRST animal arrived to the zoo is: ",firstNm)    
print("That arrived in:",firstYr )    
print()

print("The LAST animal arrived to the zoo is: ",lastYr)    
print("That arrived in:",lastNm )   
print()

delList=[]
for i in an:
    if an[i]>=1990 and an[i]<=1995:
        delList.append(i)
        

for i in delList:
    del an[i]
    
print("The new animals list of the zoo is:", an)

