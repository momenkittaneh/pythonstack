#Biggie Size
def Biggie_size(num):
    for i in range(len(num)):
        if num[i]>0:
             num[i]="big"
    return (num)
  
x=[1,3,-1,7]
x= Biggie_size(x)
print(x)

#*****#
#Count Positives
def Count(x):
    counter=0
    for i in range (len(x)):
        if x[i]>0 :
            counter+=1
            x[-1]=counter
