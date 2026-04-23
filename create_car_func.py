from other import validate_plate, is_plate_unique, get_next_id, save_cars

def create_car(cars):
    print("\nСОЗДАНИЕ НОВОЙ ЗАПИСИ")
    brand = input("Введите марку авто: ").strip()
    model = input("Введите модель авто: ").strip()
    year = input("Введите год выпуска: ").strip()
    color = input("Введите цвет авто: ").strip()

    # Ввод номера авто с проверкой
    while True:
        plate = input("Введите номер авто (например: А123ВВ77): ").strip().upper()
        if not plate:
            print("Номер авто не может быть пустым!")
            continue
        if not validate_plate(plate):
            print("Номер должен содержать 4-12 символов!")
            continue
        if not is_plate_unique(cars, plate):
            print("Автомобиль с таким номером уже существует!")
            continue
        break

    if not brand or not model:
        print("Ошибка: марка и модель не могут быть пустыми!")
        return

    car = {
        "id": get_next_id(cars),
        "brand": brand,
        "model": model,
        "year": year,
        "color": color,
        "plate": plate
    }
    cars.append(car)
    save_cars(cars)
    print(f"Автомобиль успешно добавлен с ID: {car['id']} и номером: {car['plate']}")