import networkx as nx
from networkx.drawing.nx_agraph import to_agraph
from IPython.display import display
import graphviz

def draw_markov_chain(transition_matrix, states=None):
    D = None
    G = None
    
    # Define states:
    states = states if states else list(range(len(transition_matrix)))   

    # Create graph with Networkx
    G = nx.MultiDiGraph()
    
    # Add edges:
    for i, row in enumerate(transition_matrix):
        for j, weight in enumerate(row):
            G.add_edge(states[i], states[j], label=weight, weight=weight) if weight != 0 else None
    
    # Set edges properties:
    G.graph['edge'] = {'arrowsize': '0.6', 'splines': 'curved'}
    G.graph['graph'] = {'scale': '5'}

    # Drawing properties:
    D = nx.drawing.nx_agraph.to_agraph(G)
    D.node_attr.update(color='lightblue', style='filled')
    D.layout('dot')                                                                 

    # Display
    display(graphviz.Source(D))


if __name__ == "__main__":
    # States:
    states = ["sunny", "cloudy"]

    # Transition matrix:
    T = [[0.9, 0.1], 
         [0.2, 0.8]]

    draw_markov_chain(T, states)