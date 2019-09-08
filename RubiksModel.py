from CoordinateModel import CoordinateModel


class RubiksModel:

    def __init__(self, facelet, cubie):
        self.facelet_model = facelet
        self.cubie_model = cubie
        self.coordinate_model = CoordinateModel(self.cubie_model)

    def move(self, face):
        self.facelet_model.move(face)
        self.cubie_model.move(face)

    def get_facelets(self):
        return self.facelet_model

    def get_cubies(self):
        return self.cubie_model

    def phase1_coords(self):
        return self.coordinate_model.phase1_coords()
