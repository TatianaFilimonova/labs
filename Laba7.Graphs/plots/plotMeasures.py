import matplotlib.pyplot as plt

def plotMeasure(fileName):
    file = open(f"../datasources/{fileName}.txt", 'r')
    nums = list(map(float, file.read()[:-1].split()))
    x = [xi for xi in range(10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)]
    y = nums

    plt.plot(x,y)
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.title(f'{fileName}', fontsize=16, fontname='Arial')
    plt.savefig(f"..\plots\{fileName}.png")
    plt.show()
    plt.clf()

def plotMeasureDijkstraA():
    file = open(f"..\datasources\dijkstraA.txt", 'r')
    nums = list(map(float, file.read()[:-1].split()))
    x = [xi for xi in range(10 ** 3, 10 ** 3 + 1000 * len(nums), 1000)]
    y = nums

    plt.plot(x, y)
    plt.xlabel('Number of vertices')
    plt.ylabel('Time')
    plt.title('Dijkstra a', fontsize=16, fontname='Arial')
    plt.savefig(f"..\plots\dijkstraA.png")
    plt.show()
    plt.clf()

# dijkstraA >> 10 ** 3, 10 ** 3 + 1000 * len(nums), 1000)
# dijkstraB >> 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
# bellmanFordA >>  10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)
# bellmanFordB >> 10 ** 1, 10 ** 1 + 1000 * len(nums), 1000)

plotMeasureDijkstraA()
#plotMeasure('dijkstraB')
#plotMeasure('bellmanFordA')
#plotMeasure('bellmanFordB')
