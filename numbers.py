class Numbers:
#This function finds the max in an array of numbers by traversing through using
#a for loop
    def findMax(nums):
        for x in nums:
            temp = 0
            if x > temp:
                temp = x
        return temp

#Find the minimum number in an array
    def findMin(nums):
        for x in nums:
            temp2 = 999999
            if x < temp2:
                temp2 = x
        return temp2
    
#Find the mean of an array
    def findMean(nums):
        temp3 = 0
        for x in nums:
            temp3 += x
        return temp3/(len(nums))

#Testing whether the function work on not by printing out the results of
#each function
nums = [1,2,3,4,5,6,7,8]
nums2 = [10,20,30,40,50,1]
nums3 = [10,10,10,10,10,10]

print("The max of this array is: ",Numbers.findMax(nums))
print("The min of is array is: ",Numbers.findMin(nums2))
print("The mean of is array is: ",Numbers.findMean(nums3))

