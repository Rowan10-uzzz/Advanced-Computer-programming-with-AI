from rental import Vehicle, Renter, ElectricCar, Motorbike


def main():
    car = Vehicle("Toyota", "Yaris", "1AB234")
    electric_car = ElectricCar("Tesla", "Model 3", "EV001", 60)
    motorbike = Motorbike("Honda", "Click", "MC123", 150)
    renter = Renter("Tony", 12345)

    print("=== Created Objects ===")
    print(car)
    print(electric_car)
    print(motorbike)
    print(f"Renter: {renter.name}, License: {renter.license_no}")

    print("\n=== Rent and Return ===")
    car.rent()
    renter.rented.append(car)
    print(car)

    car.return_vehicle()
    renter.rented.remove(car)
    print(car)

    print("\n=== Validation ===")
    try:
        Renter("", 100)
    except ValueError as error:
        print("Caught:", error)

    try:
        Renter("Alex", 0)
    except ValueError as error:
        print("Caught:", error)

    try:
        renter.name = ""
    except ValueError as error:
        print("Caught:", error)

    try:
        renter.license_no = -5
    except ValueError as error:
        print("Caught:", error)

    print("\n=== Polymorphism ===")
    vehicles = [car, electric_car, motorbike]
    for vehicle in vehicles:
        print(vehicle)


if __name__ == "__main__":
    main()
