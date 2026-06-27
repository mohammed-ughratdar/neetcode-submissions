class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        for x in range(0, len(numbers)):
            to_find = target - numbers[x]
            for y in (range(x+1, len(numbers))):
                if numbers[y] == to_find:
                    return [x+1,y+1]
                elif numbers[y] > to_find:
                    break