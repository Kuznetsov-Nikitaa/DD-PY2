import doctest


class Planet:
    def __init__(self, name: str, distance_to_the_surface: (int, float), presence_of_life: bool):
        """
        Создание и подготовка к работе объекта "Планета"

        :param name: Название планеты
        :param distance_to_the_surface: Расстояние до планеты, млн км
        :param presence_of_life: Наличие жизни

        Пример:
        >>> mars = Planet("Марс", 3389.5, False)
        """
        if not isinstance(name, str):
            raise TypeError('Название планеты должно быть типа str')
        self.name = name

        if not isinstance(distance_to_the_surface, (int, float)):
            raise TypeError('Расстояние до поверхности должно быть типа int или float')
        if distance_to_the_surface < 0:
            raise ValueError('Расстояние до поверхности не может иметь отрицательное значение')
        self.distance_to_the_surface = distance_to_the_surface

        if not isinstance(presence_of_life, bool):
            raise TypeError('Наличие жизни должно определяться переменными типа bool')
        self.presence_of_life = presence_of_life

    def make_a_warp_jump(self, distance: (int, float)) -> None:
        """
        Совершение варп-прыжка

        :param distance: Длина варп-прыжка, млн км
        :raise ValueError: Если длина варп-прыжка превышает расстояние до поверхности, возвращается ошибка

        Пример:
        >>> mars = Planet("Марс", 3389.5, False)
        >>> mars.make_a_warp_jump(1000)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина варп-прыжка должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина варп-прыжка не может быть отрицательной')
        if distance > self.distance_to_the_surface:
            raise ValueError('(!) Угроза столкновения: длина варп-прыжка не может превышать расстояние до поверхности')
        self.distance_to_the_surface -= distance
        if self.distance_to_the_surface > 0:
            # print(f"Прыжок выполнен, оставшееся расстояние до планеты {self.name}:"
            # f" {self.distance_to_the_surface} млн км")
            ...
        elif self.distance_to_the_surface == 0:
            # print(f'Посадка выполнена! Вы на поверхности планеты {self.name}')
            ...

    def terraform(self) -> None:
        """
        Терраформирование планеты

        :raise ValueError: Если расстояние до поверхности планеты больше нуля, возвращается ошибка
        :raise ValueError: Если на планете уже есть жизнь, возвращается ошибка

        Пример:
        >>> mars = Planet("Марс", 0, False)
        >>> mars.terraform()
        """
        if self.distance_to_the_surface > 0:
            raise ValueError(f'Чтобы терраформировать планету {self.name}, необходимо находиться на ней')
        if self.presence_of_life is True:
            raise ValueError(f'На планете {self.name} уже есть жизнь')
        self.presence_of_life = True
        # print(f'Планета {self.name} успешно терраформирована, теперь на ней есть жизнь...')


class FruitTree:
    def __init__(self, name: str, growth_time: (int, float)):
        """
        Создание и подготовка к работе объекта "Фруктовое дерево"

        :param name: Название дерева
        :param growth_time: Время роста дерева до появления плодов, лет

        Пример:
        >>> apple = FruitTree("Яблоня", 2)
        """
        if not isinstance(name, str):
            raise TypeError('Название дерева должно быть типа str')
        self.name = name

        if not isinstance(growth_time, (int, float)):
            raise TypeError('Время роста дерева должен быть типа int или float')
        if growth_time <= 0:
            raise ValueError('Время роста дерева должно быть положительным числом')

    def estimate_age(self) -> (int, float):
        """
        Оценка возраста дерева

        :return: (int, float)

        Пример:
        >>> apple = FruitTree("Яблоня", 2)
        >>> apple.estimate_age()
        """
        ...

    def shake_the_tree(self) -> None:
        """
        Потрясти дерево, чтобы собрать плоды

        :return: None

        Пример:
        >>> apple = FruitTree("Яблоня", 2)
        >>> apple.shake_the_tree()
        """
        ...


class Flat:
    def __init__(self, square: (int, float), number_of_rooms: int, number_of_inhabitants: int):
        """
        Создание и подготовка к работе объекта "Квартира"

        :param square: Площадь, м^2
        :param number_of_rooms: Число комнат
        :param number_of_inhabitants: Число жителей

        :raise ValueError: Если площадь квартиры меньше или равна нулю, возвращается ошибка
        :raise ValueError: Если число комнат меньше или равно нулю, возвращается ошибка
        :raise ValueError: Если число жителей меньше нуля, возвращается ошибка

        Пример:
        >>> flat = Flat(30, 2, 2)
        """
        if not isinstance(square, (int, float)):
            raise TypeError('Площадь квартиры должна быть типа int или float')
        if square <= 0:
            raise ValueError('Площадь квартиры должна быть положительным числом')
        self.square = square

        if not isinstance(number_of_rooms, int):
            raise TypeError('Число комнат должно быть типа int')
        if number_of_rooms <= 0:
            raise ValueError('Число комнат должно быть положительным')
        self.number_of_rooms = number_of_rooms

        if not isinstance(number_of_inhabitants, int):
            raise TypeError('Число жителей должно быть типа int')
        if number_of_inhabitants < 0:
            raise ValueError('Число жителей не может быть отрицательным')
        self.number_of_inhabitants = number_of_inhabitants

    def settle_a_resident(self, value: int) -> None:
        """
        Заселение жителей

        :param value: Число заселяемых жителей
        :return: None

        :raise ValueError: Если число новосельцев меньше нуля, возвращается ошибка
        """
        if not isinstance(value, int):
            raise TypeError('Число новосельцев должно быть типа int')
        if value <= 0:
            raise ValueError('Число новосельцев должно быть положительным')
        ...

    def evict_a_resident(self, value: int) -> None:
        """
        Выселение жителей

        :param value: Число выселяемых жителей
        :return: None

        :raise ValueError: Если число выселенцев меньше нуля, возвращается ошибка
        """
        if not isinstance(value, int):
            raise TypeError('Число выселенцев должно быть типа int')
        if value <= 0:
            raise ValueError('Число выселенцев должно быть положительным')
        ...


if __name__ == "__main__":
    doctest.testmod()
