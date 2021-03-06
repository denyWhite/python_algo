# Реализация некоторых алгоритмов на графах


class Graph:
    def __init__(self, gr = {}):
        self._gr = gr

    def __str__(self):
        rtrn = ""
        for node in self._gr:
            rtrn += str(node) + " -> " + str(self._gr[node]) + "\n"
        return rtrn


g = Graph({
    1 : [2],
    2 : [1, 5],
    3: [4],
    4: [3, 5],
    5 : [2, 4],
})
print(g)

f = Graph()
print(f)