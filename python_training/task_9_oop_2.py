class Page:


    def __init__(self, url):
        self.url = url

    def get(self):
        print("Ссылка - {}".format(self.url))

home = Page("https://google.com")
home.get()