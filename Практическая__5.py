class Room:
    def __init__(self, x, y, z):
        self.length = x
        self.width = y
        self.height = z
        self.wd = []
 
    def addWD(self, y, z):
        self.wd.append(WinDoor(y, z))
 
    def fullSerface(self):
        return 2 * self.height * (self.length + self.width)
 
    def workSurface(self):
        new_square = self.fullSerface()
        for i in self.wd:
            new_square -= i.square
        return new_square
 
    def wallpapers(self, x, y):
        return math.ceil(self.workSurface() / (x * y))
 
 
print("Размеры помещения:")
x = float(input("Длина "))
y = float(input("Ширина "))
z = float(input("Высота "))
r1 = Room(x, y, z)
 
flag = input("Есть неоклеиваемая поверхность? (1 - да, 2 - нет) ")
while flag == '1':
    w = float(input("Ширина - "))
    h = float(input("Высота - "))
    r1.addWD(y, z)
    flag = input("Добавить еще? (1 - да, 2 - нет) ")
 
print("Размеры рулона:")
x = float(input("Длина - "))
y = float(input("Ширина - "))
 
print("Площадь оклейки", r1.workSurface())
print("Количество рулонов", r1.wallpapers(x, y))