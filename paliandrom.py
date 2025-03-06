
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
