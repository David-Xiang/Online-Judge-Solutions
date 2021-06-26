# LeetCodeOffer 37 Hard
# Serialize and Deserialize Binary Tree
# Binary Tree

from typing import List

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    NULL = "null"

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return self.NULL
        return "(%s,%s,%s)" % (root.val, self.serialize(root.left), self.serialize(root.right))
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        node, pos = self.parse_help(data, 0)
        return node
        
    def parse_help(self, data, pos):
        if data[pos] == 'n':
            return (None, pos+len(self.NULL))
        pos = pos + 1 # read (    
        val, pos = self.read_int(data, pos)
        node = TreeNode(val)
        pos = pos + 1 # read ,
        node.left, pos = self.parse_help(data, pos)
        pos = pos + 1 # read ,
        node.right, pos = self.parse_help(data, pos)
        pos = pos + 1 # read )
        return node, pos

    def read_int(self, data, pos):
        val = 0
        is_positive = True
        if data[pos] == "-":
            is_positive = False
            pos = pos + 1
        while data[pos] in "0123456789":
            val = val * 10 + int(data[pos])
            pos = pos + 1

        return val if is_positive else -val, pos

if __name__ == "__main__":
    # node1 = TreeNode(1)
    # node2 = TreeNode(2)
    # node3 = TreeNode(3)
    # node4 = TreeNode(4)
    # node5 = TreeNode(5)
    # node1.left = node2
    # node1.right = node3
    # node3.left = node4
    # node3.right = node5
    node1 = TreeNode(-1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node1.left = node2
    node1.right = node3

    codec = Codec()
    serial_str = codec.serialize(node1)
    print(serial_str)
    root_new = codec.deserialize(serial_str)
    print(root_new.val)
    print(root_new.left.val)
    print(root_new.right.val)