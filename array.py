# 1. Given an array with some integer type values. Write a python script to sort array values?
n=int(input())
arr=list(map(int,input().split()))
arr.sort()
print(arr)

# 2. Given a list of heterogenous elements. Write a python script to remove all the non int values from the list.
l = input().split()
int_list = []
for i in l:
    try:
        num = int(i)
        int_list.append(num)
    except ValueError:
        pass
print(int_list)

# 3. Write a Python script to calculate average of elements of a list.
n=int(input())
arr=list(map(int,input().split()))
a=sum(arr)
print(a//n)
# 4. Write a Python script to create a list of first N prime numbers.
s=int(input())
e=int(input())
for i in range(s,e+1):
    if i>1:
        for j in range(2,int(i ** 0.5) + 1):
            if(i%j==0):
                break
        else:
            print(i,end=" ")
# 5. Write a Python script to create a list of first N terms of a Fibonacci series
n=int(input())
a=0
b=1
for i in range(n):
    print(a,end=" ")
    a,b=b,a+b
print()
