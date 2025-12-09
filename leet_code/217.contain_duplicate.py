# nums = [1,2,3,4]
# contain_duplicate = False
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j]:
#             contain_duplicate = True
#             print(contain_duplicate)
#             break

# if not contain_duplicate:
#     print(contain_duplicate)


nums = [1,2,3,4, 1]
nums.sort()

for i in range(1, len(nums)):
    if nums[i] == nums[i-1]:
        print(True)
        break
    
