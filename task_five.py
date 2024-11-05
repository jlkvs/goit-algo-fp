import uuid
import networkx as nx
import matplotlib.pyplot as plt
import colorsys
from collections import deque

class Node:
    def __init__(self, key, color="#0000FF"): 
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(arr):
    nodes = [Node(key) for key in arr]
    for i in range(len(arr)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(arr):
            nodes[i].left = nodes[left_index]
        if right_index < len(arr):
            nodes[i].right = nodes[right_index]
    return nodes[0] if nodes else None

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def generate_color(index, total_steps):
    hue = 210 / 360 
    saturation = 0.6
    lightness = 0.3 + (index / total_steps) * 0.5  
    r, g, b = colorsys.hls_to_rgb(hue, lightness, saturation)
    return f'#{int(r * 255):02x}{int(g * 255):02x}{int(b * 255):02x}'

def draw_tree(graph, pos, labels, colors):
    plt.figure(figsize=(8, 5))
    nx.draw(graph, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show(block=False)
    plt.pause(0.8) 

def bfs_visualize(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    
    queue = deque([root])
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}
    total_steps = len(tree.nodes())
    
    for step in range(total_steps):
        if not queue:
            break
        node = queue.popleft()
        node.color = generate_color(step, total_steps)  
        labels[node.id] = node.val
        colors = [data['color'] for _, data in tree.nodes(data=True)]
        
        draw_tree(tree, pos, labels, colors)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_visualize(root):
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    tree = add_edges(tree, root, pos)
    
    stack = [root]
    labels = {node: data['label'] for node, data in tree.nodes(data=True)}
    total_steps = len(tree.nodes())
    
    for step in range(total_steps):
        if not stack:
            break
        node = stack.pop()
        node.color = generate_color(step, total_steps)  
        labels[node.id] = node.val
        colors = [data['color'] for _, data in tree.nodes(data=True)]
        
        draw_tree(tree, pos, labels, colors)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

heap_array = [10, 5, 3, 2, 4, 1]

heap_tree_root = build_heap_tree(heap_array)


bfs_visualize(heap_tree_root)

dfs_visualize(heap_tree_root)
