class Vecteur2D():
    _count = 0

    def __init__(self, X, Y):
        self.__X = X
        self.__Y = Y
        Vecteur2D._count += 1

    def getX(self):
        return self.__X

    def getY(self):
        return self.__Y

    def setX(self, X):
        self.__X = X

    def setY(self, Y):
        self.__Y = Y

    def ToString(self):
        print("l'abscisse X =", self.getX())
        print("l'ordonnee Y =", self.getY())

    def Equals(self, V2):
        X1, Y1 = self.getX(), self.getY()
        X2, Y2 = V2.getX(), V2.getY()

        if (X1 == X2) and (Y1 == Y2):
            return True
        else:
            return False

    def Norme(self):
        return ((self.__X)**2 + (self.__Y)**2)**0.5


class Vecteur3D(Vecteur2D):
    def __init__(self, X, Y, Z):
        super().__init__(X, Y)
        self.__Z = Z

    def getZ(self):
        return self.__Z

    def setZ(self, Z):
        self.__Z = Z

    def ToString(self):
        print("l'abscisse X =", self.getX())
        print("l'ordonnee Y =", self.getY())
        print("Z =", self.getZ())

    def Equals(self, V3):
        X2, Y2, Z2 = self.getX(), self.getY(), self.getZ()
        X3, Y3, Z3 = V3.getX(), V3.getY(), V3.getZ()

        if (X2 == X3) and (Y2 == Y3) and (Z2 == Z3):
            return True
        else:
            return False

    def Norme(self):
        return ((self.__X)**2 + (self.__Y)**2 + (self.__Z)**2)**0.5


vecte2 = Vecteur2D(3, 5)
print("Vecteur2D:")
vecte2.ToString()
print("Norm of V2D:", vecte2.Norme())

vecte3 = Vecteur3D(2, 1, 8)
print("Vecteur3D:")
vecte3.ToString()
print("Norm of V3D:", vecte3.Norme())
