''' save this as a script to run in the terminal '''
import sys, threading

sys.setrecursionlimit(3000000)
threading.stack_size(67108864)

def kosaraju(graph, loop_order={}):
    """
    Compute strongly connected components or SCCs in the graph.

    input:  a directed graph
    output: a tuple(ft, ld) where -:
            ft: a dictionary {each node: finish time}
            ld: a dictionary {each leader: list of children nodes}
    time:   O(m + n) linear time
    remark: in the 1st pass, compute finish times "ft" of each node of the reversed graph,
            in the 2nd pass, on the original graph, find SCCs by processing nodes in decreasing order of "ft".
            in fact, the finish times here very much resemble the topological order.
            in the 1st pass, we only care about the finish time "ft" to pass to the 2nd call,
            in the 2nd pass, we only care about the leaders "ld" to find SCCs.

    usage:  G_rev = reverse(G)
            ft, _ = kosaraju(G_rev)             # 1st pass
            _, ld = kosaraju(G, loop_order=ft)  # 2nd pass
    """
    # initialize
    explored = set()
    t = 0     # number of nodes processed so far, or finish time
    ft = {}   # track finish times for each node
    s = None  # source node or leader for the current DFS() invocation
    ld = {}   # track leader for each node, all nodes in a SCC must share the same leader

    # ----------------------------- tracing function -----------------------------
    def DFS(source):
        nonlocal explored, t, ft, s, ld

        explored.add(source)
        ld[s].append(source)

        # corner case: if "source" is a sink vertex (no outgoing arcs)
        if source not in graph.keys():
            pass
        else:
            for w in graph[source]:
                if w not in explored:
                    DFS(w)

        # when DFS() hits a sink or backtracks:
        t += 1          # the 1st sink node will be assigned "ft" = 1
        ft[source] = t  # then backtrack one node, "ft" = 2, and so forth...
    # ----------------------------- tracing function -----------------------------

    # 1st pass, loop from node n down to node 1
    if not loop_order:
        node_list = list(graph.keys())
        node_list.reverse()
    # 2nd pass, loop nodes in decreasing order of finish time
    else:
        node_list = [t[0] for t in sorted(loop_order.items(), key=lambda x: x[1], reverse=True)]

    # main loop
    for v in node_list:
        if v not in explored:
            s, ld[s] = v, []  # set "v" as a new leader
            DFS(v)  # start DFS search from "v"

    return (ft, ld)

def reverse_direction(graph):
    """ returns a new graph = the original directed graph with all arcs reversed """
    rev = {}
    for node, neighbors in graph.items():
        for nbr in neighbors:
            if nbr in rev.keys():
                rev[nbr].append(node)
            else:
                rev[nbr] = [node]
    return rev

def main():
    U, V = [], []
    with open("SCC.txt") as fh:
        for line in fh.readlines():
            U.append(int(line.split()[0]))
            V.append(int(line.split()[1]))

    G = {}
    for i in range(len(U)):
        if U[i] not in G.keys():
            G[U[i]] = [V[i]]
        else:
            G[U[i]].append(V[i])

    G_rev = reverse_direction(G)

    ft, _ = kosaraju(G_rev)
    _, ld = kosaraju(G, loop_order=ft)

    for leader, scc in ld.items():
        ld[leader] = len(scc)

    top_sccs = sorted(ld.items(), key=lambda x: x[1], reverse=True)

    print(top_sccs[:5])

if __name__ == "__main__":
    thread = threading.Thread(target=main)
    thread.start()
