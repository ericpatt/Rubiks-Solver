from copy import deepcopy


class FaceletModel:

    def __init__(self, state):
        self.stickers = state

    def get_state(self):
        return deepcopy(self.stickers)

    def get(self, ind):
        return deepcopy(self.stickers[ind])

    def __rotate_face_counterclockwise(self, temp, start_ind):
        ind = start_ind * 9
        temp[ind] = self.stickers[ind + 2]
        temp[ind + 1] = self.stickers[ind + 5]
        temp[ind + 2] = self.stickers[ind + 8]
        temp[ind + 3] = self.stickers[ind + 1]
        temp[ind + 5] = self.stickers[ind + 7]
        temp[ind + 6] = self.stickers[ind]
        temp[ind + 7] = self.stickers[ind + 3]
        temp[ind + 8] = self.stickers[ind + 6]

    def __rotate_face_clockwise(self, temp, start_ind):
        ind = start_ind * 9
        temp[ind] = self.stickers[ind + 6]
        temp[ind + 1] = self.stickers[ind + 3]
        temp[ind + 2] = self.stickers[ind]
        temp[ind + 3] = self.stickers[ind + 7]
        temp[ind + 5] = self.stickers[ind + 1]
        temp[ind + 6] = self.stickers[ind + 8]
        temp[ind + 7] = self.stickers[ind + 5]
        temp[ind + 8] = self.stickers[ind + 2]

    def move(self, face):
        temp = self.get_state()
        if face == "b":
            # rotate blue face
            self.__rotate_face_clockwise(temp, 0)

            # yellow face
            temp[42] = self.stickers[35]
            temp[43] = self.stickers[32]
            temp[44] = self.stickers[29]

            # red face
            temp[18] = self.stickers[42]
            temp[21] = self.stickers[43]
            temp[24] = self.stickers[44]

            # white face
            temp[45] = self.stickers[24]
            temp[46] = self.stickers[21]
            temp[47] = self.stickers[18]

            # orange face
            temp[29] = self.stickers[45]
            temp[32] = self.stickers[46]
            temp[35] = self.stickers[47]

        elif face == "b'":
            # b, g, r, o, y, w
            # 0, 1, 2, 3, 4, 5
            # rotate blue face
            self.__rotate_face_counterclockwise(temp, 0)

             # yellow face
            temp[42] = self.stickers[18]
            temp[43] = self.stickers[21]
            temp[44] = self.stickers[24]

            # red face
            temp[18] = self.stickers[47]
            temp[21] = self.stickers[46]
            temp[24] = self.stickers[45]

            # white face
            temp[45] = self.stickers[29]
            temp[46] = self.stickers[32]
            temp[47] = self.stickers[35]

            # orange face
            temp[29] = self.stickers[44]
            temp[32] = self.stickers[43]
            temp[35] = self.stickers[42]

        elif face == "b2":
            self.move("b")
            self.move("b")
            return

        elif face == "g":
            # rotate green face
            self.__rotate_face_clockwise(temp, 1)

            # yellow face
            temp[36] = self.stickers[20]
            temp[37] = self.stickers[23]
            temp[38] = self.stickers[26]

            # red face
            temp[20] = self.stickers[53]
            temp[23] = self.stickers[52]
            temp[26] = self.stickers[51]

            # white face
            temp[51] = self.stickers[27]
            temp[52] = self.stickers[30]
            temp[53] = self.stickers[33]

            # orange face
            temp[27] = self.stickers[38]
            temp[30] = self.stickers[37]
            temp[33] = self.stickers[36]

        elif face == "g'":
            # rotate green face
            self.__rotate_face_counterclockwise(temp, 1)

            # yellow face
            temp[36] = self.stickers[33]
            temp[37] = self.stickers[30]
            temp[38] = self.stickers[27]

            # red face
            temp[20] = self.stickers[36]
            temp[23] = self.stickers[37]
            temp[26] = self.stickers[38]

            # white face
            temp[51] = self.stickers[26]
            temp[52] = self.stickers[23]
            temp[53] = self.stickers[20]

            # orange face
            temp[27] = self.stickers[51]
            temp[30] = self.stickers[52]
            temp[33] = self.stickers[53]

        elif face == "g2":
            self.move("g")
            self.move("g")
            return

        elif face == "w":
            # rotate white face
            self.__rotate_face_clockwise(temp, 5)

            # blue face
            temp[6] = self.stickers[33]
            temp[7] = self.stickers[34]
            temp[8] = self.stickers[35]

            # red face
            temp[24] = self.stickers[6]
            temp[25] = self.stickers[7]
            temp[26] = self.stickers[8]

            # green face
            temp[9] = self.stickers[26]
            temp[10] = self.stickers[25]
            temp[11] = self.stickers[24]

            # orange face
            temp[33] = self.stickers[11]
            temp[34] = self.stickers[10]
            temp[35] = self.stickers[9]

        elif face == "w'":
            # rotate white face
            self.__rotate_face_counterclockwise(temp, 5)

            # blue face
            temp[6] = self.stickers[24]
            temp[7] = self.stickers[25]
            temp[8] = self.stickers[26]

            # red face
            temp[24] = self.stickers[11]
            temp[25] = self.stickers[10]
            temp[26] = self.stickers[9]
            # green face
            temp[9] = self.stickers[35]
            temp[10] = self.stickers[34]
            temp[11] = self.stickers[33]

            # orange face
            temp[33] = self.stickers[6]
            temp[34] = self.stickers[7]
            temp[35] = self.stickers[8]

        elif face == "w2":
            self.move("w")
            self.move("w")
            return

        elif face == "y":
            # rotate yellow face
            self.__rotate_face_clockwise(temp, 4)

            # blue face
            temp[0] = self.stickers[18]
            temp[1] = self.stickers[19]
            temp[2] = self.stickers[20]

            # red face
            temp[18] = self.stickers[17]
            temp[19] = self.stickers[16]
            temp[20] = self.stickers[15]

            # green face
            temp[15] = self.stickers[29]
            temp[16] = self.stickers[28]
            temp[17] = self.stickers[27]

            # orange face
            temp[27] = self.stickers[0]
            temp[28] = self.stickers[1]
            temp[29] = self.stickers[2]

        elif face == "y'":
            # rotate yellow face
            self.__rotate_face_counterclockwise(temp, 4)

            # blue face
            temp[0] = self.stickers[27]
            temp[1] = self.stickers[28]
            temp[2] = self.stickers[29]

            # red face
            temp[18] = self.stickers[0]
            temp[19] = self.stickers[1]
            temp[20] = self.stickers[2]

            # green face
            temp[15] = self.stickers[20]
            temp[16] = self.stickers[19]
            temp[17] = self.stickers[18]

            # orange face
            temp[27] = self.stickers[17]
            temp[28] = self.stickers[16]
            temp[29] = self.stickers[15]

        elif face == "y2":
            self.move("y")
            self.move("y")
            return

        elif face == "r":
            # rotate red face
            self.__rotate_face_clockwise(temp, 2)

            # blue face
            temp[2] = self.stickers[47]
            temp[5] = self.stickers[50]
            temp[8] = self.stickers[53]

            # yellow face
            temp[38] = self.stickers[2]
            temp[41] = self.stickers[5]
            temp[44] = self.stickers[8]

            # green face
            temp[11] = self.stickers[38]
            temp[14] = self.stickers[41]
            temp[17] = self.stickers[44]

            # white face
            temp[47] = self.stickers[11]
            temp[50] = self.stickers[14]
            temp[53] = self.stickers[17]

        elif face == "r'":
            # rotate red face
            self.__rotate_face_counterclockwise(temp, 2)

            # blue face
            temp[2] = self.stickers[38]
            temp[5] = self.stickers[41]
            temp[8] = self.stickers[44]

            # yellow face
            temp[38] = self.stickers[11]
            temp[41] = self.stickers[14]
            temp[44] = self.stickers[17]

            # green face
            temp[11] = self.stickers[47]
            temp[14] = self.stickers[50]
            temp[17] = self.stickers[53]

            # white face
            temp[47] = self.stickers[2]
            temp[50] = self.stickers[5]
            temp[53] = self.stickers[8]

        elif face == "r2":
            self.move("r")
            self.move("r")
            return

        elif face == "o":
            # rotate orange face
            self.__rotate_face_clockwise(temp, 3)

            # blue face
            temp[0] = self.stickers[36]
            temp[3] = self.stickers[39]
            temp[6] = self.stickers[42]

            # yellow face
            temp[36] = self.stickers[9]
            temp[39] = self.stickers[12]
            temp[42] = self.stickers[15]

            # green face
            temp[9] = self.stickers[45]
            temp[12] = self.stickers[48]
            temp[15] = self.stickers[51]

            # white face
            temp[45] = self.stickers[0]
            temp[48] = self.stickers[3]
            temp[51] = self.stickers[6]

        elif face == "o'":
            # rotate orange face
            self.__rotate_face_counterclockwise(temp, 3)

            # blue face
            temp[0] = self.stickers[45]
            temp[3] = self.stickers[48]
            temp[6] = self.stickers[51]

            # yellow face
            temp[36] = self.stickers[0]
            temp[39] = self.stickers[3]
            temp[42] = self.stickers[6]

            # green face
            temp[9] = self.stickers[36]
            temp[12] = self.stickers[39]
            temp[15] = self.stickers[42]

            # white face
            temp[45] = self.stickers[9]
            temp[48] = self.stickers[12]
            temp[51] = self.stickers[15]

        elif face == "o2":
            self.move("o")
            self.move("o")
            return

        self.stickers = deepcopy(temp)

    # def unmove(self, face):
    #     if face == "b":
    #         self.move("b'")
    #     elif face == "b'":
    #         self.move("b")
    #     elif face == "g":
    #         self.move("g'")
    #     elif face == "g'":
    #         self.move("g")
    #     elif face == "r":
    #         self.move("r'")
    #     elif face == "r'":
    #         self.move("r")
    #     elif face == "o":
    #         self.move("o'")
    #     elif face == "o'":
    #         self.move("o")
    #     elif face == "y":
    #         self.move("y'")
    #     elif face == "y'":
    #         self.move("y")
    #     elif face == "w":
    #         self.move("w'")
    #     elif face == "w'":
    #         self.move("w")
