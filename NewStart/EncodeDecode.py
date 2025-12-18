from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        # create a string in this format (without spaces): len1#str1 len2#str2 len3#str3...
        res = []
        for s in strs:
            length = str(len(s))
            res.append(length)
            res.append("#")
            res.append(s)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # initalize result list
        # read input string - when encounters a number - refer to it as length of the string
        # read length until '#' and add all the characters using this length
        res = []
        n = len(s)
        i = 0
        while(i < n):
            # extract the string using partition
            parts = s[i:].partition('#')
            length = int(parts[0])
            result_string = parts[2][:length]
            res.append(result_string)

            # use the total length to advance i - counter
            total_len = len(parts[0]) + len(result_string) + 1 # for the '#' delimeter
            i += total_len
        
        return res
    
def main():
    sol = Solution()
    strs = ["neet","code","love","you"]
    res = (sol.encode(strs))
    print(sol.decode(res))
    # stam = "hello world"
    # print(stam[2 :])# llo world
    # print(stam[:5]) # hello

if __name__ == "__main__":
    main()