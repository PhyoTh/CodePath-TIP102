from collections import deque


def bidirectional_flights(flights):
    for i in range(len(flights)):
        for neighbors in flights[i]:
            if (
                not i in flights[neighbors]
            ):  # if 0 is 1 neighbor, 1 should also be 0 neighbor
                return False
    return True


flights1 = [[1, 2], [0], [0, 3], [2]]
flights2 = [[1, 2], [], [0], [2]]

print(bidirectional_flights(flights1))
print(bidirectional_flights(flights2))


def find_center(terminals):
    edge1 = terminals[0]
    edge2 = terminals[1]
    return edge1[0] if edge1[0] in edge2 else edge1[1]


terminals1 = [[1, 2], [2, 3], [4, 2]]
terminals2 = [[1, 2], [5, 1], [1, 3], [1, 4]]

print(find_center(terminals1))
print(find_center(terminals2))


def get_all_destinations(flights, start):
    visited = set()
    que = [start]

    while que:
        des = que.pop()
        for neighbor in flights.get(des, []):
            if neighbor not in visited:
                visited.add(neighbor)
                que.append(neighbor)
    return list(visited)


flights = {
    "Tokyo": ["Sydney"],
    "Sydney": ["Tokyo", "Beijing"],
    "Beijing": ["Mexico City", "Helsinki"],
    "Helsinki": ["Cairo", "New York"],
    "Cairo": ["Helsinki", "Reykjavik"],
    "Reykjavik": ["Cairo", "New York"],
    "Mexico City": ["Sydney"],
}

print(get_all_destinations(flights, "Beijing"))
print(get_all_destinations(flights, "Helsinki"))
