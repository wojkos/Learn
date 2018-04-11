# graph
graph = {}
graph['start'] = {}
graph['start']['a'] = 6
graph['start']['b'] = 2
graph['a'] = {}
graph['a']['meta'] = 1
graph['b'] = {}
graph['b']['a'] = 3
graph['b']['meta'] = 5
graph['meta'] = {}

# cost table
infinity = float('inf')
costs = {}
costs['a'] = 6
costs['b'] = 2
costs['fin'] = infinity