from typing import List
def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    def helper(i,k,sumTillNow,n):
        if k == 0:
            if sumTillNow == n:
                ans.append(subset.copy())
            return
        if sumTillNow > n:
            return
        if i == 10:
            return
        sumTillNow += i
        subset.append(i)
        helper(i+1,k-1,sumTillNow,n)
        subset.pop()
        sumTillNow -= i
        helper(i+1,k,sumTillNow,n)
    subset = []
    
    ans = []
    helper(1,k,0,n)
    return ans
    