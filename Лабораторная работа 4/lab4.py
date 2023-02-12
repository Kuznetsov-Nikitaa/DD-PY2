import doctest

if __name__ == "__main__":
    class Mashroom:
        """Базовый класс гриб"""
        def __init__(self, name: str):
            """
            Создание и подготовка к работе объекта "Гриб"

            :param name: Название гриба

            Пример:
            >>> unknown_mashroom = Mashroom('Опёнок (вроде)')
            """
            self.name = name

        def __str__(self) -> str:
            """
            Магический метод __str__

            :return: str

            Пример:
            >>> unknown_mashroom = Mashroom('Опёнок (вроде)')
            >>> print(unknown_mashroom)
            """
            return f"Гриб {self.name}"

        def __repr__(self) -> str:
            """
            Магический метод __repr__

            :return: str

            Пример:
            >>> unknown_mashroom = Mashroom('Опёнок (вроде)')
            >>> print(repr(unknown_mashroom))
            """
            return f"{self.__class__.__name__}(name={self.name!r})"

        def can_i_eat_this(self) -> None:
            """
            Метод, определяющий, можно ли есть этот гриб.

            :return: None

            Пример:
            >>> unknown_mashroom = Mashroom('Опёнок (вроде)')
            >>> unknown_mashroom.can_i_eat_this()
            """
            ...
            print("На свой страх и риск...")

        def perform_laplace_transformation(self) -> None:
            """
            Метод, выполняющий преобразование Лапласа.
            Использовать только когда уже съел гриб.

            :return: None

            Пример:
            >>> unknown_mashroom = Mashroom('Опёнок (вроде)')
            >>> unknown_mashroom.perform_laplace_transformation()
            """
            ...

    class FlyAgaric(Mashroom):
        """Дочерний класс мухомор"""
        def __init__(self, name: str, number_of_spots: int):
            """
            Создание и подготовка к работе объекта "Мухомор"

            :param name: Название мухомора
            :param number_of_spots: Количество пятнышек на мухоморе

            Пример:
            >>> fly_agaric = FlyAgaric('Мухомор', 26)
            """
            super().__init__(name)
            self.number_of_spots = number_of_spots

        def __repr__(self) -> str:
            """
            Магический метод __repr__
            Обоснование перегрузки: для инициализации экземпляра данного класса требуется указание значения
            нового атрибута.

            :return: str

            Пример:
            >>> fly_agaric = FlyAgaric('Мухомор', 26)
            >>> print(repr(fly_agaric))
            """
            return f"{self.__class__.__name__}(name={self.name!r}, number_of_spots={self.number_of_spots})"

        def can_i_eat_this(self) -> None:
            """
            Метод, определяющий, можно ли есть мухомор.
            Обоснование перегрузки: грибы есть можно, а вот мухоморы не ем и Вам не советую.

            :return: None

            Пример:
            >>> fly_agaric = FlyAgaric('Мухомор', 26)
            >>> fly_agaric.can_i_eat_this()
            """
            ...
            print("Мухомор - ядовитый гриб")

    mashroom = Mashroom('Лисичка')
    print(mashroom)
    print(repr(mashroom))
    mashroom.can_i_eat_this()
    mashroom1 = FlyAgaric('похож на мухомор', 32)
    print(mashroom1)
    print(repr(mashroom1))
    mashroom1.can_i_eat_this()
    doctest.testmod()
