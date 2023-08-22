from typing import List


class Solution:

    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum = [0] * (len(s) + 1)
        left_closet_candle = [-1] * (len(s) + 1)
        right_closet_candle = [-1] * (len(s) + 1)

        for index, el in enumerate(s):
            candle = 0
            left_candle_pos = left_closet_candle[index]
            if el == "|":
                candle = 1
                left_candle_pos = index
            prefix_sum[index + 1] = prefix_sum[index] + candle
            left_closet_candle[index + 1] = left_candle_pos

            reverted_index = len(s) - 1 - index
            right_closet_candle[reverted_index] = reverted_index if s[reverted_index] == "|" else right_closet_candle[
                reverted_index + 1]

        result = []
        for query in queries:
            left_index = right_closet_candle[query[0]]
            right_index = left_closet_candle[query[1] + 1]
            count = 0
            if left_index < right_index and left_index > -1 and right_index > -1:
                count = right_index - left_index - (prefix_sum[right_index + 1] - prefix_sum[left_index + 1])
            result.append(count)
        return result
