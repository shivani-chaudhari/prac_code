
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}

#DFS

visited=set()

def dfs(visited,graph,node):
    if node not in visited:
        print(node)
        visited.add(node)
    for neighbour in graph[node]:
        dfs(visited,graph,neighbour) 

print("Depth First Search:")
dfs(visited,graph,'5')           

visit=[]
queue=[]

def bfs(visit,graph,node):
    visit.append(node)
    queue.append(node)

    while queue:
        m=queue.pop(0)
        print(m)
        for neighbours in graph[m]:
            if neighbours not in visit:
                visit.append(neighbours)
                queue.append(neighbours)

print("Breadth First Search:")
bfs(visit,graph,'5')                