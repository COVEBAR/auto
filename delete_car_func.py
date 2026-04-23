from other import save_cars

def delete_car(cars):
    print("\nУДАЛЕНИЕ ЗАПИСИ")
    if not cars:
        print("Нет записей для удаления.")
        return

    try:
        car_id = int(input("Введите ID автомобиля для удаления: "))
    except ValueError:
        print("Ошибка: ID должен быть числом!")
        return

    # Поиск автомобиля
    car_to_delete = None
    for car in cars:
        if car["id"] == car_id:
            car_to_delete = car
            break

    if not car_to_delete:
        print(f"Автомобиль с ID {car_id} не найден!")
        return

    print(
        f"\nАвтомобиль для удаления: {car_to_delete['brand']} {car_to_delete['model']}, номер: {car_to_delete['plate']}")
    confirm = input("Вы уверены, что хотите удалить эту запись? (да/нет): ").strip().lower()

    if confirm == "да":
        cars.remove(car_to_delete)
        save_cars(cars)
        print(f"Автомобиль с ID {car_id} и номером {car_to_delete['plate']} успешно удален!")
    else:
        print("Удаление отменено.")