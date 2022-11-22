nums = [2,3,4,5,6];

x = len(nums)
print("Len = ", x);

# add array elements
nums.append(10);

for num in nums:
    print(num);
    
# remove element: array.pop(index)
nums.pop(2)

print("After pop");
for num in nums:
    print(num);