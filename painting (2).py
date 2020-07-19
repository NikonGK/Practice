import itertools

import time
# Раскраска графа, переборный алгоритм

start_all=time.time()

# Задаем граф как список смежности
# Для этого используем словарь
G = {}

# Задаем количество вершин
graph_length = int(input('Введите количество вершин:'))
assert (graph_length >= 1)  # Проверка, что количество вершин больше или равно 1

for i in range(graph_length):
    #Добавляем в словарь
    G[i + 1] = [int(x) for x in input('Введите смежные вершны для '+str(i+1)+"(через пробел!):").split()]

# Создаем список цветов и добавляем первый цвет
colors = [1]


# Функция, которая проверяет корректность раскраски
# Принимает комбинацию раскраски вершин
def checkPainting(comb):
    for vertex in G.keys():
        for pair in G.get(vertex):
            # Если смежные вершины имееют один цвет,
            # то закончить проверку, так как такая раскраска не подходит
            if comb[pair - 1] == comb[vertex - 1]:
                return False
    # Проверки пройдены, а значит раскраска верна
    return True


# Худший случай - graph_length цветов, где graph_length - Размер графа,
# Поэтому если количество красок равно graph_length, то оптимальной раскраски
# не существует
while len(colors) < graph_length:
    # Получаем всевозможные комбинации раскрасок размера graph_length
    # и используя цвета из colors
    for comb in itertools.product(colors, repeat=graph_length):
        # проверяем комбинацию
        if (checkPainting(comb)):
            # Если комбинация прошла проверки, то она является оптимальной
            print(comb, 'количество цветов:', len(colors))
            end_all=time.time()
            print('время работы программы:' , end_all-start_all)
            exit()
    # Если не смогли раскрасить, то добавляем новый цвет и проверяем новые комбинации
    # для этого в конец добавляем цвет на 1 больше предыдущего
    colors.append(len(colors) + 1)

# Если не смогли оптимально раскрасить, то количество цветов равно graph_length
print("Невозможно покрасить оптимально, нужно цветов:", graph_length)
end_all=time.time()
print('время работы программы:' , end_all-start_all)

