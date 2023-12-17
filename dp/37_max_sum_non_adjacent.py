# Link: https://www.geeksforgeeks.org/problems/max-sum-without-adjacents2430/1

# Memo solution
def findMaxSum(self,arr, n):
		def rec(ind, dp):
		    if ind < 0:
		        return 0
		    if ind == 0:
		        return arr[ind]
		    
		    # memo check
		    if dp[ind] != -1:
		        return dp[ind]
		        
		    # op on ind
		    # take index or skip index
		    take = arr[ind] + rec(ind-2, dp) # can't take immidiate prev
		    skip = 0 + rec(ind-1, dp)
		    
		    # memo
		    dp[ind] = max(take, skip)
		    return max(take, skip)
	    
	    dp = [-1 for _ in range(n)]
	    return rec(n-1, dp)

# Space Optimized
# A bit tricky
def findMaxSum(self,arr, n):
      if n == 1: return arr[0]
      
      dp = [0] * n
      dp[0] = arr[0]
      dp[1] = max(arr[0], arr[1])
  
      for i in range(2, n):
          take = arr[i] + dp[i-2]
          skip = dp[i-1]
          dp[i] = max(take, skip)
  
      return dp[n-1]
