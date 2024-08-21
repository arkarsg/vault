For complete notes, refer to [Dynamic Programming](School/Y3S1/CS3230/Notes/Dynamic%20Programming.md)

# Edit distance
Given two words $w_1$ and $w_2$, find the minimum number of operations required to convert the word $w_1$ to $w_2$

There are 3 permitted operations:
1. Insert a character
2. Delete a character
3. Replace a character

We want to convert the words with *the least cost possible*

## Example

```
s1    r a d
s2    a p p l e
```

![edit-distance-example|300](https://labuladong.gitbook.io/~gitbook/image?url=https%3A%2F%2F2525270655-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-legacy-files%2Fo%2Fassets%252F-M1hB-LnPpOmZGsmxY7T%252Fsync%252F1912ddf88b038ff8d0097dbb3f584989f4f2019d.gif%3Fgeneration%3D1609991747720508%26alt%3Dmedia&width=300&dpr=4&quality=100&sign=d301c0df&sv=1)

- When the 2 characters are the same, there should be **no operation** to minimize the distance.
- When $w_i$ is finished but $w_j$ has yet to finish, then you can only delete the character in $w_j$ to make them the same
- When $i$ finished $w_1$ and $j$ has not finished $w_2$, you can only insert remaining characters of $w_2$ into $w_1$

## Optimal substructure

Define $OPT(i, j)$ to be the minimum cost of aligning strings $x_1, x_2, … , x_i$ and $y_1, y_2, …, y_j$

Then,
```python
OPT(i, j)
	j if i == 0
	i if j == 0
	OPT(i-1, j-1) if s1[i] == s2[j]

	otherwise:
		min(
			OPT(i, j-1) + 1, # insert
			OPT(i-1, j) + 1, # delete
			OPT(i-1, j-1) + 1 # replace
		)
```

```python
OPT(i-1, j-1) if s1[i] == s2[j]
```
In other words, if $s_1[i] = s_2[j]$, the least editing distance must equal the lease editing distance of $s_1[i-1] = s_2[j-1]$

## Memo
Add a memo to store the results of the optimal substructures

## DP table
- Create a 2D DP table such that `dp[i][j]` stores the least edit distance of `s1[0...i]` and `s2[0...j]`

![dp-table|500](image.jpeg)

---

# Solution
```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0 for i in range(m+1)] for j in range(n+1)]
        '''
        initialize base case
        - if one of the word is at index -1 or an empty string,
            simply "insert" all the characters from the other string
        '''
        for i in range(1, m+1):
            dp[0][i] = i
        for j in range(1, n+1):
            dp[j][0] = j

		'''
		Build DP table from bottom up
		'''
        for i in range(1, n+1):
            for j in range(1, m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(
                        dp[i][j-1] + 1,
                        dp[i-1][j] + 1,
                        dp[i-1][j-1] + 1
                    )
        return dp[n][m]
    
word1 = "horse"
word2 = "ros"

print(Solution().minDistance(word1, word2))
```