from Bellman.BellmanFord import BellmanFordMeasure
from Dijkstra.Dijkstra import DijkstraMeasure

def saveTimesWithName(times, name): # Лучше бы БД делала
    toSave = " "
    for time in times:
        toSave += f"{time} "
    file = open(f"{name}.txt", 'a')
    file.write(toSave)
    file.close()

def collectDataDijkstraA():
    dijkstra = DijkstraMeasure()
    dijkstraTimes = []
    for n in range(10 ** 3, 10 ** 5, 1000):
        print(n / 10 ** 5 * 100) #  можно считать, что это проценты до окончания расчетов
        m = 100 * n
        timedijkstra = dijkstra.measure(n=n, m=m)
        saveTimesWithName([timedijkstra], "./Datasources/dijkstraA")
        dijkstraTimes.append(timedijkstra)

def collectDataDijkstraB():
    dijkstra = DijkstraMeasure()
    for n in range(10 ** 3, 10 ** 5, 1000):
        print(n / 10 ** 5 * 100)
        m = 1000 * n
        timedijkstra = dijkstra.measure(n=n, m=m)
        saveTimesWithName([timedijkstra], "./Datasources/dijkstraB")

def collectDataBellmanFordA():
    bellmanFord = BellmanFordMeasure()
    for n in range(10 ** 3, 10 ** 5, 1000):
        print(n / 10 ** 5 * 100)
        m = 100 * n
        timeBellman = bellmanFord.measure(n=n, m=m)
        saveTimesWithName([timeBellman], "./Datasources/bellmanFordA")

def collectDataBellmanFordB():
    bellmanFord = BellmanFordMeasure()
    for n in range(10 ** 1, 10 ** 5, 1000):
        print(n / 10 ** 5 * 100)
        m = 1000 * n
        timeBellman = bellmanFord.measure(n=n, m=m)
        saveTimesWithName([timeBellman], "./Datasources/bellmanFordB")

collectDataDijkstraA()  # возможно стоит запускать их по отдельности
collectDataDijkstraB()
collectDataBellmanFordA()
collectDataBellmanFordB()
exit()

# после повторного запуска функции, результаты пишутся в тот же файл,
# при необходимости очистка производится вручную