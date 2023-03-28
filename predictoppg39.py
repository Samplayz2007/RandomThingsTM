#question(a)
count=0
while count<10:
    print('Hello')
        count+=1
#output unexpected indentat error
#question(b)
x=10
y=0
while x,y:
    print(x,z)
    x=x-1
    y=y+1
#output
#10 0
#9 1
#8 2
#7 3
#6 4
#question(c)
keepgoing=True
x=100
while keepgoing:
    print(x)
    x=x-10
    if x < 50:
        keepgoing=False
#output
#100
#90
#80
#70
#60
#50
#question (d)
x=45
while x<50:
    print(x)
#output
#Infinite loop of 45s caused due to no updation of loop
#question (e)
for x in (1,2,3,4,5):
    print(x)
#output
#1
#2
#3
#4
#5
#questions (f)
for p in range(1,10):
    print(p)
#output
#1
#2
#3
#4
#5
#6
#7
#8
#9
#questions(g)
for z in range(-500,500,100):
    print(z)
#output
#-500
#-400
#-300
#-200
#-100
#0
#100
#200
#300
#400
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