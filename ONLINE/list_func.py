a=[0,1,2,3,4,5,6,7,8,9]
print(a[:5:2])
#a=['A',1,2.0,3,True]
print(max(a))
if 10 not in a:
    print(True)
else:
    print(False)
t=(1,2,3)
t=t*2
print(t*2)
for n in a[::-1]:
    print(n)
print(list(range(0,10)))
for i in range(0,10):
    print(i,end=',')
print("\n")
for i in range(0,11):
    if(i%2==0):
        print(i,end=' ')
    else:
        continue
n=int(input("Enter n value"))
s=0
for i in range(0,n):
    s+=i
print("sum value is %d"%s)
    
for i in range(11):
    if(i==2):
        print("Skipping")
        continue
    if(i==5):
        print("Breaking")
        break
    else:
        print(i)
print("Done")
