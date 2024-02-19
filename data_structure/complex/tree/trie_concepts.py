"""
"""

"""
A trie, also known as a prefix tree, is a tree-like data structure used to efficiently store and retrieve a dynamic set of strings. Trie structures are particularly useful for tasks involving string manipulation and searching, such as autocomplete systems, spell checkers, and routing tables.

Structure of Tries:
A trie consists of nodes that represent characters in strings. Each node contains:

A reference to the parent node.
A collection of child nodes, typically represented using a dictionary or an array. This collection maps characters to child nodes.
A flag indicating whether the node represents the end of a valid word.
Operations:
Insertion: Inserting a new string into a trie involves traversing the tree, creating new nodes as necessary, and marking the end of the string by setting the corresponding flag.
Search: Searching for a string in a trie involves traversing the tree along the characters of the string. If the entire string is found and the node representing the last character has the end-of-word flag set, the string is present in the trie.
Deletion: Deleting a string from a trie involves removing nodes corresponding to the string's characters and updating the end-of-word flags.
Example:
Let's see a simple example of implementing a trie in Python:

"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.end_of_word


# Example usage:
trie = Trie()
words = ["apple", "app", "banana", "bat", "cat"]
for word in words:
    trie.insert(word)

print(trie.search("apple"))  # Output: True
print(trie.search("app"))  # Output: True
print(trie.search("banana"))  # Output: True
print(trie.search("bat"))  # Output: True
print(trie.search("cat"))  # Output: True
print(trie.search("ap"))  # Output: False
print(trie.search("b"))  # Output: False
