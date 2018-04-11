# graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']["meta"] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']["meta"] = 5
graph["meta"] = {}

# cost table
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity

# parents table
parents = {}
parents['a'] = 'start'
parents['b'] = 'start'
parents["meta"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float('inf')
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
print node
while node is not None:
    cost = costs[node]
    print "cost:  " + str(cost)
    neighbors = graph[node]
    print neighbors
    for n in neighbors.keys():
        print n
        new_cost = cost + neighbors[n]
        print "new_cost:   " + str(new_cost)
        print  "costs[n]   "  + str(costs[n])
        if costs[n] > new_cost:
            print "Nowy koszt"
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)