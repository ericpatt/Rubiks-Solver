from scipy import special


class CoordinateModel:

    def __init__(self, cubie):
        self.cubie_model = cubie

    def phase1_coords(self):
        return self.corner_orientation_coord(), self.edge_orientation_coord(), self.ud_slice_coord()

    def corner_orientation_coord(self):
        corners = self.cubie_model.get_corners()
        coord = 0
        for i in range(7):
            coord += corners[i][1] * (3 ** (6 - i))
        return coord

    def edge_orientation_coord(self):
        edges = self.cubie_model.get_edges()
        coord = 0
        for i in range(11):
            coord += edges[i][1] * (2 ** (10 - i))
        return coord

    def ud_slice_coord(self):
        edges = self.cubie_model.get_edges()
        coord = 0
        ud_seen = 0
        for i in range(11, -1, -1):
            if edges[i][0] >= 8:
                ud_seen += 1
                if ud_seen >= 4:
                    break
            else:
                coord += special.comb(i, 3 - ud_seen, exact=True)

        return coord
