from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop


def dijkstras_shortest_path(src, dst, graph, adj):
  
    prev = {}
    dist = {}
    queue = []
    dist[src] = 0
    # explore starting at the source node
    
    #discovered[source] = True
    heappush(queue, (dist[src],src))
    
    iterations = 0
    
    while queue:
        
       # iterations += 1
        
        u,u2 = heappop(queue)
        
        if u2 == dst: # early termination
            break
        neighbors = adj(graph,u2)
        for v in neighbors:
            dx = (abs(u2[0]-v[0]))
            dy = (abs(u2[1]-v[1]))
            rDis = sqrt(dx*dx + dy*dy)
            alt = u + rDis
            if v not in dist or alt < dist[v]:
               # discovered[v] = True
                #parent[v] = u
                dist[v] = alt
                prev[v] = u2
                heappush(queue, (dist[v],v))
    
    if u2 == dst:
        path = []
        node = dst
        while node in prev:
            path.append(node)
            node = prev[node]
        path.append(src)
        path.reverse()
        return path
    else:
        return []



def navigation_edges(level, cell):
    steps = []
    x, y = cell
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            next_cell = (x + dx, y + dy)
            dist = sqrt(dx * dx + dy * dy)
            if dist > 0 and next_cell in level['spaces']:
                steps.append(next_cell)
    return steps


def test_route(filename, src_waypoint, dst_waypoint):
    level = load_level(filename)

    show_level(level)

    src = level['waypoints'][src_waypoint]
    dst = level['waypoints'][dst_waypoint]

    path = dijkstras_shortest_path(src, dst, level, navigation_edges)

    if path:
        show_level(level, path)
    else:
        print "No path possible!"


if __name__ == '__main__':
    import sys

    _, filename, src_waypoint, dst_waypoint = sys.argv
    test_route(filename, src_waypoint, dst_waypoint)


