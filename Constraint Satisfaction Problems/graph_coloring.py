colors = []
states = []
neighbors = {}
n=int(input("Enter the no. of colours: "))
print()
for i in range(n):
    color=input("Enter colour"+str(i+1)+": ")
    colors.append(color)

print()
print("The colours are: ",', '.join(colors))
print()
m=int(input("Enter the no. of states: "))
print()
for i in range(m):
    state=input("Enter state"+str(i+1)+": ")
    states.append(state)

print()
print("The states are: ",', '.join(states))
print()
print
for i in range(m):
    neighbors[states[i]]=input("Enter neighbors of "+str(states[i])+": ").split()


print()
colors_of_states = {}

def promising(state, color):
    for neighbor in neighbors.get(state): 
        color_of_neighbor = colors_of_states.get(neighbor)
        if color_of_neighbor == color:
            return False

    return True

def get_color_for_state(state):
    for color in colors:
        if promising(state, color):
            return color

def main():
    min_colours=[]
    for state in states:
        colors_of_states[state] = get_color_for_state(state)
        min_colours.append(get_color_for_state(state))

    min_colours=set(min_colours)    
    print(colors_of_states)
    print()
    print("Minimum no. of colours used:",len(min_colours))
    print()
    print("Colours used:",', '.join(min_colours))



if __name__ == '__main__':
    main()