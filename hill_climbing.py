class Tree:
 def __init__(self,node, child, non):
  self.node = []
  self.child = []
  self.heu = []
  self.cost = []
  self.non = non

 def addNode(self, node,child, heu, cost):
  self.node.append(node)
  self.heu.append(heu)
  temp = list(map(int, cost.split()))
  self.cost.append(temp)

  temp = list(map(str, child.split()))
  self.child.append(temp)

#global vars
visited = []
soln = []

def solnPath(goal, rg, final_cost, soln, found):
 if goal == source:
  soln.insert(0, rg)
  soln=list(reversed(soln))

  if found==True:
  	print("Solution Path: ",soln)
  	print("Path Cost: ",final_cost)
  	#print("Order of nodes explored: {}".format(visited))
  else:
  	print("Solution Path: ")
  print("Order of nodes explored: {}".format(visited))
  #print("Order of nodes explored: {}".format(visited))
  exit(0)
 
 for j in range(len(visited)):
 	if goal in t1.child[j] and visited[j] not in soln:
 		soln.append(visited[j])
 		ind1 = t1.child.index(t1.child[j])
 		ind2 = t1.child[j].index(goal)
 		final_cost = final_cost + t1.cost[ind1][ind2]
 		break
 return(solnPath(visited[j], rg, final_cost, soln, found))

  
def hillS(queue, goal, minheu, found, source):
 final_cost = 0           
 for i in range(len(t1.node)):

  if found == True:
   break
  else:
   current = queue.pop(0)
   if current not in visited:
   	visited.append(current)
   index = t1.node.index(current)
   if current == goal:
    found = True
    print("Solution found")
    final_cost = 0
    solnPath(goal, goal, final_cost, soln, found)
    break
   else:
    for x in t1.child[index]:
     temp_index = t1.node.index(x)
     temp_heu = t1.heu[temp_index]
    	
     print("Node {} has heuristic {}".format(x, temp_heu))
     if temp_heu < minheu:
      minheu = temp_heu
      val = x
     	
    queue.insert(0,val)
    print()
    print("Node {} has minimum heuristic of {} among these".format(val, minheu))
    #print("Appending node {} to the queue".format(val))
                # soln.append(val)
    print("Queue is: {}".format(queue))
    print()
 print("Solution not found. Stuck at node {}".format("".join(queue)))
 solnPath(queue[0], queue[0], final_cost, soln, found)
                    


n = int(input("Enter the no. of nodes: "))
print()
t1 = Tree(None, None, n)
for i in range(n):
    node = input("Enter node u"+str(i+1)+": ")
    heuristic = int(input("Enter heuristic for node u"+str(i+1)+": "))
    child = input("Enter children of node u"+str(i+1)+": ")
    cost = input("Enter path cost from node u"+str(i+1)+" to its respective children: ")
    print()
    t1.addNode(node, child, heuristic, cost)
source = input("Enter source node: ")
goal = input("enter goal node: ")
print()
queue = [source]
minheu = t1.heu[t1.node.index(source)]
found = False
# hillSolver(queue, goal, found, maxcost,soln)
hillS(queue, goal, minheu, found, source)
