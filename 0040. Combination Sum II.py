class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        :param candidates: a collection of candidate numbers.
        :param target: a target num.
        :return: all unique combinations in candidates where the candidate numbers sum to target.
        
        similar quesitons: 77, 216, 39 can be solved by backtrack, 377 can be solved by dp too.
        """
        candidates.sort()
        res = []

        def backtrack(remain_target: int, candidates: List[int], 
                      combination: List[List[int]], sum_: int) -> None:
                      
            for i in range(len(candidates)):
                if sum_ + candidates[i] == target:
                    res.append(combination + [candidates[i]])
                    return
                elif sum_  + candidates[i] > target:
                    return
                else:
                    # if candidates[i] == candidates[i - 1] we skip it to prevent duplicate combinations.
                    if i > 0 and candidates[i] == candidates[i - 1]:
                        continue
                    backtrack(target - candidates[i], candidates[i + 1 :], 
                              combination + [candidates[i]], sum_ + candidates[i])
        
        backtrack(target, candidates, [], 0)
        return res 
