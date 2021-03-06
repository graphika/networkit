# extension imports
from .graph import Graph
from .dynamics import GraphEvent, DGSStreamParser, GraphUpdater, GraphDifference
from .distance import APSP

def graphFromStream(stream, weighted, directed):
	""" Convenience function for creating a new graph from a stream of graph events

	Parameters:
	-----------
	stream : list of GraphEvent
		event stream
	weighted : produce a weighted or unweighted graph
		boolean
	directed : produce a directed or undirected graph
		boolean
	"""
	G = Graph(0, weighted, directed)
	gu = GraphUpdater(G)
	gu.update(stream)
	return G
