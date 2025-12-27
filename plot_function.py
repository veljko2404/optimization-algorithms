import matplotlib.pyplot as plt


def plot_function(xs, ys, path, f, function, x_min, name):
    plt.figure(figsize=(9, 6))
    plt.plot(xs, ys, label=function, linewidth=2)
    plt.scatter(path, [f(x) for x in path], s=50, color="red", label="Path")
    plt.plot(path, [f(x) for x in path], color="red", linestyle="--")
    plt.scatter([x_min], [f(x_min)], s=100, color="green", label=f"Minimum found value {x_min:.2f}")

    plt.title(name)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()
    plt.show()
