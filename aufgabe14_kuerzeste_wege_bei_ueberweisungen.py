import networkx as nx
from pprint import pprint


def restwert(anfang, *prozentwerte):
    if len(prozentwerte) == 1:
        p = prozentwerte[0]
        return round(anfang - anfang*p/100, 3)
    else:
        return restwert(
            restwert(anfang, prozentwerte[0]),
            *prozentwerte[1:]
        )


def verlust(anfang, prozentwert):
    return round(anfang - restwert(anfang, prozentwert), 3)


def restwert_verlust(anfang, prozentwert):
    return (restwert(anfang, prozentwert), verlust(anfang, prozentwert))


def product(l):
    r = 1
    for e in l:
        r = round(r*e, 3)
    return r


def gewicht_der_letzten_kante(*prozentwerte):
    if len(prozentwerte) == 1:
        p = prozentwerte[0]
        return round(p/100, 3)
    else:
        r = [round(1-p/100, 3) for p in prozentwerte]
        return round(product(r[:-1]) - product(r), 3)


G = nx.DiGraph()
G.add_nodes_from(['Rostock'] + [c for c in 'abcdef'] + ['Bangkok'])
G.add_weighted_edges_from(
    [
        ('Rostock', 'a', 0.03),
        ('Rostock', 'b', 0.08),
        ('Rostock', 'c', 0.01),
        ('a', 'e', 0.03),
        ('b', 'd', 0.06),
        ('b', 'f', 0.04),
        ('c', 'e', 0.05),
        ('d', 'Bangkok', 0.02),
        ('e', 'b', 0.02),
        ('e', 'Bangkok', 0.1),
        ('f', 'Bangkok', 0.04),
    ]
)

print('Unbearbeiteter Graph:')
print('kürz. Pfad:', nx.shortest_path(G, 'Rostock', 'Bangkok'))
print(
    'alle kürz. Pfade:',
    list(nx.all_shortest_paths(G, 'Rostock', 'Bangkok'))
)
print(
    'kürz. Dijkstra-Pfad:',
    nx.dijkstra_path(G, 'Rostock', 'Bangkok'),
    nx.dijkstra_path_length(G, 'Rostock', 'Bangkok'),
)

print(
    'kürz. Dijkstra-Pfad zu allen Knoten:',
)
pprint(
    nx.single_source_dijkstra_path(G, 'Rostock')
)
pprint(
    nx.single_source_dijkstra_path_length(G, 'Rostock')
)

H = nx.DiGraph()
H.add_nodes_from(['Rostock'] + [c for c in 'abcdef'] + ['Bangkok'])
H.add_weighted_edges_from(
    [
        ('Rostock', 'a', 3),
        ('Rostock', 'b', 8),
        ('Rostock', 'c', 1),
        ('a', 'e', 2.9),
        ('b', 'd', 5.5),
        ('b', 'f', 3.7),
        ('c', 'e', 4.9),
        ('d', 'Bangkok', 1.7),
        ('e', 'b', 1.9),
        ('e', 'Bangkok', 9.4),
        ('f', 'Bangkok', 3.5),
    ]
)
print('Bearbeiteter Graph:')
print('kürz. Pfad:', nx.shortest_path(H, 'Rostock', 'Bangkok'))
print(
    'alle kürz. Pfade:',
    list(nx.all_shortest_paths(H, 'Rostock', 'Bangkok'))
)
print(
    'kürz. Dijkstra-Pfad:',
    nx.dijkstra_path(H, 'Rostock', 'Bangkok'),
    nx.dijkstra_path_length(H, 'Rostock', 'Bangkok'),
)

print(
    'kürz. Dijkstra-Pfad zu allen Knoten:',
)
pprint(
    nx.single_source_dijkstra_path(H, 'Rostock')
)
pprint(
    nx.single_source_dijkstra_path_length(H, 'Rostock')
)
