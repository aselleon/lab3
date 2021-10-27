class Shoe:

    def __init__(self, name, price, sizes, url):
        self.__name = name
        self.__price = price
        self.__sizes = sizes
        self.__url = url

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price

    def get_sizes(self):
        return self.__sizes

    def set_sizes(self, sizes):
        self.__sizes = sizes

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url
