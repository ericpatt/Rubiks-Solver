class RubiksModel:

    def __init__(self, facelet, cubie):
        self.facelet_model = facelet
        self.cubie_model = cubie

    def move(self, face):
        self.facelet_model.move(face)
        self.cubie_model.move(face)

    def get_facelets(self):
        return self.facelet_model

    def get_cubies(self):
        return self.cubie_model
