# LeetCode 127
# Word Ladder
# BFS

from typing import List
import collections
import sys

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_len = len(beginWord)
        wordList.append(beginWord)
        start = len(wordList) - 1
        if endWord not in wordList:
            return 0
        else:
            end = wordList.index(endWord)
        
        adj = [[] for i in range(len(wordList))]
        vt_keys = dict()
        for i in range(len(wordList)): # 这段预处理非常重要，直接对比两个单词会超时
            for j in range(word_len):
                word = wordList[i]
                vkey = word[:j] + "-" + word[j+1:]
                if vkey not in vt_keys:
                    vt_keys[vkey] = [i]
                else:
                    vt_keys[vkey].append(i)
        for i in range(len(wordList)):
            for j in range(word_len):
                word = wordList[i]
                vkey = word[:j] + "-" + word[j+1:]
                if vkey not in vt_keys:
                    vt_keys[vkey] = [i]
                else:
                    vt_keys[vkey].append(i)
                adj[i].extend(set([k for k in vt_keys[vkey] if k != i]))
        
        q1 = collections.deque()
        q2 = collections.deque()
        q1.append(start)
        q2.append(end)
        ans = 2
        s1 = set()
        s1.add(start)
        s2 = set()
        s2.add(end)
        while len(q1) > 0 and len(q2) > 0 and ans <= len(wordList):
            if len(q1) > len(q2):
                q1, q2 = q2, q1
                s1, s2 = s2, s1
            l = len(q1)
            for i in range(l):
                v = q1.popleft()
                for nv in adj[v]:
                    if nv in s2:
                        return ans
                    if nv not in s1:
                        q1.append(nv)
                        s1.add(nv)
            ans = ans + 1
        return 0
        

if __name__ == "__main__":
    print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))
    print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))