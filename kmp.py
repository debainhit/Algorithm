class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if  needle== "" :
            return 0
        if haystack == "":
            return -1
        i = 0
        k = 0
        next = self.get_next(needle)
        while(i< len(haystack) and k< len(needle)):
            if  k == -1 or haystack[i] == needle[k]:
                i += 1
                k += 1
            else:
                k = next[k]
        if k == len(needle):
            return i-k
        else:
            return -1
    def get_next(self,p):
        k = -1
        i =0
        next = []
        next.append(-1)
        while(i<len(p)):
            if k == -1 or p[i]== p[k]:
                i += 1
                k += 1
                next.append(k)
            else:
                k = next[k]
        return next