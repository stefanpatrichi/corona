import matplotlib.pyplot as plt

def plot():
    print('Plotting..')
    conf = []
    rec = []
    dth = []
    active = []

    with open('../data/cases.in', 'r') as f:
        n = int(f.readline())
        for i in range(n):
            day = list(map(int, f.readline().split()))
            conf.append(day[0])
            rec.append(day[1])
            dth.append(day[2])
            active.append(day[0] - day[1] - day[2])
    plt.plot([n for n in range(len(conf))], [n for n in conf])
    plt.savefig('../images/cases.png')
    plt.clf()
    plt.plot([n for n in range(len(rec))], [n for n in rec])
    plt.savefig('../images/recov.png')
    plt.clf()
    plt.plot([n for n in range(len(dth))], [n for n in dth])
    plt.savefig('../images/deaths.png')
    plt.clf()
    plt.plot([n for n in range(len(active))], [n for n in active])
    plt.savefig('../images/actives.png')
    plt.clf()
