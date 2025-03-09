
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

#Check if there exist a triple with sum = target
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
