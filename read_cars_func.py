def read_cars(cars):
    print("\nСПИСОК ВСЕХ АВТОМОБИЛЕЙ")
    if not cars:
        print("Нет записей об автомобилях.")
        return

    print(f"{'ID':<5} {'Марка':<12} {'Модель':<12} {'Год':<6} {'Цвет':<10} {'Номер':<15}")
    for car in cars:
        print(
            f"{car['id']:<5} {car['brand']:<12} {car['model']:<12} {car['year']:<6} {car['color']:<10} {car['plate']:<15}")
    print(f"Всего записей: {len(cars)}")