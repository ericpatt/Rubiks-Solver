from copy import deepcopy


class CubieModel:

    def __init__(self):
        # URF, ULF, ULB, URB, DRF, DLF, DLB, DRB
        # BYR, BWR, BWO, BYO, GYR, GWR, GWO, GYO
        self.corners = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0)]

        # UF, UL, UB, UR, FR, FL, BL, BR, DF, DL, DB, DR
        # BR, BW, BO, BY, RY, RW, OW, OY, GR, GW, GO, GY
        self.edges = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0), (9, 0), (10, 0), (11, 0)]

    def get_corners(self):
        return deepcopy(self.corners)

    def get_edges(self):
        return deepcopy(self.edges)

    def get_corner(self, ind):
        return deepcopy(self.corners[ind])

    def get_corner_oriented(self, ind, orientation):
        (i, o) = self.get_corner(ind)
        o += orientation
        o %= 3
        return i, o

    def get_edge_oriented(self, ind, orientation):
        (i, o) = self.get_edge(ind)
        o += orientation
        o %= 2
        return i, o

    def get_edge(self, ind):
        return deepcopy(self.edges[ind])

    def move(self, face):
        temp_corners = self.get_corners()
        temp_edges = self.get_edges()

        if face == "b":
            temp_corners[0] = self.get_corner_oriented(3, 0)
            temp_corners[1] = self.get_corner_oriented(0, 0)
            temp_corners[2] = self.get_corner_oriented(1, 0)
            temp_corners[3] = self.get_corner_oriented(2, 0)

            temp_edges[0] = self.get_edge_oriented(3, 0)
            temp_edges[1] = self.get_edge_oriented(0, 0)
            temp_edges[2] = self.get_edge_oriented(1, 0)
            temp_edges[3] = self.get_edge_oriented(2, 0)
        elif face == "b'":
            temp_corners[0] = self.get_corner_oriented(1, 0)
            temp_corners[1] = self.get_corner_oriented(2, 0)
            temp_corners[2] = self.get_corner_oriented(3, 0)
            temp_corners[3] = self.get_corner_oriented(0, 0)

            temp_edges[0] = self.get_edge_oriented(1, 0)
            temp_edges[1] = self.get_edge_oriented(2, 0)
            temp_edges[2] = self.get_edge_oriented(3, 0)
            temp_edges[3] = self.get_edge_oriented(0, 0)
        elif face == "b2":
            temp_corners[0] = self.get_corner_oriented(2, 0)
            temp_corners[1] = self.get_corner_oriented(3, 0)
            temp_corners[2] = self.get_corner_oriented(0, 0)
            temp_corners[3] = self.get_corner_oriented(1, 0)

            temp_edges[0] = self.get_edge_oriented(2, 0)
            temp_edges[1] = self.get_edge_oriented(3, 0)
            temp_edges[2] = self.get_edge_oriented(0, 0)
            temp_edges[3] = self.get_edge_oriented(1, 0)
        elif face == "g":
            temp_corners[4] = self.get_corner_oriented(5, 0)
            temp_corners[5] = self.get_corner_oriented(6, 0)
            temp_corners[6] = self.get_corner_oriented(7, 0)
            temp_corners[7] = self.get_corner_oriented(4, 0)

            temp_edges[8] = self.get_edge_oriented(9, 0)
            temp_edges[9] = self.get_edge_oriented(10, 0)
            temp_edges[10] = self.get_edge_oriented(11, 0)
            temp_edges[11] = self.get_edge_oriented(8, 0)
        elif face == "g'":
            temp_corners[4] = self.get_corner_oriented(7, 0)
            temp_corners[5] = self.get_corner_oriented(4, 0)
            temp_corners[6] = self.get_corner_oriented(5, 0)
            temp_corners[7] = self.get_corner_oriented(6, 0)

            temp_edges[8] = self.get_edge_oriented(11, 0)
            temp_edges[9] = self.get_edge_oriented(8, 0)
            temp_edges[10] = self.get_edge_oriented(9, 0)
            temp_edges[11] = self.get_edge_oriented(10, 0)
        elif face == "g2":
            temp_corners[4] = self.get_corner_oriented(6, 0)
            temp_corners[5] = self.get_corner_oriented(7, 0)
            temp_corners[6] = self.get_corner_oriented(4, 0)
            temp_corners[7] = self.get_corner_oriented(5, 0)

            temp_edges[8] = self.get_edge_oriented(10, 0)
            temp_edges[9] = self.get_edge_oriented(11, 0)
            temp_edges[10] = self.get_edge_oriented(8, 0)
            temp_edges[11] = self.get_edge_oriented(9, 0)
        elif face == "r":
            temp_corners[0] = self.get_corner_oriented(1, 1)
            temp_corners[1] = self.get_corner_oriented(5, 2)
            temp_corners[4] = self.get_corner_oriented(0, 2)
            temp_corners[5] = self.get_corner_oriented(4, 1)

            temp_edges[0] = self.get_edge_oriented(5, 1)
            temp_edges[4] = self.get_edge_oriented(0, 0)
            temp_edges[5] = self.get_edge_oriented(8, 0)
            temp_edges[8] = self.get_edge_oriented(4, 1)
        elif face == "r'":
            temp_corners[0] = self.get_corner_oriented(4, 1)
            temp_corners[1] = self.get_corner_oriented(0, 2)
            temp_corners[4] = self.get_corner_oriented(5, 2)
            temp_corners[5] = self.get_corner_oriented(1, 1)

            temp_edges[0] = self.get_edge_oriented(4, 0)
            temp_edges[4] = self.get_edge_oriented(8, 1)
            temp_edges[5] = self.get_edge_oriented(0, 1)
            temp_edges[8] = self.get_edge_oriented(5, 0)
        elif face == "r2":
            temp_corners[0] = self.get_corner_oriented(5, 0)
            temp_corners[1] = self.get_corner_oriented(4, 0)
            temp_corners[4] = self.get_corner_oriented(1, 0)
            temp_corners[5] = self.get_corner_oriented(0, 0)

            temp_edges[0] = self.get_edge_oriented(8, 0)
            temp_edges[4] = self.get_edge_oriented(5, 0)
            temp_edges[5] = self.get_edge_oriented(4, 0)
            temp_edges[8] = self.get_edge_oriented(0, 0)
        elif face == "o":
            temp_corners[2] = self.get_corner_oriented(3, 1)
            temp_corners[3] = self.get_corner_oriented(7, 2)
            temp_corners[6] = self.get_corner_oriented(2, 2)
            temp_corners[7] = self.get_corner_oriented(6, 1)

            temp_edges[2] = self.get_edge_oriented(7, 0)
            temp_edges[6] = self.get_edge_oriented(2, 1)
            temp_edges[7] = self.get_edge_oriented(10, 1)
            temp_edges[10] = self.get_edge_oriented(6, 0)
        elif face == "o'":
            temp_corners[2] = self.get_corner_oriented(6, 1)
            temp_corners[3] = self.get_corner_oriented(2, 2)
            temp_corners[6] = self.get_corner_oriented(7, 2)
            temp_corners[7] = self.get_corner_oriented(3, 1)

            temp_edges[2] = self.get_edge_oriented(6, 0)
            temp_edges[6] = self.get_edge_oriented(10, 1)
            temp_edges[7] = self.get_edge_oriented(2, 1)
            temp_edges[10] = self.get_edge_oriented(8, 0)
        elif face == "o2":
            temp_corners[2] = self.get_corner_oriented(7, 0)
            temp_corners[3] = self.get_corner_oriented(6, 0)
            temp_corners[6] = self.get_corner_oriented(3, 0)
            temp_corners[7] = self.get_corner_oriented(2, 0)

            temp_edges[2] = self.get_edge_oriented(10, 0)
            temp_edges[6] = self.get_edge_oriented(7, 0)
            temp_edges[7] = self.get_edge_oriented(6, 0)
            temp_edges[10] = self.get_edge_oriented(2, 0)
        elif face == "y":
            temp_corners[0] = self.get_corner_oriented(4, 2)
            temp_corners[3] = self.get_corner_oriented(0, 1)
            temp_corners[4] = self.get_corner_oriented(7, 1)
            temp_corners[7] = self.get_corner_oriented(3, 2)

            temp_edges[3] = self.get_edge_oriented(4, 0)
            temp_edges[4] = self.get_edge_oriented(11, 0)
            temp_edges[7] = self.get_edge_oriented(3, 0)
            temp_edges[11] = self.get_edge_oriented(7, 0)
        elif face == "y'":
            temp_corners[0] = self.get_corner_oriented(3, 2)
            temp_corners[3] = self.get_corner_oriented(7, 1)
            temp_corners[4] = self.get_corner_oriented(0, 1)
            temp_corners[7] = self.get_corner_oriented(4, 2)

            temp_edges[3] = self.get_edge_oriented(7, 0)
            temp_edges[4] = self.get_edge_oriented(3, 0)
            temp_edges[7] = self.get_edge_oriented(11, 0)
            temp_edges[11] = self.get_edge_oriented(4, 0)
        elif face == "y2":
            temp_corners[0] = self.get_corner_oriented(7, 0)
            temp_corners[3] = self.get_corner_oriented(4, 0)
            temp_corners[4] = self.get_corner_oriented(3, 0)
            temp_corners[7] = self.get_corner_oriented(0, 0)

            temp_edges[3] = self.get_edge_oriented(11, 0)
            temp_edges[4] = self.get_edge_oriented(7, 0)
            temp_edges[7] = self.get_edge_oriented(4, 0)
            temp_edges[11] = self.get_edge_oriented(3, 0)
        elif face == "w":
            temp_corners[1] = self.get_corner_oriented(2, 1)
            temp_corners[2] = self.get_corner_oriented(6, 2)
            temp_corners[5] = self.get_corner_oriented(1, 2)
            temp_corners[6] = self.get_corner_oriented(5, 1)

            temp_edges[1] = self.get_edge_oriented(6, 0)
            temp_edges[5] = self.get_edge_oriented(1, 0)
            temp_edges[6] = self.get_edge_oriented(9, 0)
            temp_edges[9] = self.get_edge_oriented(5, 0)
        elif face == "w'":
            temp_corners[1] = self.get_corner_oriented(5, 1)
            temp_corners[2] = self.get_corner_oriented(1, 2)
            temp_corners[5] = self.get_corner_oriented(6, 2)
            temp_corners[6] = self.get_corner_oriented(2, 1)

            temp_edges[1] = self.get_edge_oriented(5, 0)
            temp_edges[5] = self.get_edge_oriented(9, 0)
            temp_edges[6] = self.get_edge_oriented(1, 0)
            temp_edges[9] = self.get_edge_oriented(6, 0)
        elif face == "w2":
            temp_corners[1] = self.get_corner_oriented(6, 0)
            temp_corners[2] = self.get_corner_oriented(5, 0)
            temp_corners[5] = self.get_corner_oriented(2, 0)
            temp_corners[6] = self.get_corner_oriented(1, 0)

            temp_edges[1] = self.get_edge_oriented(9, 0)
            temp_edges[5] = self.get_edge_oriented(6, 0)
            temp_edges[6] = self.get_edge_oriented(5, 0)
            temp_edges[9] = self.get_edge_oriented(1, 0)

        self.corners = deepcopy(temp_corners)
        self.edges = deepcopy(temp_edges)

    def print(self):
        for c in self.corners:
            print(c)
        print()
