from create_car_func import create_car
from delete_car_func import delete_car
from other import load_cars, show_menu
from read_cars_func import read_cars
from update_car_func import update_car

cars = load_cars()

while True:
    show_menu()
    choice = input("Выберите действие (1-5): ").strip()

    if choice == "1":
        create_car(cars)
    elif choice == "2":
        read_cars(cars)
    elif choice == "3":
        update_car(cars)
    elif choice == "4":
        delete_car(cars)
    elif choice == "5":
        print("\nПрограмма завершена.")
        break
    else:
        print("Ошибка: неверный выбор. Пожалуйста, выберите от 1 до 5.")