#write a to find prime no. and non prime no. from given list
my_list=[]
for j in range(1,11):
    n=int(input(f"enter number{j}:"))
    my_list.append(n)
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

