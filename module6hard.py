import math

class Figure:
    sides_count = 0
    def __init__(self, __color, *__sides: int):
        self.__sides = list(__sides)
        self.__color = __color
        self.filled = False


    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                self.__color = (r, g, b)
            else:
                print(f'Ошибка')
        else:
            print(f'Ошибка')

    def set_color(self, r, g, b):
        if isinstance(r, int) and isinstance(g, int) and isinstance(b, int):
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                self.__color = (r, g, b)
                return True
            else:
                return False
        else:
            return False

    def __is_valid_sides(self, *new_sides):
        if len(new_sides) != self.sides_count:
            for side in new_sides:
                if side <= 0:
                    return False
        return True

    def get_sides(self):
        return self.__sides

    def __len__(self):
        per = sum(self.__sides)
        return per

    def set_sides(self, *new_sides):
        new_sides = list(new_sides)
        if len(new_sides) != self.sides_count:
            return False
        else:
            self.__sides = new_sides

class Circle(Figure):
    def __init__(self, __color, side_length):
        sides_count = 1
        sides = [side_length] * sides_count
        super().__init__(__color, *sides)
        self.sides_count = sides_count
        self.__radius = sides_count / math.pi * 2

    def get_square(self):
        square = 2 * math.pi * self.__radius
        return square

class Triangle(Figure):
    def __init__(self, __color, side_length):
        sides_count = 3
        sides = [side_length] * sides_count
        super().__init__(__color, *sides)
        self.sides_count = sides_count

    def get_square(self):
        per = 0.5 * sum(self.__sides)
        side_1 = self.__sides[0]
        side_2 = self.__sides[1]
        side_3 = self.__sides[2]
        square = math.sqrt(per * ((per - side_1) * (per - side_2) * (per - side_3)))
        return square

class Cube(Figure):
    def __init__(self, __color, side_length):
        sides_count = 12
        sides = [side_length] * sides_count
        super().__init__(__color, *sides)
        self.sides_count = sides_count

    def get_volume(self):
        volume = self._Figure__sides[0] ** 3
        return volume


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
