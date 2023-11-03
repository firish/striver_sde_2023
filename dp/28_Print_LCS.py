# LCS, but, print the LCS


def lcs(s, t) :
	#Your code goes here
	dp = [[0 for _ in range(len(t)+1)] for _ in range(len(s)+1)]
	
	for ind1 in range(1, len(s)+1):
		for ind2 in range(1, len(t)+1):
			if s[ind1-1] == t[ind2-1]:
				dp[ind1][ind2] = 1 + dp[ind1-1][ind2-1]
			else:
				dp[ind1][ind2] = 0 + max(dp[ind1-1][ind2], dp[ind1][ind2-1])
	
	size = dp[len(s)][len(t)]
	ans = [0]*size
	ind1, ind2 = len(s), len(t)
	while ind1 > 0 and ind2 > 0:
		if s[ind1-1] == t[ind2-1]:
			ans[size-1] = s[ind1-1]
			ind1 -= 1
			ind2 -= 1
			size -= 1
		else:
			if dp[ind1][ind2-1] > dp[ind1-1][ind2]:
				ind2 -= 1
			else:
				ind1 -= 1
	return "".join(ans)
