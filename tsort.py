'''
Chase M. Peak
-topological sort for graph data structure
'''
from stack import *
from sys import argv

def tsort(vertices):
    order = []
    tsorted = ""
    if not vertices or len(vertices) == 0: #this checks for empty inputs
        raise ValueError("input contains no edges")
    elif len(vertices) % 2 != 0: #this checks for odd inputs
        raise ValueError("input contains an odd number of tokens")
    vertices_dict = {} #keys are vertices, values are lists of the form [in-degree, (list of) adjacent vertices]
    tsort_build_dict(vertices_dict, vertices, order)
    stack = Stack(len(order)) #initialized to this size so that no IndexError occur from pushing items to stack
    for i in order: #this is the initial popping of vertices to the stack
        for j in vertices_dict[i][1]:
            if i in vertices_dict[j][1]:
                raise ValueError('input contains a cycle')
        if vertices_dict[i][0] == 0:
            stack.push(i)
    while not stack.is_empty():
        popped_vertex = stack.pop()
        tsorted += "{}\n" .format(popped_vertex)
        for j in vertices_dict[popped_vertex][1]: #this looks at each vertex in the adjacent verticies list
            vertices_dict[j][0] -= 1
            if vertices_dict[j][0] == 0:
                stack.push(j)
    return tsorted.strip()
    '''
    * Performs a topological sort of the specified directed acyclic graph.  The
    * graph is given as a list of vertices where each pair of vertices represents
    * an edge in the graph.  The resulting string return value will be formatted
    * identically to the Unix utility {@code tsort}.  That is, one vertex per
    * line in topologically sorted order.'''
    pass


def tsort_build_dict(vertices_dict, vertices, order):
    for i in range(0, len(vertices), 2):
        if not vertices[i] in vertices_dict: #this inserts the vertex into the dictionary initially
            order.append(vertices[i])
            vertices_dict[vertices[i]] = [0,[]]
        if not vertices[i + 1] in vertices_dict: #this inserts the second vertex into the dictionary if it isnt there already
            order.append(vertices[i + 1])
            vertices_dict[vertices[i + 1]] = [1, []]
        else: #if the second vertex is already in the dictionary, then it's in degree is incremented
            vertices_dict[vertices[i + 1]][0] += 1
        vertices_dict[vertices[i]][1].append(vertices[i + 1]) #this adds the second vertex to the adjacency list of the first vertex
    cyclic = True #this checks to see if the graph is cyclic after building the dictionary
    for i in vertices_dict: #this iterates through the dictionary to see if there are any cycles
        if vertices_dict[i][0] == 0:
            cyclic = False
    if cyclic:
        raise ValueError("input contains a cycle")
    return vertices_dict


def main():
    '''Entry point for the tsort utility allowing the user to specify
       a file containing the edge of the DAG'''
    if len(argv) != 2:
        print("Usage: python3 tsort.py <filename>")
        exit()
    try:
        f = open(argv[1], 'r')
    except FileNotFoundError as e:
        print(argv[1], 'could not be found or opened')
        exit()

    vertices = []
    for line in f:
        vertices += line.split()

    try:
        result = tsort(vertices)
        print(result)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()

