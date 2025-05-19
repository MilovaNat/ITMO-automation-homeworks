#task 1
class Rectangle:


    def __init__(self, width, height):
        self.width = width
        self.height = height


    def square(self):
        return self.width * self.height


    def perimeter(self ):
         return 2 * (self.width + self.height)

obj1 = Rectangle(10, 10)
obj2 = Rectangle(2, 6)
obj3 = Rectangle(1, 2)

print('Task 1')
print(f'obj1 square: {obj1.square()}, perimeter: {obj1.perimeter()}')
print(f'obj2 square: {obj2.square()}, perimeter: {obj2.perimeter()}')
print(f'obj2 square: {obj3.square()}, perimeter: {obj3.perimeter()}')
print('\n')

#task2
class Math:

    def __init__(self, a = None, b = None):
        self.a = a
        self.b = b


    @staticmethod
    def addition(a, b):
        return a + b


    @staticmethod
    def subtraction(a, b):
        return a - b


    @staticmethod
    def multiplication(a, b):
        return a * b


    @staticmethod
    def division(a, b):
        return a / b

print('Task 2')
print(Math.addition(1, 2))
print(Math.subtraction(9, 2))
print(Math.multiplication(2, 2))
print(Math.division(10, 9))
print('\n')

#task3
class Button:


    type: str = 'Кнопка'

    def __init__(self, text, loc = None):
        self.text = text
        self.loc = loc


    def click(self):
        print(f'Клик по кнопке {self.text}\n')

class TextBox(Button):


    def __init__(self):
        super().__init__('TextBox')


class CheckBox(Button):


    def __init__(self):
        super().__init__('CheckBox')


class RadioButton(Button):

    def __init__(self):
        super().__init__('RadioButton')

class WebTables(Button):

    def __init__(self):
        super().__init__('WebTables')

class Buttons(Button):

    def __init__(self):
        super().__init__('Buttons')


class Links(Button):

    def __init__(self):
        super().__init__('Links')


class BrokenLinksImages(Button):

    def __init__(self):
        super().__init__('Broken Links - Images')


class UploadAndDownload(Button):

    def __init__(self):
        super().__init__('Upload and Download')

class DynamicProperties(Button):

    def __init__(self):
        super().__init__('Dynamic Properties')

text_box = TextBox()
print(f'Текст кнопки {text_box.text}')
text_box.click()

check_box = CheckBox()
print(f'Текст кнопки {check_box.text}')
check_box.click()

radio_button = RadioButton()
print(f'Текст кнопки {radio_button.text}')
radio_button.click()

web_tables = WebTables()
print(f'Текст кнопки {web_tables.text}')
web_tables.click()

buttons = Buttons()
print(f'Текст кнопки {buttons.text}')
buttons.click()

links = Links()
print(f'Текст кнопки {links.text}')
links.click()

broken_links_images = BrokenLinksImages()
print(f'Текст кнопки {broken_links_images.text}')
broken_links_images.click()

upload_and_download = UploadAndDownload()
print(f'Текст кнопки {upload_and_download.text}')
upload_and_download.click()

dynamic_properties = DynamicProperties()
print(f'Текст кнопки {dynamic_properties.text}')
dynamic_properties.click()