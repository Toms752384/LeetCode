class Solution():
    def gcd(self, a, b):
        """
        Calculates the Greatest Common Divisor (GCD) of two non-negative integers a and b
        using the Euclidean Algorithm.

        Args:
            a (int): The first non-negative integer.
            b (int): The second non-negative integer.

        Returns:
            int: The Greatest Common Divisor of a and b.
        """
        # Ensure a and b are non-negative
        a = abs(a)
        b = abs(b)

        # Base case: The GCD is b when a is 0
        while b:
            # The core of the Euclidean algorithm:
            # Replace a with b and b with the remainder of a divided by b (a % b)
            a, b = b, a % b
        
        # When b becomes 0, a holds the GCD
        return a

            

def main():
    sol = Solution()
    print(sol.gcd(10, 5))

if __name__ == "__main__":
    main()