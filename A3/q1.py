node = []
edge = {} 

def InsertNode(id, name):
    for n in node:
        if n[0] == id:
            print("ID exists.")
            return
    node.append((id, name))
    edge[id] = set()

def InsertEdge(startId, endId):
    node_ids = [n[0] for n in node]
    if startId not in node_ids or endId not in node_ids:
        print("No such node.")
        return
    if endId in edge[startId] or startId in edge[endId]:
        print("Edge exists")
        return 
    edge[startId].add(endId)
    edge[endId].add(startId)

def CommonNeighbor(x, y):
    node_ids = [n[0] for n in node]
    if x not in node_ids or y not in node_ids:
        print("No such node.")
        return
    common = edge[x] & edge[y]
    if not common:
        print("No common neighbor.")
        return
    for c in sorted(common):
        for n in node:
            if n[0] == c:
                print(str(c) + n[1])

def ShortestPath(x, y):
    node_ids = [n[0] for n in node]
    if x not in node_ids or y not in node_ids:
        print("No such node.")
        return
    # initialization
    q = []
    visited = {}
    previous = {}
    q.append(x)
    for n in node_ids:
        visited[n] = False
    visited[x] = True

    # start search
    while q and not visited[y]:
        current = q.pop(0)
        for nei in edge[current]:
            if not visited[nei]:
                q.append(nei)
                visited[nei] = True
                previous[nei] = current

    # Print path
    if visited[y]:
        path = []
        current = y
        while current != x:
            path.append(current)
            current = previous[current]
        path.append(x)
        print(" -> ".join(str(n) for n in reversed(path)))
    else:
        print("No path exists.")

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

if __name__ == "__main__":
    main()


# Complete Test Sequence:

# InsertNode 1 Alice
# InsertNode 2 Bob
# InsertNode 3 Charlie
# InsertNode 4 David
# InsertEdge 1 2
# InsertEdge 2 3
# InsertEdge 3 4
# InsertEdge 1 4
# CommonNeighbor 1 3
# ShortestPath 1 4
# END