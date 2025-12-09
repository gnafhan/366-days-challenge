# nums = [1,2,3,1,2,3]
# k = 1
# contain_duplicate = False
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] == nums[j] and abs(i-j) <= k:
#             contain_duplicate = True
#             print(contain_duplicate)
#             break

# if not contain_duplicate:
#     print(contain_duplicate)

# nums = [1,0,1,1]
# k = 1
# saved = {}

# for i in range(len(nums)):
#     # print(nums[i], saved)
#     if nums[i] not in saved.keys():
#         saved[nums[i]] = i
#     else:
#         # print(f"i: {i}, saved: {saved[nums[i]]}")
#         if abs(i - saved[nums[i]]) <= k:
#             print(True)
#         else:
#             saved[nums[i]] = i


nums = [1,0,1,1]
k = 1
saved = {}
nums_cpy = nums.copy()

nums_cpy.sort()
print(nums)

print(list(enumerate(nums)))

