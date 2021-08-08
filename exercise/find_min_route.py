def find_min_route(s, e, arr):
    route = [[-1 for _ in lst] for lst in arr]
    route = bfs_util(s[0], s[1], route, arr)
    print(route)
    return route[e[0]][e[1]]


def bfs_util(i, j, route, arr):
    move = [[-1,0], [1,0], [0,-1], [0, 1]]
    queue = [[i,j]]
    route[i][j] = 0
    while queue:
        i, j = queue.pop(0)
        for x, y in move:
            cur_i, cur_j = i + x, j + y
            if not is_valid(cur_i, cur_j, arr):
                continue
            if route[cur_i][cur_j] != -1:
                continue
            route[cur_i][cur_j] = 1 + route[i][j]
            queue.append([cur_i, cur_j])
    return route


def is_valid(i, j, arr):
    if i < 0 or i >= len(arr):
        return False
    if j < 0 or j >= len(arr[0]):
        return False
    if arr[i][j] == 1:
        return False
    else:
        return True


def find_route_with_distance(s, e, arr, distance):
    route = [[-1 for _ in lst] for lst in arr]
    route[s[0]][s[1]] = distance
    return dfs_util(s, e, route, arr)


def dfs_util(s, e, route, arr):
    distance = route[s[0]][s[1]]
    if distance == 0:
        return s == e

    move = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    for x, y in move:
        new_i, new_j = s[0]+x, s[1]+y
        if not is_valid(new_i, new_j, arr):
            continue
        if route[new_i][new_j] != -1:
            continue
        route[new_i][new_j] = distance-1
        if dfs_util([new_i, new_j], e, route, arr):
            return True
        route[new_i][new_j] = -1
    return False





if __name__ == '__main__':
    mat = [
        [1, 1, 0, 0, 0, 0],
        [0, 1, 0, 1, 0, 0],
        [1, 0, 0, 1, 0, 0],
        [1, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 0],
    ]
    s = [3, 4]
    e = [0, 5]
    # min_route = find_min_route(s, e, mat)
    # print(min_route)
    print(find_route_with_distance(s,e,mat,6))
