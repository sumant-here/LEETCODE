# from collections import deque
# class Solution:
#     def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
#         wordset = set(wordList)
#         if endWord not in  wordset:
#             return []
#         result = []
#         queue = deque()
#         queue.append([beginWord])
#         while len(queue) != 0:
#             level_size = len(queue)
#             chosen_words = set()
#             for _ in range(level_size):
#                 sequence = queue.popleft()
#                 last_word = sequence[-1]
#                 if last_word == endWord:
#                     result.append(sequence)
#                     continue
#                 for i in range(len(last_word)):
#                     for ch in "abcdefghijklmnopqrstuvwxyz" :
#                         if ch == last_word[i]:
#                             continue
#                         new_word = last_word[:i] + ch + last_word[i+1:]
#                         if new_word in wordset:
#                             new_seq = sequence + [new_word]
#                             queue.append(new_seq)
#                             chosen_words.add(new_word)
#             for word in chosen_words:
#                 wordset.remove(word)
#         return result


from collections import deque
from typing import List

class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        wordSet = set(wordList)

        if endWord not in wordSet:
            return []

        # BFS queue
        queue = deque([beginWord])

        # parent[word] = words that can come before this word
        parent = {beginWord: []}

        # Used to stop after finding the shortest level
        found = False

        while queue and not found:

            level_size = len(queue)
            level_used = set()

            for _ in range(level_size):

                word = queue.popleft()

                for i in range(len(word)):

                    for ch in "abcdefghijklmnopqrstuvwxyz":

                        if ch == word[i]:
                            continue

                        new_word = word[:i] + ch + word[i+1:]

                        if new_word not in wordSet:
                            continue

                        # First time seeing this word
                        if new_word not in parent:

                            parent[new_word] = [word]
                            queue.append(new_word)
                            level_used.add(new_word)

                        # Another shortest path to the same word
                        elif new_word in level_used:

                            parent[new_word].append(word)

                        if new_word == endWord:
                            found = True

            # Remove words only after completing the whole level
            for word in level_used:
                wordSet.remove(word)

        if endWord not in parent:
            return []

        # Build answers using DFS
        result = []
        path = [endWord]

        def dfs(word):

            if word == beginWord:
                result.append(path[::-1])
                return

            for p in parent[word]:
                path.append(p)
                dfs(p)
                path.pop()

        dfs(endWord)

        return result