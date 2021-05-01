import numpy as np
import matplotlib.pyplot as plt


# треугольник серпинского
def sierpinski_triangle(number_of_points, side_length):
    center_point_x_y = np.random.randint(10, size=2)  # координаты середины треугольника
    p1_x = center_point_x_y[0]  # координата верхней вершины
    p2_x = center_point_x_y[0] - np.sin(np.pi / 6) * side_length
    p3_x = center_point_x_y[0] + np.sin(np.pi / 6) * side_length
    xs_corners = [p1_x, p2_x, p3_x]
    p1_y = center_point_x_y[1] + (np.sqrt(3) / 3) * side_length
    p2_y = p1_y - np.cos(np.pi / 6) * side_length
    p3_y = p2_y
    ys_corners = [p1_y, p2_y, p3_y]
    xs = [0] * number_of_points
    ys = [0] * number_of_points
    xs[0] = np.random.randint(xs_corners[1], xs_corners[2])
    ys[0] = np.random.randint(ys_corners[1], ys_corners[0])
    for i in range(1, number_of_points):
        result = np.random.randint(1, 7)
        if result == 1 or result == 2:
            xs[i] = (xs[i - 1] + xs_corners[0]) / 2
            ys[i] = (ys[i - 1] + ys_corners[0]) / 2
        elif result == 3 or result == 4:
            xs[i] = (xs[i - 1] + xs_corners[1]) / 2
            ys[i] = (ys[i - 1] + ys_corners[1]) / 2
        else:
            xs[i] = (xs[i - 1] + xs_corners[2]) / 2
            ys[i] = (ys[i - 1] + ys_corners[2]) / 2
    plt.scatter(xs, ys)
    plt.scatter(xs_corners, ys_corners)
    plt.title("Sierpinski's triangle")
    plt.xlabel('$xs$')
    plt.ylabel('$ys$')
    plt.savefig("Sierpinski_triangle.png")
    plt.show()


# коврик серпинского
def sierpinski_carpet(number_of_points, side_length):
    p0 = np.random.randint(10, size=2)  # координаты нижнего левого угла
    px = [p0[0],
          p0[0],
          p0[0],
          p0[0] + side_length / 2,
          p0[0] + side_length,
          p0[0] + side_length,
          p0[0] + side_length,
          p0[0] + side_length / 2]
    py = [p0[1],
          p0[1] + side_length / 2,
          p0[1] + side_length,
          p0[1] + side_length,
          p0[1] + side_length,
          p0[1] + side_length / 2,
          p0[1],
          p0[1]]
    xs = [0] * number_of_points
    ys = [0] * number_of_points
    xs[0] = np.random.randint(px[0], px[6])
    ys[0] = np.random.randint(py[0], py[2])
    for i in range(1, number_of_points):
        result = np.random.randint(0, 8)
        if result == 0:
            xs[i] = (xs[i - 1] + 2 * px[0]) / 3
            ys[i] = (ys[i - 1] + 2 * py[0]) / 3
        elif result == 1:
            xs[i] = (xs[i - 1] + 2 * px[1]) / 3
            ys[i] = (ys[i - 1] + 2 * py[1]) / 3
        elif result == 2:
            xs[i] = (xs[i - 1] + 2 * px[2]) / 3
            ys[i] = (ys[i - 1] + 2 * py[2]) / 3
        elif result == 3:
            xs[i] = (xs[i - 1] + 2 * px[3]) / 3
            ys[i] = (ys[i - 1] + 2 * py[3]) / 3
        elif result == 4:
            xs[i] = (xs[i - 1] + 2 * px[4]) / 3
            ys[i] = (ys[i - 1] + 2 * py[4]) / 3
        elif result == 5:
            xs[i] = (xs[i - 1] + 2 * px[5]) / 3
            ys[i] = (ys[i - 1] + 2 * py[5]) / 3
        elif result == 6:
            xs[i] = (xs[i - 1] + 2 * px[6]) / 3
            ys[i] = (ys[i - 1] + 2 * py[6]) / 3
        else:
            xs[i] = (xs[i - 1] + 2 * px[7]) / 3
            ys[i] = (ys[i - 1] + 2 * py[7]) / 3
    plt.scatter(px, py)
    plt.scatter(xs, ys, s=0.2)
    plt.title("Sierpinski's carpet.")
    plt.savefig('Sierpinski_carpet.png')
    plt.show()
