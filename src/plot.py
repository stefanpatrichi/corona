import matplotlib.pyplot as plt
with open('data/cases.in', 'r') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))
growth = []
for i in range(len(arr) - 2):
    d = arr[i + 2] - arr[i + 1]
    e = arr[i + 1] - arr[i]
    growth.append(d / e if e > 0 else (growth[i - 1] if i > 0 else 0))
plt.plot([n for n in range(len(arr))], [n for n in arr])
plt.savefig('images/cases.png')
plt.clf()
plt.plot([n for n in range(len(arr) - 2)], [growth[i] for i in range(len(arr) - 2)])
plt.savefig('images/growth_graph.png')
plt.show()
plt.clf()
