
#question (h)
x=10
y=5
for i in range(x-y*2):
    print("%",i)
#output is well nothing bcz 10 - 5*2 where 5*2 is 10 so 10-10 0 and the code is not run :)
#question (i)
c=0
for x in range(10):
    for y in range(5):
        c+=1
print(c)
#output
#50
#question(j)
x=[1,2,3]
counter=0
while counter < len(x):
    print(x[counter]*'%')
    for y in x:
        print(y*'*')
    counter+=1
#output
#%
#*
#**
#***
#%%
#*
#**
#***
#%%%
#*
#**
#***
#question(k)
for x in 'lamp':
    print(str.upper(x))
#output
#L
#A
#M
#P
x='one'
y='two'
counter=0
while counter < len(x):
    print(x[counter],y[counter])
    counter+=1
#output
#o t
#n w
#e o
x='apple,pear,peach'
y=x.split(',')
for z in y:
    print(z)
#output
#apple
#pear
#peach
x='apple,pear,peach,grapefruit'
y=x.split(',')
for z in y:
    if z < 'm':
        print(str.lower(z))
    else:
        print(str.upper(z))
#output
#apple
#PEAR
#PEACH
#grapefruit