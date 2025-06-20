class Solution:
    def isHappy(self, n: int) -> bool:
        # initialize variables
        res = 0
        results = set()
        temp = n

        # iterate through n's digits and sum its digits, and add results to set
        while(True):
            while(temp != 0): # compute the sum of squares
                remiander = (temp % 10)
                res += pow(remiander, 2)
                temp = int(temp / 10)
            if res in results: # if found a cycle
                return False
            if res == 1: # if non cyclic
                return True
            # add result so set and start again for the result
            results.add(res) 
            temp = res
            res = 0

        