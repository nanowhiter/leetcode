List = list


class Solution:
    """
    Given n non-negative integers representing an elevation map where the width of each bar is 1,
    compute how much water it can trap after raining.
    n == height.length
    1 <= n <= 2 * 104
    0 <= height[i] <= 105
    """

    def trap(self, height) -> int:
        ans = 0
        if len(height) <= 2:
            return ans
        top_list = [(idx, height[idx]) for idx in range(len(height))]
        last_len_top_list = -1
        while last_len_top_list != len(top_list):
            last_len_top_list = len(top_list)
            idx = 1
            while idx < len(top_list) - 1:
                if top_list[idx - 1][1] >= top_list[idx][1] and top_list[idx + 1][1] >= top_list[idx][1]:
                    del top_list[idx]
                    continue
                idx += 1
        for idx in range(len(top_list) - 1):
            ans += max(0, min(top_list[idx][1], top_list[idx + 1][1]) * (top_list[idx + 1][0] - top_list[idx][0] - 1))

        ans += sum([top[1] for top in top_list])
        ans -= sum(height)
        return ans


def main():
    sol = Solution()
    height = [4,2,0,3,2,5]
    print(sol.trap(height))


if __name__ == '__main__':
    main()
