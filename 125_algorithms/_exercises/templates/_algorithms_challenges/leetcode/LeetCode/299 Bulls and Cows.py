from collections ______ defaultdict

__author__ = 'Daniel'


class Solution(object
    ___ getHint(self, secret, guess
        """
        Need to revert B

        Example:
        1121
        2323

        :type secret: str
        :type guess: str
        :rtype: str
        """
        cnt = defaultdict(int)
        A = 0
        B = 0
        for c in secret:
            cnt[c] += 1

        for i, v in enumerate(guess
            __ v __ secret[i]:
                A += 1
                __ cnt[v] > 0:
                    cnt[v] -= 1
                ____
                    B -= 1

            ____ cnt[v] > 0:
                B += 1
                cnt[v] -= 1

        r_ "%dA%dB" % (A, B)


__ __name__ __ "__main__":
    assert Solution().getHint("0", "1") __ "0A0B"
