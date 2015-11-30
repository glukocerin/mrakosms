# without class

# #
# lada = {
#     'color': 'red',
#     'type': 'Lada 1200',
#     'km': 40000
# }
#
# tesla = {
#     'color': 'pink',
#     'type': 'Tesla S',
#     'km': 1200
# }

# without class 2

def initCar(color, type, km):
    car = {'color': '', 'type': '', 'km': 0}
    car['color'] = color
    car['type'] = type
    car['km'] = km
    return car

lada = initCar('red', 'Lada 1200', 40000)
tesla = initCar('pink', 'Tesla S', 1200)
ifa = initCar('brown', 'Ifa', 3000000)

def ride(car, km):
    car['km'] += km

ride(ifa, 220)

print(ifa)
