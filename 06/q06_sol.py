import networkx as nx

with open("q06_inp.txt") as fp:
    graph = nx.DiGraph()
    for i in fp.readlines():
        graph.add_edge(*[j.strip() for j in i.split(")")])
    print("Part A:", nx.transitive_closure(graph).size())
    graph_modified = graph.to_undirected()
    print("Part B:", nx.shortest_path_length(graph_modified, "YOU", "SAN") - 2)