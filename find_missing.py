from collections import deque

class TrieNode:
    def __init__(self, character):
        self.c = character
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode('') 

    def addWord(self, word):
        root = self.root
        for i in word:
            if i not in root.children:
                root.children[i] = TrieNode(i)
            root = root.children[i]
        root.isWord = True

class Solution:
    def find_min(self, word):
        trie = Trie()
        for i in range(len(word)):
            trie.addWord(word[i:])
        
        all_words = ["a", "b", "c", "d", "e", "f"]
        q = deque([(trie.root, "")])  
        
        while q:
            node, string = q.popleft()
            for c in all_words:
                if c not in node.children:
                    print(string + c)
                    return string + c
                else:
                    q.append((node.children[c], string + c)) 

        return ""

def main():
    solution = Solution()  
    result = solution.find_min("acbdef") 
    print(result)  

if __name__ == "__main__":  
    main()
