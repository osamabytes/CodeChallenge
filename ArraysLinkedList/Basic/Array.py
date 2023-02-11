# Step 1
try:
    inp = input("Enter Size of Array: ")
    n = int(inp)

    main_list = []

    for i in range(n):
        num_inp = input("Enter Number: ")
        num = int(num_inp)
        main_list.append(num)

    # Step 2
    print(main_list)

    # Step 3
    main_list.sort()
    min = main_list[0]
    max = main_list[len(main_list) - 1]
    print("Minimum: " + str(min))
    print("Maximum: " + str(max))

    # Step 4
    numSum = sum(main_list)
    print("Sum: " + str(numSum))

    # Step 5
    print("Average: " + str(numSum / len(main_list)))

    # Step 6
    search = input("Enter Search: ")
    search_num = int(search)
    if search_num in main_list:
        print("The value is found in " + str(main_list.index(search_num)))

    # Step 7
    search = input("Enter for Delete: ")
    search_num = int(search)
    if search_num in main_list:
        main_list.remove(search_num)
        print(main_list)
    else:
        print("Element not found for delete.")

    # Step 8
    position = input("Enter Position of index to add Value: ")
    value = input("Enter Value: ")

    pos = int(position)
    val = int(value)

    if(pos > 0 and pos <= len(main_list) - 1):
        temp = main_list[pos]
        main_list[pos] = val
        main_list.append(temp)
        print(main_list)

    # Step 9
    main_list.reverse()
    print(main_list)
except ValueError:
    print("Invalid input. Please Enter a valid number.")