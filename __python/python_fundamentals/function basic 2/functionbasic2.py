#countdown goes here 

def countdown(num):
    list=[]
    for i in range(num,-1,-1):
        list.append(i)
    return list

print(countdown(10))

#*****#

#printAndreturni

def printAndreturn(num):
    print(num[0])
    return (num[1])
x=printAndreturn([2,3])
print (x)

#*****#

#First Plus Length 

def firstpluslength(num):
    sum=num[0]+len(num)
    return (sum)

#*****#

#values greater than second

def greaterthansecond(list):
    new_list=[]
    y=list[1]
    counter=0
    if len(list)<2:
        return False
    for i in range (len(list)):
        if y< list[i]:
            new_list.append(list[i])
            counter+=1
    print (counter)
    return new_list 
x=[3,4,5,6]
y=greaterthansecond(x)

print (y)
#*****#
#This Length,That Value 

def length(size,value):
    list=[]
    for i in range (size):
        list.append(value)
    return list
print(length(6,9))

#*****#











