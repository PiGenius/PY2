import doctest
from typing import Union


class Window:
    def __init__(self, is_opened: bool, is_clean: bool, colour: str):
        """
        Создание и подготовка к работе объекта "Окно"

        :param is_opened: состояние окна - True открыто, False закрыто
        :param is_clean: состояние окна - True чистое, False грязное
        :param colour: цвет окна - 1 из 4: прозрачный, красный, зеленый, синий; регистр не важен

        Пример:
        >>> window = Window(False, True, 'Прозрачный')
        """
        self.is_opened = None
        self.init_is_opened(is_opened)

        self.is_clean = None
        self.init_is_clean(is_clean)

        self.colour = None
        self.init_colour(colour)

    def init_is_opened(self, is_opened: bool):
        """
        Инициализация атрибута is_opened - является ли стакан пустым

        :param is_opened: задаваемое состояние окна
        """
        if not isinstance(is_opened, bool):
            raise TypeError('Состояние окна должно быть типа bool - открыто True, закрыто False')
        self.is_opened = is_opened

    def init_is_clean(self, is_clean: bool):
        """
        Инициализация атрибута is_clean - является ли окно чистым

        :param is_clean: задаваемое состояние окна
        """
        if not isinstance(is_clean, bool):
            raise TypeError('Состояние окна должно быть типа bool - чистое True, грязное False')
        self.is_clean = is_clean

    def init_colour(self, colour: str):
        """
        Инициализация атрибута colour - цвет окна

        :param colour: задаваемый цвт окна
        """
        if not isinstance(colour, str):
            raise TypeError('Цвет окна должен быть типа str')
        if colour.lower() not in ['прозрачный', 'красный', 'зеленый', 'синий']:
            raise ValueError('Цвет окна может быть 1 из 4: прозрачный, красный, зеленый, синий')
        self.colour = colour

    def open(self):
        """
        Открыть окно

        Пример:
        >>> window = Window(False, False, 'Прозрачный')
        >>> window.open()
        """
        if self.is_opened:
            raise ValueError('Окно уже открыто!')
        ...

    def clean(self):
        """
        Помыть окно

        Пример:
        >>> window = Window(False, True, 'Прозрачный')
        >>> window.clean()
        """

        ...

    def change_colour(self, colour: str):
        """
        Сменить цвет окна на 1 из 4: прозрачный, красный, зеленый, синий; регистр не важен

        :param colour: желаемый цвет окна

        Пример:
        >>> window = Window(False, True, 'Прозрачный')
        >>> window.change_colour('Красный')
        """
        ...


class Car:
    def __init__(self, oil_amount: Union[int, float], oil_consumption: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Машина"

        :param oil_amount: текущее количество топлива в баке
        :param oil_consumption: потребление топлива на единицу пути

        Пример:
        >>> car = Car(100, 10)
        """
        self.oil_amount = None
        self.init_oil_amount(oil_amount)

        self.oil_consumption = None
        self.init_oil_consumption(oil_consumption)

    def init_oil_amount(self, oil_amount: Union[int, float]):
        """
        Инициализация атрибута oil_amount - текущее количество топлива

        :param oil_amount: текущее количество топлива
        """
        if not isinstance(oil_amount, (int, float)):
            raise TypeError('Количество топлива должно быть типа int или float')
        if oil_amount < 0:
            raise ValueError('Количество топлива должно быть не меньше 0')
        self.oil_amount = oil_amount

    def init_oil_consumption(self, oil_consumption: Union[int, float]):
        """
        Инициализация атрибута oil_consumptio - потребление топлива на единицу пути

        :param oil_consumption: потребление топлива на единицу пути
        """
        if not isinstance(oil_consumption, (int, float)):
            raise TypeError('Потребление топлива должно быть типа int или float')
        if oil_consumption <= 0:
            raise ValueError('Потребление топлива должно быть больше 0')
        self.oil_consumption = oil_consumption

    def add_oil(self, extra_oil: Union[int, float]):
        """
        Добавить топлива в бак

        :param extra_oil: дополнительное топливо

        Пример:
        >>> car = Car(100, 10)
        >>> car.add_oil(10)
        """
        if not isinstance(extra_oil, (int, float)):
            raise TypeError('Добавленное топливо должно быть типа int или float')
        if extra_oil < 0:
            raise ValueError('Добавленное топливо должно быть не меньше 0')
        ...

    def make_trip(self, distance: Union[int, float]):
        """
        Совершить поездку длиной distance, соответственно потратив некоторое количество топлива

        :param distance: длина пути

        Пример:
        >>> car = Car(100, 10)
        >>> car.make_trip(100)
        """
        if not isinstance(distance, (int, float)):
            raise TypeError('Длина пути должна быть типа int или float')
        if distance < 0:
            raise ValueError('Длина пути должна быть не меньше 0')
        ...

    def get_current_oil_level(self) -> Union[int, float]:
        """
        Узнать текущий объем топлива

        :return: текущий объем топлива

        Пример:
        >>> car = Car(100, 10)
        >>> car.get_current_oil_level()
        100
        """
        return self.oil_amount


class Hammer:
    def __init__(self, material: str, handle_length: Union[int, float]):
        """
        Создание и подготовка к работе объекта "Молоток"

        :param material: материал молотка 1 из 3 - железный, резиновый, деревянный; регистр не важен
        :param handle_length: длина ручки

        Пример:
        >>> hammer = Hammer('Железный', 30)
        """
        self.material = None
        self.init_material(material)

        self.handle_length = None
        self.init_handle_length(handle_length)

    def init_material(self, material: str):
        """
        Инициализация атрибута material - материал молотка 1 из 3 - железный, резиновый, деревянный; регистр не важен

        :param material:  материал молотка
        """
        if not isinstance(material, str):
            raise TypeError('Материал молотка должен быть типа str')
        if material.lower() not in ['железный', 'резиновый', 'деревянный']:
            raise ValueError('Материал молотка может быть 1 из 3: железный, резиновый, деревянный')
        self.material = material

    def init_handle_length(self, handle_length: Union[int, float]):
        """
        Инициализация атрибута handle_length - длина молотка

        :param handle_length: длина молотка
        """
        if not isinstance(handle_length, (int, float)):
            raise TypeError('Длина ручки должна быть типа int или float')
        if handle_length < 10:
            raise ValueError('Длина ручки должна быть не меньше 10')
        self.handle_length = handle_length

    def hammer_nail(self):
        """
        Забить гвоздь. Можно только железным молотком

        Пример:
        >>> hammer = Hammer('Железный', 30)
        >>> hammer.hammer_nail()
        """
        if self.material.lower() != 'железный':
            raise ValueError('Для забивания гвоздей нужен железный молоток')
        ...

    def pull_out_nail(self):
        """
        Вытащить гвоздь. Можно только железным молотком

        Пример:
        >>> hammer = Hammer('Железный', 30)
        >>> hammer.pull_out_nail()
        """
        if self.material.lower() != 'железный':
            raise ValueError('Для вытаскивания гвоздей нужен железный молоток')
        ...

    def extend_handle(self, length: Union[int, float]):
        """
        Удлинить ручку на длину length

        :param length: на сколько удлинить

        Пример:
        >>> hammer = Hammer('Железный', 30)
        >>> hammer.extend_handle(10)
        """
        if not isinstance(length, (int, float)):
            raise TypeError('Удлинение ручки должно быть типа int или float')
        if length <= 0:
            raise ValueError('Удлинение ручки должно быть больше 0')
        ...


if __name__ == "__main__":
    doctest.testmod()

