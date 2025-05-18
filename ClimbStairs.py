class Solution:
    # dynamic programming with extra space: init a list of elements sized n. res = num_options[n-1] + num_options[n-2], so we will fill an array
    # dynamic programming with O(1) space: init base1 and base2 to be 1's, and iterate the solution until n, while storing the second
    # base inside the first base after calculation is done
    def climbStairs(self, n: int) -> int:
        # cover base cases
        if n == 0 or n == 1:
            return 1
        
        # init base variables
        base1 = base2 = 1
        res = 0

        # compute value until n
        for _ in range(2, n + 1):
            res = base1 + base2
            base1 = base2
            base2 = res
        
        return res
        
        # # cover base cases
        # if n == 0 or n == 1:
        #     return 1
        
        # # init a array to store the number of options for each number of steps from 1 to n
        # num_of_options = [0] * (n + 1)

        # # populate the first two options with base cases
        # num_of_options[0] = 1
        # num_of_options[1] = 1

        # # populate the array
        # for i in range(2, n + 1):
        #     res = num_of_options[i - 1] + num_of_options[i - 2]
        #     num_of_options[i] = res

        # # return the n-th cell
        # return num_of_options[n]

def main():
    sol = Solution()
    stairs = 4
    print(sol.climbStairs(stairs))
    
if __name__ == "__main__":
    main()