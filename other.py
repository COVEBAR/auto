import os

FILE_NAME = "cars.txt"


def load_cars():
    cars = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 6:  # Обновлено для 6 полей
                        car = {
                            "id": int(parts[0]),
                            "brand": parts[1],
                            "model": parts[2],
                            "year": parts[3],
                            "color": parts[4],
                            "plate": parts[5]  # Добавлен номер авто
                        }
                        cars.append(car)
    return cars


def save_cars(cars):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        for car in cars:
            file.write(f"{car['id']}|{car['brand']}|{car['model']}|{car['year']}|{car['color']}|{car['plate']}\n")


def validate_plate(plate):
    # Простой паттерн: буквы и цифры, 6-9 символов
    if plate and len(plate) >= 4 and len(plate) <= 12:
        return True
    return False


def get_next_id(cars):
    if not cars:
        return 1
    return max(car["id"] for car in cars) + 1


def is_plate_unique(cars, plate, exclude_id=None):
    for car in cars:
        if car["plate"].lower() == plate.lower() and car["id"] != exclude_id:
            return False
    return True

def show_menu():
    print("УЧЁТ АВТОМОБИЛЕЙ")
    print("1. Создать запись об авто")
    print("2. Просмотреть все записи")
    print("3. Изменить запись")
    print("4. Удалить запись")
    print("5. Выход")