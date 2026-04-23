from other import is_plate_unique, validate_plate, save_cars


def update_car(cars):
    print("\nИЗМЕНЕНИЕ ЗАПИСИ")
    if not cars:
        print("Нет записей для изменения.")
        return

    try:
        car_id = int(input("Введите ID автомобиля для изменения: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    # Поиск автомобиля по ID
    car_to_update = None
    for car in cars:
        if car["id"] == car_id:
            car_to_update = car
            break

    if not car_to_update:
        print(f"Автомобиль с ID {car_id} не найден!")
        return

    print(
        f"\nТекущие данные: {car_to_update['brand']} {car_to_update['model']}, {car_to_update['year']} г., {car_to_update['color']}, номер: {car_to_update['plate']}")
    print("\nОставьте поле пустым, чтобы не изменять:")

    new_brand = input(f"Новая марка ({car_to_update['brand']}): ").strip()
    new_model = input(f"Новая модель ({car_to_update['model']}): ").strip()
    new_year = input(f"Новый год ({car_to_update['year']}): ").strip()
    new_color = input(f"Новый цвет ({car_to_update['color']}): ").strip()

    # Ввод нового номера с проверками
    print(f"\nТекущий номер: {car_to_update['plate']}")
    new_plate = input("Новый номер (оставьте пустым для сохранения текущего): ").strip().upper()

    if new_plate:
        if not validate_plate(new_plate):
            print("Номер должен содержать 4-12 символов!")
            return
        if not is_plate_unique(cars, new_plate, car_id):
            print("Автомобиль с таким номером уже существует!")
            return
        car_to_update["plate"] = new_plate

    if new_brand:
        car_to_update["brand"] = new_brand
    if new_model:
        car_to_update["model"] = new_model
    if new_year:
        car_to_update["year"] = new_year
    if new_color:
        car_to_update["color"] = new_color

    save_cars(cars)
    print(f"Автомобиль с ID {car_id} успешно обновлен!")