# LeetCode 1147
# Longest Chunked Palindrome Decomposition
# Greedy

class Solution:
    def longestDecomposition(self, text: str) -> int:
        print(text)
        i, j, pair = 0, len(text) - 1, 0
        while i < j:
            l, r = i, j
            while l < r:
                if text[i : l + 1] == text[r : j + 1]:
                    pair = pair + 2
                    break
                l, r = l + 1, r - 1
    
            i, j = l + 1, r - 1
        
        if i >= j and i != j + 1:
            pair = pair + 1
        return pair

    
if __name__ == '__main__':
    print(Solution().longestDecomposition('ghiabcdefhelloadamhelloabcdefghi'))
    print(Solution().longestDecomposition('merchant'))
    print(Solution().longestDecomposition('antaprezatepzapreanta'))
    print(Solution().longestDecomposition('abab'))
    print(Solution().longestDecomposition('aaa'))
    print(Solution().longestDecomposition("elvtoelvto"))
    print(Solution().longestDecomposition("bqrcnnqrcb"))