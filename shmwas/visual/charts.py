import matplotlib.pyplot as plt

def plot_age(patients):
    ages = []

    for p in patients:
        try:
            ages.append(int(p.age))
        except:
            pass

    plt.hist(ages)
    plt.show()