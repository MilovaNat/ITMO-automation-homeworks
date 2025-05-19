from task_9_checks import Checks

class Input(Checks):

    name : str = 'Input'

    def __init__(self, loc: str, text: str):
        super().__init__(loc)
        self.loc = loc
        self.text = text

class Button(Checks):

    name : str = 'Button'

    def __init__(self, loc: str, text: str):
        super().__init__(loc)
        self.loc = loc
        self.text = text

class Title(Checks):

    name : str = 'Title'

    def __init__(self, loc: str, text: str):
        super().__init__(loc)
        self.loc = loc
        self.text = text

class Link(Checks):

    name : str = 'Link'

    def __init__(self, loc: str, text : str):
        super().__init__(loc)
        self.loc = loc
        self.text = text

search = Input("input#search", "input_text")
button = Button("button#submit", "submit_text")
title = Title("title#main", "main_text")
link = Link("link#home", "home_text")

print("Input loc = {}, text = {}, check_text = {}".format(search.loc, search.text, search.check_text()))
print("Button loc = {}, text = {}, check_text = {}".format(button.loc, button.text, button.check_text()))
print("Title loc = {}, text = {}, check_text = {}".format(title.loc, title.text, title.check_text()))
print("Link loc = {}, text = {}, check_text = {}".format(link.loc, link.text, link.check_text()))