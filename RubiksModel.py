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

    def unmove(self, face):
        if face == "b":
            self.move("b'")
        elif face == "b'":
            self.move("b")
        elif face == "b2":
            self.move("b2")
        elif face == "g":
            self.move("g'")
        elif face == "g'":
            self.move("g")
        elif face == "g2":
            self.move("g2")
        elif face == "r":
            self.move("r'")
        elif face == "r'":
            self.move("r")
        elif face == "r2":
            self.move("r2")
        elif face == "o":
            self.move("o'")
        elif face == "o'":
            self.move("o")
        elif face == "o2":
            self.move("o2")
        elif face == "y":
            self.move("y'")
        elif face == "y'":
            self.move("y")
        elif face == "y2":
            self.move("y2")
        elif face == "w":
            self.move("w'")
        elif face == "w'":
            self.move("w")
        elif face == "w2":
            self.move("w2")
