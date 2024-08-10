---
title: Finding out if graph is bipartite
---

We want to split a group of `n` people (labeled from `1` to `n`) into two groups of **any size**. Each person may dislike some other people, and they should not go into the same group.

Given the integer `n` and the array `dislikes` where `dislikes[i] = [ai, bi]` indicates that the person labeled `ai`does not like the person labeled `bi`, return `true` _if it is possible to split everyone into two groups in this way_.

---

Essentially, this question is asking us if a graph as given by a list of edges (`dislikes`) is [bipartite](Graph.md#Bipartiteness).

To check if a graph is bipartite, we can do *red-blue* coloring (or any other colors). 
1. Pick any node $v$. Assign $v$ as *red* without loss of generality
2. Assign all its neighbours *blue*

Repeat this process for the nodes in the graph. If a node is already colored and has the same color as its neighbour, then the graph is not bipartite.

Another way to find out if a graph is bipartite is to find out if the graph has an odd-length cycle.

---

From our understanding, a pseudocode will be:

```plaintext
class Solution:
	def possibleBipartition(self, n, dislikes):
		adjList = make_adj_list(dislikes)

		queue = []
		
		for each node in the graph
		   if node is not colored:
			   color the node RED
			   append node to the queue

				while there are nodes in the queue
					get curr_color and curr_color of node
					pop the node

					for each neighbouring node of curr_node:
						if curr_color == neighbouring node_color:
							return False
						else:
							assign neighbouring node as the opposite color
						append neighbouring node to the queue
		return True
```

**Points to be careful about**
- A person is labelled `1` to `n` (1-based indexing)
- The relationship between the two nodes are not directional

---
```python
class Solution:
	def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
		RED = 0
		BLUE = 1
		
		person_dislike_hm = defaultdict(lambda: [])
		
		for person, dislike in dislikes:
			person_dislike_hm[person].append(dislike)
			person_dislike_hm[dislike].append(person)
		
		color = defaultdict(lambda: -1)
		queue = []
		
		for i in range(1, n+1):
			if color[i] == -1:
				color[i] = RED
				queue.append([i, RED])
			
				while len(queue) != 0:
					node, curr_color = queue[0]
					queue.pop(0)
					
					for neighbour in person_dislike_hm[node]:
						if color[neighbour] == curr_color:
							return False
						if color[neighbour] == -1:
							if curr_color == RED:
								color[neighbour] = BLUE
							else:
								color[neighbour] = RED
						queue.append([neighbour, color[neighbour]])
					
	return True
```