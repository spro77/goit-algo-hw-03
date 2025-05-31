import matplotlib.pyplot as plt
import numpy as np
import argparse

def koch_snowflake(order, scale=10):
    def _koch_recursion(start, end, order):
        if order == 0:
            return [start, end]
        else:
            start = np.array(start)
            end = np.array(end)
            delta = (end - start) / 3
            p1 = start + delta
            p2 = start + 2 * delta
            angle = np.deg2rad(60)
            px = p1[0] + delta[0] * np.cos(angle) - delta[1] * np.sin(angle)
            py = p1[1] + delta[0] * np.sin(angle) + delta[1] * np.cos(angle)
            peak = [px, py]

            return (
                _koch_recursion(start, p1, order - 1)[:-1] +
                _koch_recursion(p1, peak, order - 1)[:-1] +
                _koch_recursion(peak, p2, order - 1)[:-1] +
                _koch_recursion(p2, end, order - 1)
            )
    # Initial Triangle points
    p0 = [0, 0]
    p1 = [scale, 0]
    angle = np.deg2rad(60)
    p2 = [scale / 2, scale * np.sin(angle)]
    points = []
    for (a, b) in [(p0, p1), (p1, p2), (p2, p0)]:
        points += _koch_recursion(a, b, order)[:-1]
    points.append(points[0])
    return np.array(points)

def main():
    parser = argparse.ArgumentParser(description="Koch snowflake fractal (w/ matplotlib)")
    parser.add_argument("-l", "--level", type=int, default=3, help="Recursion level (default: 3)")
    args = parser.parse_args()

    pts = koch_snowflake(args.level)
    plt.figure(figsize=(6, 6))
    plt.plot(pts[:, 0], pts[:, 1])
    plt.axis('equal')
    plt.title(f"Koch Snowflake (Level {args.level})")
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    main()