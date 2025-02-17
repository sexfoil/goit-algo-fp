import uuid

import networkx as nx
import matplotlib.pyplot as plt


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


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree(root)


""" Побудова дерева на основі купи """
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


# Бінарна купа в форматі списку
heap1 = [0, 4, 1, 5, 10, 3]
heap2 = [10, 21, 13, 5, 7, 15, 17, 1, 9]

# Побудова дерева з купи
tree_from_heap1 = build_bst_from_heap(heap1)
tree_from_heap2 = build_bst_from_heap(heap2)

# Візуалізація побудованого дерева
draw_tree(tree_from_heap1)
draw_tree(tree_from_heap2)