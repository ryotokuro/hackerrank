class Difference:
    def __init__(self, a):
        self.__elements = a
        self.elements = []
        self.elements.append(a)
        self.maximumDifference = 0


    def computeDifference(self):
        sorted(self.__elements)
        self.maximumDifference = abs(self.__elements[0] - self.__elements[-1])
        return self.maxmimumDifference
# End of Difference class


_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)