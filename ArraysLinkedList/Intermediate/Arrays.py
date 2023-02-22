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