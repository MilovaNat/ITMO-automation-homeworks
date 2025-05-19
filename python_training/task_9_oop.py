class Button:

    type: str = "button"

    def __init__(self, text, link):
        self.text = text
        self.link = link



b = Button("text", "link")

print(b.text)
print(b.link)
print(b.type)

class Button2:
    type: str = "button2"

    def __init__(self, text, link):
        self.text = text
        self.link = link

    def click(self):
        return "Я тыкнул кнопку - {}".format(self.text)


button2 = Button2("text", "link")
print(button2.click())