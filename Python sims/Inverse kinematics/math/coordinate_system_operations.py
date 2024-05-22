def distance_between_2_points_in_2D(P: list, Q: list): #P[x, y] = P(x; y)
    return ((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2) ** 0.5

def distance_between_2_points_in_3D(P: list, Q: list): #P[x, y, z] = P(x; y; z)
    return ((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2 + (P[2] - Q[2]) ** 2) ** 0.5