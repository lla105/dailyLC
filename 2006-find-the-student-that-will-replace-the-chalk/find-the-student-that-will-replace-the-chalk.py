class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        remainchalk = k%sum(chalk)

        for i in range(len(chalk)):
            remainchalk -= chalk[i]
            if remainchalk<0:
                return i