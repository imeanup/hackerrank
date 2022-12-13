class ManacherAlgorithm:

    def longestPalindrome(self, s:str) -> str:
        T = '#'.join('^{}$'.format(s))
        