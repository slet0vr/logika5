class Widget():
    def __init__(self, x, y, label):
        self.x = x
        self.y = y
        self.label = label

    def print(self):
        print("Напис:", self.label)
        print("Розташування:", self.x, self.y)

class Button(Widget):
    def __init__(self, x, y, label, is_clicked):
        super().__init__(x, y, label)
        self.is_clicked = is_clicked

    def click(self):
        self.is_clicked = True
        print("Ви зареєстровані")

btn = Button(100, 100, "Брати участь", False)

