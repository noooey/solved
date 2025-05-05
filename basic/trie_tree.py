class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

def autocomplete(trie, prefix):
    node = trie.root
    for char in prefix:
        if char not in node.children:
            return []
        node = node.children[char]

    result = []
    def dfs(node, word):
        if node.is_end:
            result.append(word)
        for char in node.children:
            dfs(node.children[char], word + char)

    dfs(node, prefix)
    return result

#
if __name__ == "__main__":
    trie = Trie()
#     trie.insert("apple")
#     trie.insert("app")
#     print(trie.search("apple"))
#     print(trie.search("app"))
#     print(trie.search("appl"))
#     print(trie.starts_with("ap"))
#     print(trie.starts_with("ban"))
    trie.insert("banana")
    trie.insert("band")
    trie.insert("bandit")
    trie.insert("banner")
    print(autocomplete(trie, "ban"))
