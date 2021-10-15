##### CLASSES #####

class Car:

    def __init__(self, id, length, position=-1):
        self.id = id
        self.length = length
        self.position = position


class Parking:

    def __init__(self, parking_length):
        self.parking_length = "v"*parking_length
        self.invoiced_revenue = 0
        self.__arrived = []

    def to_park(self, car):
        position = self.parking_length.find("v"*car.length)

        if position != -1:
            car.position = position
            self.__arrived.append(car)
            self.invoiced_revenue += 10
            self.parking_length = self.parking_length.replace(
                "v"*car.length, "o"*car.length, 1)

            return True

        else:
            return False

    def remove(self, car):
        found_car = [
            icar for icar in self.__arrived if icar.id == car.id].pop()
        self.__arrived.remove(found_car)
        parking_length = list(self.parking_length)

        for i in range(found_car.position, found_car.position+found_car.length):
            parking_length[i] = "v"

        self.parking_length = "".join(parking_length)

    def check_if_car_is_present(self, car):
        return True if True in [True for icar in self.__arrived if icar.id == car.id] else False


##### FUNCTIONS #####
def main():
    args = input().split(" ")
    (parking_length, events_qty) = [int(number) for number in args]
    parking = Parking(parking_length)


    for i in range(events_qty):
        event = input().split(" ")
        (option, id) = event[:2]
        length = int(event[2]) if len(event) == 3 else -1
        car = Car(id, length)

        if option.lower() == "c":
            parking.to_park(car)

        elif option.lower() == "s" and parking.check_if_car_is_present(car):
            parking.remove(car)


    print(f"{parking.invoiced_revenue}")


##### MAIN #####
while True:
    try: main()
    except EOFError: break