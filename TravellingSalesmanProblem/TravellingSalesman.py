from itertools import permutations

def calculate_total_distance(path, distances):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distances[path[i]][path[i + 1]]
    return total_distance

def traveling_salesman_bruteforce(distances):
    num_cities = len(distances)
    cities = list(range(num_cities))
    shortest_path = None
    shortest_distance = float('inf')

    for path in permutations(cities):
        current_distance = calculate_total_distance(path, distances)
        if current_distance < shortest_distance:
            shortest_distance = current_distance
            shortest_path = path

    return shortest_path, shortest_distance

if __name__ == "__main__":
    # Example distances between cities (replace with your own data)
    distances = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    shortest_path, shortest_distance = traveling_salesman_bruteforce(distances)

    print("Shortest Path:", shortest_path)
    print("Shortest Distance:", shortest_distance)
