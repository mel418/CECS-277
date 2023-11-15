from plate_decorator import PlateDecorator


class GreenBeans(PlateDecorator):

    def description(self):
        if super().count() == 0:
            return super().description() + " Green Beans"
        else:
            return super().description() + " and Green Beans"

    def area(self):
        return super().area() - 20

    def weight(self):
        return super().weight() - 3

    def count(self):
        return super().count() + 1
