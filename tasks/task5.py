import networkx as nx
import matplotlib.pyplot as plt
import uuid
from queue import Queue
from collections import deque

COLOR_INITIAL = 0xFF227730
COLOR_INDEX = 10000

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
	if node is not None:
		graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
	if node.left:
		graph.add_edge(node.id, node.left.id)
		left = x - 1 / 2 ** layer
		pos[node.left.id] = (left, y - 1)
		left = add_edges(graph, node.left, pos, x=left, y=y - 1, layer=layer + 1)
	if node.right:
		graph.add_edge(node.id, node.right.id)
		right = x + 1 / 2 ** layer
		pos[node.right.id] = (right, y - 1)
		right = add_edges(graph, node.right, pos, x=right, y=y - 1, layer=layer + 1)
	return graph

def draw_tree(tree_root):
	tree = nx.DiGraph()
	pos = {tree_root.id: (0, 0)}
	tree = add_edges(tree, tree_root, pos)

	colors = [node[1]['color'] for node in tree.nodes(data=True)]
	labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

	plt.figure(figsize=(8, 5))
	nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
	plt.show()

def prepare_graph(root):
    G = nx.DiGraph()
    def add_edges(node):
        if node:
            G.add_node(node.val)
            if node.left:
                G.add_edge(node.val, node.left.val)
                add_edges(node.left)
            if node.right:
                G.add_edge(node.val, node.right.val)
                add_edges(node.right)
    add_edges(root)
    return G

def bfs_visualization(graph, root_val, ax):
    color_map = []
    color_dict = {}
    queue = Queue()
    queue.put(root_val)
    
    index = 0
    while not queue.empty():
        node = queue.get()
        color = '#%06x' % (COLOR_INITIAL + index * COLOR_INDEX)
        color_dict[node] = color
        if node in graph:
            for neighbour in graph[node]:
                queue.put(neighbour)
        index += 1
    for node in graph:
        if node in color_dict:
            color_map.append(color_dict[node])
        else:
            color_map.append('#000000')
    nx.draw(graph, pos=nx.spring_layout(graph), node_color=color_map, with_labels=True, ax=ax)

def dfs_visualization(graph, root_val, ax):
    color_map = []
    color_dict = {}
    stack = deque([root_val])
    
    index = 0
    while stack:
        node = stack.pop()
        color = '#%06x' % (COLOR_INITIAL + index * COLOR_INDEX)
        color_dict[node] = color
        if node in graph:
            neighbors = list(graph[node])
            for neighbour in reversed(neighbors):
                stack.append(neighbour)
        index += 1
    for node in graph:
        if node in color_dict:
            color_map.append(color_dict[node])
        else:
            color_map.append('#000000')
    nx.draw(graph, pos=nx.spring_layout(graph), node_color=color_map, with_labels=True, ax=ax)
    

def insert_into_bst(root, key):
    if root is None:
        return Node(key)
    elif key < root.val:
        root.left = insert_into_bst(root.left, key)
    else:
        root.right = insert_into_bst(root.right, key)
    return root

def build_bst_from_heap(heap):
    if not heap:
        return None
    
    root = None
    for value in heap:
        root = insert_into_bst(root, value)
    return root

heap = [0, 4, 1, 5, 10, 3]
tree_from_heap = build_bst_from_heap(heap)
draw_tree(tree_from_heap)

G = prepare_graph(tree_from_heap)
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 6))
bfs_visualization(G, tree_from_heap.val, axes[0])
axes[0].set_title("BFS - Colors Gradation")

dfs_visualization(G, tree_from_heap.val, axes[1])
axes[1].set_title("DFS - Colors Gradation")

plt.show()
