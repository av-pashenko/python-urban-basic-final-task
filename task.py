import csv


def read_file(filename: str) -> list[dict]:
    """Читает данные из CSV файла и преобразует их в список словарей.

    :param filename: Название файла, содержащего данные.
    :return: Список словарей с данными о домах.
    """
    with open(filename, encoding="utf-8") as f:
        housing_data = list(csv.DictReader(f))
    for h in housing_data:
        h["floor_count"] = int(h["floor_count"])
        h["population"] = int(h["population"])
        h["heating_value"] = float(h["heating_value"])
        h["area_residential"] = float(h["area_residential"])
    return housing_data


def classify_house(floor_count: int) -> str:
    """Классифицирует дом на основе количества этажей.

    Проверяет, является ли количество этажей целым числом и положительным значением.
    Возвращает категорию дома в зависимости от количества этажей.

    :param floor_count: Количество этажей в доме.
    :return: Категория дома в виде строки: "Малоэтажный", "Среднеэтажный" или
    "Многоэтажный".
    """
    if not isinstance(floor_count, int):
        error = "Количество этажей не целое число!"
        raise TypeError(error)
    if floor_count <= 0:
        error = "Количество этажей не положительное!"
        raise ValueError(error)
    low_to_med_floors_breakepoint = 5
    med_to_high_floors_breakepoint = 16
    if floor_count <= low_to_med_floors_breakepoint:
        return "Малоэтажный"
    if floor_count <= med_to_high_floors_breakepoint:
        return "Среднеэтажный"
    return "Многоэтажный"


def get_classify_houses(houses: list[dict]) -> list[str]:
    """Классифицирует дома на основе количества этажей.

    :param houses: Список словарей с данными о домах.
    :return: Список категорий домов.
    """
    return [classify_house(house["floor_count"]) for house in houses]


def get_count_house_categories(categories: list[str]) -> dict[str, int]:
    """Подсчитывает количество домов в каждой категории.

    :param categories: Список категорий домов.
    :return: Словарь с количеством домов в каждой категории.
    """
    categories_counted = {}
    for cat in categories:
        if cat in categories_counted:
            categories_counted[cat] += 1
        else:
            categories_counted[cat] = 1
    return categories_counted


def min_area_residential(houses: list[dict]) -> str:
    """Находит адрес дома с наименьшим ср. кол-вом м^2 жилплощади на одного жильца.

    :param houses: Список словарей с данными о домах.
    :return: Адрес дома с наименьшим средним количеством
    квадратных метров жилой площади на одного жильца.
    """
    min_avg_area = float("inf")
    min_addr = None
    for house in houses:
        curr_avg_area = house["area_residential"] / house["population"]
        if curr_avg_area < min_avg_area:
            min_avg_area = curr_avg_area
            min_addr = house["house_address"]
    return min_addr
