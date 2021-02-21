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


#visit all nodes of the tree

def bfs(tree, start):
	#keep track of all visited nodes
	visited=[]
	#keep track of nodes to be checked
	queue=[start]

	#keep looping until there are nodes still to be visited
	while queue:
		node=queue.pop(0) #pop shallowest node
		if node not in visited:
			#add node to list of checked nodes
			visited.append(node)
			neighbours = tree[node]

			#add neighbours of node to queue
			for neighbor in neighbours:
				queue.append(neighbor)
	return visited
print("Goal node reached.",'\n')
print("Order of nodes visited: "+str(bfs(tree,start_node)),'\n')


#find the path
def bfs_shortest_path(tree, start, goal):
	#keep track of visited nodes
	visited=[]
	#keep track of all the paths to be checked
	queue=[start]

	#return path if start is goal
	if start==goal:
		return "Goal reached."

	#keep looping until all possible paths are found
	while queue:
		#pop the first path from queue
		path = queue.pop(0)
		#get the last node from path
		node=path[-1]
		if node not in visited:
			neighbours=tree[node]
			#go thru all the neighbour nodes
			#push it into the queue
			for neighbor in neighbours:
				new_path = list(path)
				new_path.append(neighbor)
				queue.append(new_path)
				#return path if neighbour is goal
				if neighbor==goal:
					path_cost=len(new_path)-1
					return new_path, path_cost

			#mark node as visited
			visited.append(node)

	return "No path between start and goal node."

solution_path, path_cost = (bfs_shortest_path(tree,start_node, goal_node))
print("Solution Path: "+str(solution_path),'\n')
print("Path Cost: ", path_cost)