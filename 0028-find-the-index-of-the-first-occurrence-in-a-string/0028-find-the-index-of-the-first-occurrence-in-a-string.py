
class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            for i in range(len(haystack) - len(needle) + 1):
                if haystack[i:i + len(needle)] == needle:
                    return i
        return -1

        