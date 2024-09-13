def split_and_sort(nums):
    # check input list length, change limit capacity to handle up to 30 elements
    if len(nums) > 30:
        print("Error: Input list should contain less number integers.") # Use print method to print error instead of return
        return 
    
    # check if 0 is in the input list
    # if 0 in nums:
    #     print("Error: The number 0 is not a valid input.")            # Use print method to print error instead of return
    #     return
    # We assume 0 to be negative for this assignment. Hence no longer need this

    # filter numbers into two separate lists
    pos_nums = {num for num in nums if num > 0}  # Adapt change using {} bracket instead of [] to ensure duplicated numbers are sorted
    neg_nums = {num for num in nums if num <= 0} # zero treated as negative component

    # sort
    neg_nums = sorted(neg_nums)
    pos_nums = sorted(pos_nums)
    print("Positive numbers:", pos_nums)
    print("Negative numbers:", neg_nums)

    return neg_nums, pos_nums

