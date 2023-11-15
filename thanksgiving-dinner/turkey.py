from plate_decorator import PlateDecorator


class Turkey(PlateDecorator):

    def description(self):
        if super().count() == 0:
            return super().description() + " Turkey"
        else:
            return super().description() + " and Turkey"

    def area(self):
        return super().area() - 15

    def weight(self):
        return super().weight() - 4

    def count(self):
        return super().count() + 1
