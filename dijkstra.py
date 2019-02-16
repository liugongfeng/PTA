""" For example:
    edge = 12, and input s2 is :
    1 4 1
    1 5 1
    1 6 1
    4 8 1
    4 3 1
    3 5 1
    5 7 1
    3 7 1
    6 2 1
    7 2 1
    7 10 1
    2 9 1
the result:
graph = {1: {4: 1, 5: 1, 6: 1}, 4: {8: 1, 3: 1}, 3: {5: 1, 7: 1}, 5: {7: 1}, 6: {2: 1}, 7: {2: 1, 10: 1}, 2: {9: 1}}

costs = {4: 1, 5: 1, 6: 1, 8: inf, 3: inf, 7: inf, 2: inf, 10: inf, 9: inf}

parents = {4: 1, 5: 1, 6: 1, 8: None, 3: None, 7: None, 2: None, 10: None, 9: None}
    """
def initial(edges):
    for i in range(edges):
        s2 = input().split(" ")
        nums = [int(e) for e in s2]
        if nums[0] in graph.keys():
            graph[nums[0]][nums[1]] = nums[-1]
        else:
            graph[nums[0]] = {}
            graph[nums[0]][nums[1]] = nums[-1]
        if nums[0] == 1:
            costs[nums[1]] = nums[-1]
            parents[nums[1]] = 1
        elif nums[0] != 1 and nums[1] not in graph[1].keys():
            costs[nums[1]] = float('inf')
            parents[nums[1]] = None

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_node = node
    return lowest_node


if __name__ == "__main__":
    # s = input().split(" ")
    # vertices = int(s[0])    # 节点个数
    # edges = int(s[1])       # 边数
    # """ 1号节点为起点 """
    # graph = {}
    # costs = {}     # 起点到达其他节点的时间(or 权重), 不和起点直接接连的均设为无穷大'inf'
    # parents = {}   # 与起点直接相连的节点的父节点都为1号节点，否则均为None

    graph = {1: {4: 1, 5: 1, 6: 1}, 4: {8: 1, 3: 1}, 3: {5: 1, 7: 1}, 5: {7: 1}, 6: {2: 1}, 7: {2: 1, 10: 1}, 2: {9: 1}}

    costs = {4: 1, 5: 1, 6: 1, 8: 99, 3: 99, 7: 99, 2: 99, 10: 99, 9: 99}

    parents = {4: 1, 5: 1, 6: 1, 8: None, 3: None, 7: None, 2: None, 10: None, 9: None}

    processed = []
    # initial(edges)
    node = find_lowest_cost_node(costs)
    while node is not None:
        cost = costs[node]
        if not node in graph:
            graph[node] = {}
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
                parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs)


    # print(node)
    print(graph)
    print(costs)
    print(parents)

