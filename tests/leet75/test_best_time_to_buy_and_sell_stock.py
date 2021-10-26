from scripts.leet75.best_time_to_buy_and_sell_stock import Solution


class Test:
    test_cases = [
        [[7, 1, 5, 3, 6, 4], 5],
        [[7, 6, 4, 3, 1], 0]
    ]
    solution = Solution()

    def test_solution(self):
        for case, expected in self.test_cases:
            assert expected == self.solution.maxProfit(case)