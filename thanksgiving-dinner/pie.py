from plate_decorator import PlateDecorator


class Pie(PlateDecorator):

    def description(self):
        if super().count() == 0:
            return super().description() + " Pie"
        else:
            return super().description() + " and Pie"

    def area(self):
        return super().area() - 19

    def weight(self):
        return super().weight() - 8

    def count(self):
        return super().count() + 1
