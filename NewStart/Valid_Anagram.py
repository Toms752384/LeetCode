class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Docstring for isAnagram
        algorithm: first check lengths. then, add both to hash maps with {key=character : value=counter}
        :param self: Description
        :param s: Description
        :type s: str
        :param t: Description
        :type t: str
        :return: Description
        :rtype: bool
        """
        # check length
        n_s = len(s)
        n_t = len(t)
        if n_s != n_t:
            return False
        
        # create hash maps
        s_map = {}
        for i in range(n_s):
            if s[i] in s_map:
                s_map[s[i]] += 1
            else:
                s_map[s[i]] = 1
        
        t_map = {}
        for i in range(n_t):
            if t[i] in t_map:
                t_map[t[i]] += 1
            else:
                t_map[t[i]] = 1
        
        if s_map == t_map:
            return True

        return False