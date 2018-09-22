class Solution(object):
    def strStr(self, haystack, needle):
        if not needle:
            return empty
        for i in range(0,len(haystack)-len(needle)-1):
            if haystack[i] == needle[0]:
                j=1
                while j<len(haystack) and  haystack[i+j]==needle[j]:
                    j=j+1
                return (i+1)
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if haystack[0] == needle[0]:
            return 0
        if len(haystack) < len(needle):
            return -1
        global i
        for i in xrange(0,len(haystack)-len(needle)):
            if haystack[i] == needle[0]:
                j=1
                while j<len(needle) and  haystack[i+j]==needle[j]:
                    j=j+1
                if j == len(needle):
                    return i
        return -1

