def remove_adjacent(nums):

    n_ls = []

    for i in range(len(nums)):
        if not nums[i]==nums[i+1] or nums[i]==n_ls[-1:]:
            print (nums)
            print (i)
            #n_ls.append(nums[i])
    print (n_ls)
