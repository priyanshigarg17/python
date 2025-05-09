nums=[1, 2, 3, 4, 5, 6, 7]
k=3 #given position to jump over
k=k%len(nums) # to check number of rotations
myarr=[0]*len(nums) #duplicate array of nums with 0 on every index

for i in range(0, len(nums)):
    myarr[(i+k)%len(nums)]=nums[i]

nums[:]=myarr
print(nums)