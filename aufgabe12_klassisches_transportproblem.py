def print_matrix(M):
    for row in M:
        pr_row = []
        for elem in row:
            if elem is not None:
                pr_row.append(str(elem))
            else:
                pr_row.append('.')
        print('\t'.join(pr_row))


def make_matrix(rows, columns):
    return [[0 for x in range(columns)] for y in range(rows)]


def get_base_variables(M, non_base_variables=False):
    b = []
    for row in range(len(M)):
        for col in range(len(M[0])):
            if not non_base_variables:
                if M[row][col] is not None:
                    b.append((row, col))
            else:
                if M[row][col] is None:
                    b.append((row, col))

    return b


def make_human_friendly(l):
    return [(i+1, j+1) for i, j in l]


def solve_uv(M, C, first_value):
    B = get_base_variables(M)
    u = [None for _ in M]
    v = [None for _ in M[0]]

    i, _ = B[0]
    u[i] = first_value

    while None in u + v:
        for i, j in B:
            if u[i] is not None:
                v[j] = C[i][j] - u[i]
            if v[j] is not None:
                u[i] = C[i][j] - v[j]

    return (u, v)


def check_duality(M, C, first_value):
    u, v = solve_uv(M, C, first_value)
    print('u:', u)
    print('v:', v)
    N = get_base_variables(M, non_base_variables=True)

    problems = dict()

    for i, j in N:
        c_neg = C[i][j] - u[i] - v[j]
        print(f'c_{i+1}{j+1} = {C[i][j]} - {u[i]} - {v[j]} = {c_neg}')
        if c_neg < 0:
            problems[(i+1, j+1)] = c_neg

    return problems


def neighbours(M, point):
    X, Y = point
    n = set()

    row = M[X]
    for y, v in enumerate(row):
        if v is not None and y != Y:
            n.add((X, y))

    col = [M[i][Y] for i in range(len(M))]
    for x, v in enumerate(col):
        if v is not None and x != X:
            n.add((x, Y))

    return n


def calc_costs(M, C):
    c = 0
    for i, row in enumerate(M):
        for j, m in enumerate(row):
            if m is not None:
                c += m*C[i][j]

    return c


c = [
    [5, 4, 6],
    [3, 4, 2],
    [4, 3, 5],
    [4, 3, 4],
]


nwer = [
    [
        [6, None, None],
        [4, 3, None],
        [None, 5, 3],
        [None, None, 6],
    ],
    [
        [6, None, None],
        [4, 0, 3],
        [None, 8, None],
        [None, None, 6],
    ],
    [
        [6, None, None],
        [4, None, 3],
        [None, 8, None],
        [None, 0, 6],
    ],
    [
        [6, None, None],
        [None, None, 7],
        [None, 8, None],
        [4, 0, 2],
    ],
]

mk = [
    [
        [4, None, 2],
        [None, None, 7],
        [6, 2, None],
        [None, 6, None],
    ],
    [
        [6, None, None],
        [None, None, 7],
        [4, 4, None],
        [None, 4, 2],
    ],
]

nwer_test = [
    [
        [6, None, None],
        [4, None, 3],
        [None, 8, 0],
        [None, None, 6],
    ],
    [
        [6, None, None],
        [4, None, 3],
        [0, 8, None],
        [None, None, 6],
    ],
]
