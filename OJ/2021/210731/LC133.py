# LeetCode 133
# Clone Graph
# BFS/DFS

from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = dict()
        return self.clone(node, visited)
        
    def clone(self, node, visited):
        if node is None:
            return None
        if node in visited:
            return visited[node]
        node_clone = Node(val=node.val)
        node_clone.neighbors = []
        visited[node] = node_clone
        for neighbor in node.neighbors:
            node_clone.neighbors.append(self.clone(neighbor, visited))
        return node_clone

if __name__ == "__main__":
    nodes = [Node(val=i) for i in range(5)]
    nodes[1].neighbors = [nodes[2], nodes[4]]
    nodes[2].neighbors = [nodes[1], nodes[3]]
    nodes[3].neighbors = [nodes[2], nodes[4]]
    nodes[4].neighbors = [nodes[1], nodes[3]]
    cloned_node1 = Solution().cloneGraph(nodes[1])
    print(id(nodes[1]))
    print(id(cloned_node1))
    print(cloned_node1.val)