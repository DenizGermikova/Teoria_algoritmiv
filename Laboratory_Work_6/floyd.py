INF = float('inf')

# Ребра графа (неорієнтований)
edges = [
    (1,3,6),
    (3,8,7),
    (3,2,1),
    (2,6,2),
    (8,6,3),
    (8,7,4),
    (7,5,5),
    (5,4,9),
    (2,4,3),
    (1,6,8),
    (2,7,4),
    (1,4,7)
]

n = 8  # кількість вершин

# Створюємо початкову матрицю ваг W = D(0)
W = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(1, n+1):
    W[i][i] = 0

for u, v, w in edges:
    W[u][v] = min(W[u][v], w)
    W[v][u] = min(W[v][u], w)   # неорієнтований граф

print("Початкова матриця W = D(0):")
for i in range(1, n+1):
    print([("∞" if W[i][j] == INF else int(W[i][j])) for j in range(1, n+1)])
print()

# Реалізація Floyd–Warshall
D = [row[:] for row in W]   # копія W

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if D[i][k] + D[k][j] < D[i][j]:
                D[i][j] = D[i][k] + D[k][j]

# Фінальний результат
print("Фінальна матриця відстаней D (результат Флойда):")
for i in range(1, n+1):
    print([("∞" if D[i][j] == INF else int(D[i][j])) for j in range(1, n+1)])
