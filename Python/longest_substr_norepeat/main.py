class Solution:

    def lengthoflongestsubstring(self, s: str) -> str:
        longestword = ""
        seenchars = []
        currentword = ""
        seenwords = []
        start = 0

        for count, char in enumerate(s):

            while char in seenchars:
                seenwords.append(currentword)
                if len(currentword) > len(longestword):
                    longestword = currentword
                seenchars.remove(s[start])
                start += 1
                currentword = currentword[1::]

            while char not in currentword:
                currentword += char
            seenchars.append(char)

            # max_len = max()
            if len(currentword) > len(longestword):
                longestword = currentword
        return longestword


def main():
    tests = ["abcabcbb", "bbbbb", "pwwkelmw", "au", "dvdf", "tmmzuxt"]

    for elem in tests:
        tester = Solution()
        longestword = tester.lengthoflongestsubstring(elem)

        print("\nThe size of the longest substring within the input string is: ", longestword)
        print("And the word is: ", longestword)


if __name__ == '__main__':
    main()
