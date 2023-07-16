class Solution:
    def longestValidSubstring(self, word: str, forbidden: List[str]) -> int:
        trie = Trie()
        for f in forbidden:
            trie.insert(f)

        n = len(word)
        dp = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            dp[i] = dp[i + 1] + 1
            if trie.search(word[i:i + dp[i]]):
                dp[i] = 0
                for j in range(i + 1, i + dp[i + 1] + 2):
                    if not trie.search(word[i:j]):
                        dp[i] = max(dp[i], j - i)
        return max(dp)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
            if node.is_end:
                return True
        return False
