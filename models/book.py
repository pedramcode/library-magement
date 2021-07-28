import utils


class Book:
    def __init__(self, name=None, about=None, category=None):
        self.code = utils.random_code()
        self.name = name
        self.about = about
        self.category = category

    def save(self, pool):
        pool.append(self)
    
    def __str__(self):
        return f"Code: {self.code}\nName: {self.name}\nCategory: {self.category}\nAbout: {self.about}"