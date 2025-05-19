class Soda:

    def __init__(self, flavor = None):
        self.flavor = flavor

    def show_my_drink(self):
        if self.flavor is None:
            print("No flavor selected")
        else:
            print("Soda with flavor - {}".format(self.flavor))


soda_with_flavor = Soda("cola")
soda_without_flavor = Soda()

soda_with_flavor.show_my_drink()
soda_without_flavor.show_my_drink()