#powered by xin 62160246

#import tools#
import networkx as tools
import matplotlib.pyplot as plot

#ex 1 colum 1#

g00 = tools.Graph()
g00.add_nodes_from(['a','b','c','d'])
g00.add_edges_from([('a','b'),('b','c'),('b','d'),('d','c')])
print(g00.degree())

tools.draw(g00, with_labels=True)
plot.show()

# #ex 1 colum 2#
g01 = tools.Graph()
g01.add_nodes_from(['a','b','c','d','e','f'])
g01.add_edges_from([('a','b'),('a','d'),('a','e'),('b','c'),('c','e'),('d','e'),('e','f'),('c','f')])
print(g01.degree())

tools.draw(g01, with_labels=True)
plot.show()

#ex 1 colum 2#
g02 = tools.Graph()
g02.add_nodes_from(['a','b','c','d','e'])
g02.add_edges_from([('a','b'),('a','e'),('b','e'),('b','c'),('e','d'),('c','d'),('a','b')])
print(g02.degree())

tools.draw(g02, with_labels=True)
plot.show()


aj00 = tools.DiGraph()
aj00.add_nodes_from(['a','b','c','d','e','f'])
aj00.add_edges_from([('a','b'),('b','c'),('c','d'),('d','e'),('e','f'),('f','a'),('f','b'),('c','e')])

#error error error error error error error error error error error error error error error error error error error error #
# data_aj00 = aj00.adjacency_list()
# loop_adj = 0
#
# for loop00 in aj00:
#     print(loop00, ':',data_aj00[loop_adj])
#     loop00 += 1
#error error error error error error error error error error error error error error error error error error error error #

#ex 2 choice 2 show in degree & out degree by aj00#
print('Degree IN : ',aj00.in_degree())
print('Degree OUT : ',aj00.out_degree())

sum_dgin = 0
sum_dgout = 0

for loop01 in aj00:
    sum_dgin += aj00.in_degree(loop01)
    sum_dgout += aj00.out_degree(loop01)

print('Sun Degree IN : ',sum_dgin)
print('Sum Degree OUT : ',sum_dgout)
print('Edges : ',sum_dgout)  # cause >> sum_dgout


tools.draw(aj00, with_labels=True)
plot.show()  # show answer ( ex 2 choice 1 & ex2 choice 2 )

#ex 3 adjacency matrix#
ajm00 = tools.Graph()
ajm00.add_nodes_from(['a','b','c','d','e','f','g','h'])
ajm00.add_edges_from([('a','b'),('a','c'),('a','d'),('b','e'),('c','e'),('d','f'),('e','h'),('e','g'),('f','g')])

ajm_matx_func = tools.adjacency_matrix(ajm00)
loop_ajm = 0

#create colum#
print('     ',end=' ')
for loop02 in ajm00:
    print(loop02, end=' ')

# create row & value #
print()
for loop03 in ajm00:
    print(loop03, ajm_matx_func[loop_ajm].todense())
    loop_ajm += 1

tools.draw(ajm00, with_labels=True)
plot.show()

#ex 4#

g_0 = tools.Graph()
g_0.add_nodes_from(['a','b','c','d','e'])
g_0.add_edges_from([('a','b'),('a','e'),('e','d'),('d','c'),('c','b')])
print(g_0.degree())
tools.draw(g_0, with_labels=True)
plot.show()

g_1 = tools.complete_graph(['a','b','c','d','e','f'])
print(g_1.degree())
tools.draw(g_1, with_labels=True)
plot.show()

g_2 = tools.complete_bipartite_graph(('a','b','c','d'),('e','f','g'))
print(g_2.degree())
tools.draw(g_2, with_labels=True)
plot.show()

