from p1_support import load_level, show_level
from math import sqrt
from heapq import heappush, heappop


def dijkstras_shortest_path(src, dst, graph, adj):
    queue = []

    dst[src] = 0
    prev = {}
    prev[src] = None

    for v in graph:
        if v != src:
            dst[v] = float('inf')
            prev[v] = None
        queue.append(v)

    while queue:
        u = dst[src]
        node_to_be_removed = src
        for node in queue:
            if dst[node] < u:
                u = dst[node]
                node_to_be_removed = node


    #queue = [src]

    #while queue:
        #node = queue.pop()

        #if node == dst:
            #break

        #neighbors = adj(graph, node)
        #for next_node in neighbors:
            #if next_node not in prev:
                #prev[next_node] = node
                #queue.append(next_node)

    #if node == dst:
        #path = []
        #while node:
            #path.append(node)
            #node = prev[node]
        #path.reverse()
        #return path
    #else:
        #return []



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

