import os
import pickle
from graphviz import Digraph

def make_graph():
    # Get the base directory
    file_path = os.path.dirname(os.path.realpath(__file__))
    base_path = os.path.dirname( os.path.dirname( os.path.dirname( file_path ) ) )

    # Read the data required to make the graph
    graph_file = os.path.join( base_path, "MDI_Mechanic", ".temp", "graph.pickle")
    with open(graph_file, 'rb') as handle:
        data = pickle.load(handle)
    nodes = data['nodes']
    edges = data['edges']

    dot = Digraph(comment='Node Report', format='svg')

    for node in nodes.keys():
        dot.node( node, nodes[ node ], shape='box' )

    for edge in edges:
        dot.edge( edge[0], edge[1] )

    graph_path = os.path.join( base_path, "report", "graphs", "node-report.gv" )
    dot.render( graph_path )

if __name__ == "__main__":
    make_graph()
