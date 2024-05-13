import collections
import heapq
from typing import Dict, List, Set, Tuple


def dijkstra_shortest_path(edges: List[List[int]], source: int) -> Tuple[List[float], List[int]]:
    graph: Dict[int, List[Tuple[int, int]]] = collections.defaultdict(list)
    for node_a, node_b, dist in edges:
        graph[node_a].append((node_b, dist))
        graph[node_b].append((node_a, dist))

    # A min-heap keeping track of the closest unvisited node from the source node
    unvisited: List[Tuple[int, int]] = []
    # A set keeping track of the visited nodes
    visited: Set[int] = set()
    # An array keeping track of the distances between the source node and the rest of the nodes
    distances: List[float] = [float("inf") for i in range(len(graph))]
    # An array keeping track of the previous node that was traveled to reach this node
    previous: List[int] = [-1 for _ in range(len(graph))]

    # Set the distance of source node to itself to 0
    distances[source] = 0
    previous[source] = source

    # Push the (distance from source node, node) onto the heap. We use a heap so that we can greedily select the closest
    # unvisited node to explore next.
    # There is a slight difference from BFS. Here we do not add the node as marked or visited right when adding it to
    # the heap, because there may be a distinct shorter path available that has not yet been encountered to this node.
    heapq.heappush(unvisited, (0, source))

    while len(unvisited) > 0:
        dist, node = heapq.heappop(unvisited)
        # Add the node as a visited node after popping it from the heap.
        visited.add(node)
        # Explore the neighboring nodes from this node
        for node_b, dist_b in graph.get(node):
            if node_b in visited:
                continue

            total_distance = dist + dist_b
            # If the total distance to this node is less than what was previously recorded, then record this as the
            # shortest distance to this node
            if total_distance < distances[node_b]:
                distances[node_b] = total_distance
                previous[node_b] = node
                heapq.heappush(unvisited, (total_distance, node_b))

    return distances, previous


if __name__ == "__main__":
    # Each edge is bi-directional and edge[i][0] and edge[i][1] are two nodes that have an edge between them with a cost
    # of edge[i][2] to travel
    edges = [[0, 1, 2], [0, 2, 6], [1, 3, 5], [2, 3, 8], [3, 4, 10], [3, 5, 15], [4, 5, 6], [4, 6, 2], [5, 6, 6]]
    print(dijkstra_shortest_path(edges, 0))
    print("test")

















