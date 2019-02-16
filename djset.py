
def find(x, parent):
	x_root = x;
	while (parent[x_root] != -1):
		x_root = parent[x_root]

	return x_root


""" Retuns 1, Union succuessfully ; Returns 0, Union failed
"""
def union(x, y, parent, rank):
	x_root = find(x, parent)
	y_root = find(y, parent)
	if (x_root == y_root):
		return 0
	else:
		# parent[x_root] = y_root
		# Weighted Quick Union
		if (rank[x_root] > rank[y_root]):
			parent[y] = x_root
		elif (rank[y_root] > rank[x_root]):
			parent[x] = y_root
		else:
			parent[x_root] = y_root
			rank[y_root] += 1
		return 1

if __name__ == "__main__" :
	Vertices = 6
	parent = [-1] * Vertices
	rank = [0] * Vertices
	edges = [ [0,1], [1,2], [1,3], [5,4], [3,4], [2,5] ]

	for i in range(len(edges)):
		x = edges[i][0]
		y = edges[i][1]
		if (union(x, y, parent, rank) == 0):
			print("Cycle detected.")
			exit(0)
	print("No Cycles.")