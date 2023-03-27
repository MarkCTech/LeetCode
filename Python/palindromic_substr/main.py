class Solution:
    def isPalindrome(self, s: str):

        if s == s[::-1]:
            return s
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r]
            if l >= 1 and s1 == s1[::-1]:
                size += 2
                start = l - 1
            elif s2 == s2[::-1]:
                size += 1
                start = l

        return s[start: start + size]

        # longest_palindrome = ""
        # headless_s = s
        # tailless_s = headless_s
        #
        #
        # while len(headless_s) > len(longest_palindrome):
        #
        #     if tailless_s != tailless_s[::-1]:
        #         tailless_s = tailless_s[:-1]
        #
        #     else:
        #         if len(tailless_s) > len(longest_palindrome):
        #             longest_palindrome = tailless_s
        #         tailless_s = headless_s = headless_s[1:]
        #
        # return longest_palindrome


def main():
    solver = Solution()
    testcases = ["eabcb", "abccbaabc"]
    for elem in testcases:

        print(solver.isPalindrome(elem))


if __name__ == "__main__":
    main()