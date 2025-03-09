
arr=["a","b","c","b","a"]
n=len(arr)
nums=[]
for i in range(n):
    nums.append(arr[n - i - 1])
if arr == nums:
    print("True")
else:
    print("False")

arr=["a","b","c","b","a"]
n=len(arr)
for i in range(n//2):
    if arr[i]!=arr[n-i-1]:
        print("false")
print("true")

#paliandrom using two pointers
arr=["a","b","a"]
n=len(arr)
i=0
j=n-1
while i<=j:
    if arr[i]!=arr[j]:
        print("false")
        break
    i+=1
    j-=1

#Check if there exist a triple with sum = target \\first
arr=[1,2,3,4,5,6,7]
i=0
j=1
k=2
target=10
for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        for k in range(j+1,len(arr)):
            x=arr[i]
            y=arr[j]
            z=arr[k]
            if x+y+z==target:
                print(arr[i],arr[j],arr[k])

#Check if there exist a triple with sum = target \\second
arr=[1,2,3,4,5,6,7]
target=10
b=0
set = set()
for i in range(0,len(arr)-2):
    for j in range(i+1,len(arr)):
        b=target-arr[i]-arr[j]
        if b in set and b>1 and b!=arr[i] and b!=arr[j]:
            print(arr[i],arr[j],b)
        else:
            set.add(arr[j])

#Check if there exist a triple with sum = target \\3rd
arr=[1,2,3,4,5,6,7]
target=10
s=0
for i in range(0,len(arr)-2):
    left=i+1
    right=len(arr)-1
    s = arr[i]+arr[left]+arr[right]
    if s==target:
        print(True)
    elif s < target:
        left+=1
    else:
        right-=1
