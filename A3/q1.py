node=[]
edge={}

def InsertNode(id, name):
    if id in node:
        print("ID exists.")
        return
    node.add((id, name))

def InsertEdge(startId, endId):
    if startId not in edge or endId not in edge:
        print("No such node.")
        return
    if endId in edge[startId] or startId in edge[endId]:
        print("Edge exists")
        return 
    edge[startId].add(endId)
    edge[endId].add(startId)

def CommonNeighbor(x, y):
    if x not in node or y not in node:
        print("No such node.")
        return
    common = list(edge[x] & edge[y]).sort()
    if not common:
        print("No common neighbor.")
        return
    for c in common:
        print(str(c) + node[c])

def ShortestPath(x, y):
    # initization
    q = []
    visited = {}
    previous = {}
    q.append(x)
    for x in node:
        visited[n] = False
    visited[x] = True

    # start search
    while (visited[y] == False or q):
        current = q.pop()
        for nei in edge[current]:
            if visited[nei] == False:
                q.append(nei)
                visited[nei] = True
                previous[nei] = current

    
def main():
    command=input().split()
    while(command[0]!="END"):      
        if (command[0]=="InsertNode"):
            InsertNode(int(command[1]),command[2])
        elif (command[0]=="InsertEdge"):
            InsertEdge(int(command[1]),int(command[2]))               
        elif (command[0]=="CommonNeighbor"):
            CommonNeighbor(int(command[1]),int(command[2]))
        elif (command[0]=="ShortestPath"):
            ShortestPath(int(command[1]),int(command[2]))
        command=input().split()
    return

main()
