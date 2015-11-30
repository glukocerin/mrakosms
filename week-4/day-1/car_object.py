class Car:
    def __init__(self, color, car_type, km):
        if type(color) != str:
            raise Exception('No string')
        self.color = color
        self.car_type = car_type
        self.km = km

    def ride(self, km):
        self.km += km

    def getMiles(self):
        return self.km * 0.6213

tesla = Car('yellow', 'Tesla S', 1200)
tesla.ride(220)
print(tesla.km)
print(tesla.getMiles())


# Car a tervrajz, hogyan kell autot csinalni, a tesla mar egy elkeszult auto, amit a classal csinaltunk. barmikor ahato hozza property.
