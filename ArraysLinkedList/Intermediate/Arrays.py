import sys

main_list = [2, 1, 2, 2, 1, 4, 3, 3, 6, 8, 12, 8]

#functions
def RemoveRedundancy(list = []):
    if len(list) > 0:
        list.sort()
        new_list = []
        for item in list:
            if item not in new_list:
                new_list.append(item)
        return new_list
    else:
        return list
def GetConsecutives(para_list = []):
    if(len(para_list) > 0):
        new_list = []
        for i in range(len(para_list)):
            if(i < len(para_list) - 1):
                # find the difference and then add the consecutive nums
                curr_num = para_list[i]
                next_num = para_list[i + 1]
                difference = next_num - curr_num
                if(difference > 1):
                    new_list += list(range(curr_num + 1, next_num))
        return new_list
    else:
        return para_list
def GetMergedListofTwoLists(list1 = [], list2 = []):
    if len(list1) == 0 or len(list2) == 0:
        return []
    new_list = list1 + list2
    new_list.sort()
    return new_list
def Rotate(arr = [], k = 0):
    if len(arr) == 0:
        return []
    elif k == 0:
        print("Position k must not be 0")
    else:
        start_pos = (len(arr) - 1) - (k - 1)
        end_pos = len(arr)
        part_arr = arr[start_pos:]
        arr[start_pos: end_pos] = []
        arr = part_arr + arr
        return arr
def LargestSmallest(arr = []):
    if len(arr) == 0:
        return None
    elif len(arr) == 1:
        return {"small": arr[0], "large": arr[0]}
    else:
        small = arr[0]
        large = arr[0]
        for i in range(len(arr) - 1):
            if arr[i + 1] < small:
                small = arr[i + 1]
            if arr[i + 1] > large: 
                large = arr[i + 1]
        return {"small": small, "large": large}

#end functions

#Remove duplicates from an unsorted array.
redundant_list = RemoveRedundancy(main_list)
if len(redundant_list) == 0:
    print("Add data to List. Empty list is not allowed for further processing")
    sys.exit()    
print(redundant_list)

#Consecutive Arrays
consecutive_arrays = GetConsecutives(redundant_list)
if len(consecutive_arrays) == 0:
    print("Add data to List. Empty list is not allowed for further processing")
    sys.exit()    
print(consecutive_arrays)

#MergeList
merge_list = GetMergedListofTwoLists([2,4,1], [7,3,8,9])
if len(merge_list) == 0:
    print("Add data to List. Empty list is not allowed for further processing")
    sys.exit()    
print(merge_list)

# Rotate the array
new_arr = merge_list
new_arr = Rotate(new_arr, 3)
if new_arr is None:
    print("Please make sure to provide some number for position")
    sys.exit()
if len(new_arr) == 0:
    print("Array for the Rotation must not be empty")
    sys.exit()
print(new_arr)

# Find Small and Large in Array
small_large_obj = LargestSmallest(new_arr)
if(small_large_obj is None):
    print("To find the small or large number in array, it should not be empty")
    sys.exit()
print(type(small_large_obj))
print(small_large_obj)