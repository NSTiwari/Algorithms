tree={}  # declare an empty dictionary for tree
n=int(input("Enter the no. of nodes in tree: "))
print()
for i in range(n):
	keys=input("Enter node"+str(i+1)+": ")
	values=list(map(str,input("Enter neighbours of node"+str(i+1)+": ").split()))
	print()
	tree[keys]=values

print()
start_node = input("Enter the start node: ")
goal_node = input("Enter the goal node: ")

def dfs(tree, node, visited):
	if node not in visited:
		visited.append(node)
		for n in tree[node]:
			dfs(tree,n,visited)
	return visited
visited = dfs(tree,start_node,[])
print()
print("Order of nodes visited: "+str(visited),'\n')


def dfs_shortest_path(tree, start, goal):
	#keep track of visited nodes
	visited=[]
	#keep track of all the paths to be checked
	stack=[start]

	#return path if start is goal
	if start==goal:
		return "Goal reached."

	#keep looping until all possible paths are found
	while stack:
		#pop the first path from queue
		path = stack.pop(-1)
		#get the last node from path
		node=path[-1]
		if node not in visited:
			neighbours=tree[node]
			#go thru all the neighbour nodes
			#push it into the queue
			for neighbor in neighbours:
				new_path = list(path)
				new_path.append(neighbor)
				stack.append(new_path)
				#return path if neighbour is goal
				if neighbor==goal:
					path_cost=len(new_path)-1
					return new_path, path_cost

			#mark node as visited
			visited.append(node)

	return "No path between start and goal node."

solution_path, path_cost = (dfs_shortest_path(tree,start_node, goal_node))
print("Solution Path: "+str(solution_path),'\n')
print("Path Cost: ", path_cost)