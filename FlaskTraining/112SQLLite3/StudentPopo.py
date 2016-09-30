class Student:
    def __init__(self, discOfStudent):
        self.name = discOfStudent["nm"]
        self.address = discOfStudent["addr"]
        self.city = discOfStudent["city"]
        self.pincode = discOfStudent["pin"]
