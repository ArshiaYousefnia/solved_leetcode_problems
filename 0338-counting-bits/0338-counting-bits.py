class Solution:
    def countBits(self, n: int) -> List[int]:
        a = [0]

        for i in range(1, n + 1):
            if i % 2 == 1:
                a.append(a[-1] + 1)
            else:
                a.append(a[i // 2])

        return a
