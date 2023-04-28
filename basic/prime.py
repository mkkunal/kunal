#write a to find prime no. and non prime no. from given list
my_list=[13,25,37,16,256,26,4,76,8,9,5,43,45,678]
prime=[]
nonprime=[]

for num in my_list:
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
            break
    if flag==True:
        prime.append(num)
    else:
        nonprime.append(num)
print("prime no.",prime)
print("non prime no.--->>>>",nonprime)

