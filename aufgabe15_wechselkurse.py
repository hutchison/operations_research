import networkx as nx
from math import log10
from operator import itemgetter


def weight_of_path(G, path):
    w = 0.0

    for x, y in zip(path[:-1], path[1:]):
        w += G[x][y]['weight']

    w += G[path[-1]][path[0]]['weight']

    return w


def cycles_and_weights(G):
    cycles = []

    for path in nx.simple_cycles(R):
        cycles.append((path, weight_of_path(R, path)))

    cycles = sorted(cycles, key=itemgetter(1))
    return cycles


R = nx.DiGraph()
R.add_nodes_from(['EUR', 'USD', 'RUB', 'JPY', 'GBP', 'CHF'])
R.add_weighted_edges_from(
    [
        ('EUR', 'USD', -log10(1.1546)),
        ('EUR', 'RUB', -log10(73.5960)),
        ('EUR', 'JPY', -log10(127.6220)),
        ('EUR', 'GBP', -log10(0.8734)),
        ('EUR', 'CHF', -log10(1.1496)),
        ('USD', 'EUR', -log10(0.8661)),
        ('USD', 'RUB', -log10(63.7773)),
        ('USD', 'JPY', -log10(110.5340)),
        ('USD', 'GBP', -log10(0.7565)),
        ('USD', 'CHF', -log10(0.9954)),
        ('RUB', 'EUR', -log10(0.0135)),
        ('RUB', 'USD', -log10(0.0156)),
        ('RUB', 'JPY', -log10(1.7334)),
        ('RUB', 'GBP', -log10(0.0118)),
        ('RUB', 'CHF', -log10(0.0156)),
        ('JPY', 'EUR', -log10(0.0078)),
        ('JPY', 'USD', -log10(0.0090)),
        ('JPY', 'RUB', -log10(0.5769)),
        ('JPY', 'GBP', -log10(0.0068)),
        ('JPY', 'CHF', -log10(0.0090)),
        ('GBP', 'EUR', -log10(1.1448)),
        ('GBP', 'USD', -log10(1.3219)),
        ('GBP', 'RUB', -log10(84.2200)),
        ('GBP', 'JPY', -log10(146.1130)),
        ('GBP', 'CHF', -log10(1.3162)),
        ('CHF', 'EUR', -log10(0.8692)),
        ('CHF', 'USD', -log10(1.0042)),
        ('CHF', 'RUB', -log10(63.9690)),
        ('CHF', 'JPY', -log10(111.0060)),
        ('CHF', 'GBP', -log10(0.7592))
    ]
)


for path, w in cycles_and_weights(R):
    print(path, 10**(-w))
