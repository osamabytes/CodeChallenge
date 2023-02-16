import sys

main_list = [2, 1, 2, 2, 1, 4, 3, 3, 6, 8, 10, 8]

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
#end functions

#Remove duplicates from an unsorted array.
main_list = RemoveRedundancy(main_list)
if len(main_list) == 0:
    print("Add data to List. Empty list is not allowed for further processing")
    sys.exit()    