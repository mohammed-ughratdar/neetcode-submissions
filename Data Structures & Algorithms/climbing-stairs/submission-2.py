class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        def recurseSteps(current_step, final_step):

            if current_step == final_step:
                return 1

            if current_step > final_step:
                return 0

            if current_step in memo:
                return memo[current_step]

            count_1_steps = recurseSteps(current_step+1, final_step)
            count_2_steps = recurseSteps(current_step+2, final_step)
            memo[current_step] = count_1_steps+count_2_steps
            return memo[current_step]

        return recurseSteps(0, n)
