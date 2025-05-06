from ast import List

def hasDuplicate(nums: List[int]) -> bool:
    """insert all elements into a set, and if finds an element already inside, return true. if finished, false"""
    # insert elements to a set while checking for dups
    my_set = set()
    for num in nums:
        if(num in my_set):
            return True
        my_set.add(num)
    return False