ct = 1
while ct<=5: 
    print("Hello")
    ct+=1



nums = [1, 2, 4, 8, 12, 16, 20]
i = 0
while i <len(nums):
    print(nums[i])
    i+=1



# finding num 8
finding = 8
i = 0
while i<len(nums):
    if finding == nums[i]:
        print(f"number found on position: {i+1}")
        break
    i+=1




list = [1,2,3,4,5]
for i in range(len(list)): 
    print(list[i])

for i in list:
    print(i)