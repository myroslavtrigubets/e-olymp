adj = [     # список смежности
    [1,3], # 0
    [0,3,4,5], # 1
    [4,5], # 2
    [0,1,5], # 3
    [1,2], # 4
    [1,2,3] # 5
]

level = [-1] * len(adj) # список уровней вершин

def bfs(s):
    level[s] = 0 # уровень начальной вершины
    stack = [s] # добавляем начальную вершину в очередь
    while stack: # пока там что-то есть
        v = stack.pop(0) # извлекаем вершину
        for w in adj[v]: # запускаем обход из вершины v
            if level[w] is -1: # проверка на посещенность
                stack.append(w) # добавление вершины в очередь
                level[w] = level[v] + 1 # подсчитываем уровень вершины

for i in range(len(adj)):
    if level[i] is -1:
        bfs(i) # на случай, если имеется несколько компонент связности

print(level[2]) # уровень вершины 2
