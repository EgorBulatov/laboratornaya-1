# TODO: Подробно описать три произвольных класса


class Table:
    """
    Класс для описания стола.
    """

    def __init__(self, material: str, length: float, width: float):
        """
        Инициализация объекта стола.

        :param material: Материал стола (например, "дерево", "металл", "пластик").
        :param length: Длина стола в метрах. Должна быть больше 0.
        :param width: Ширина стола в метрах. Должна быть больше 0.
        :raises ValueError: Если длина или ширина не удовлетворяют условиям.
        """
        if length <= 0 or width <= 0:
            raise ValueError("Длина и ширина должны быть больше 0.")
        self.material = material
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        """
        Рассчитывает площадь стола.

        :return: Площадь стола в квадратных метрах.
        Пример:
        >>> table = Table("дерево", 2.0, 1.0)
        >>> table.calculate_area()
        2.0
        """
        return self.length * self.width

    def change_material(self, new_material: str) -> None:
        """
        Изменяет материал стола.

        :param new_material: Новый материал стола.
        Пример:
        >>> table = Table("дерево", 2.0, 1.0)
        >>> table.change_material("металл")
        >>> table.material
        'металл'
        """
        self.material = new_material

    def is_suitable(self, room_area: float) -> bool:
        """
        Проверяет, подходит ли стол для комнаты с указанной площадью.

        :param room_area: Площадь комнаты в квадратных метрах.
        :return: True, если площадь комнаты больше площади стола, иначе False.
        :raises ValueError: Если площадь комнаты <= 0.
        Пример:
        >>> table = Table("дерево", 2.0, 1.0)
        >>> table.is_suitable(5.0)
        True
        """
        if room_area <= 0:
            raise ValueError("Площадь комнаты должна быть больше 0.")
        return room_area > self.calculate_area()


class Tree:
    """
    Класс для описания дерева.
    """

    def __init__(self, species: str, height: float):
        """
        Инициализация дерева.

        :param species: Вид дерева (например, "дуб", "сосна").
        :param height: Высота дерева в метрах. Должна быть больше 0.
        :raises ValueError: Если высота не удовлетворяет условиям.
        """
        if height <= 0:
            raise ValueError("Высота дерева должна быть больше 0.")
        self.species = species
        self.height = height

    def grow(self, years: int, growth_per_year: float = 0.5) -> None:
        """
        Увеличивает высоту дерева в зависимости от количества лет.

        :param years: Количество лет. Должно быть >= 0.
        :param growth_per_year: Рост в метрах за год. По умолчанию 0.5 м.
        :raises ValueError: Если годы меньше 0 или рост отрицательный.
        Пример:
        >>> tree = Tree("дуб", 5.0)
        >>> tree.grow(3)
        >>> tree.height
        6.5
        """
        if years < 0 or growth_per_year < 0:
            raise ValueError("Годы и рост за год должны быть неотрицательными.")
        self.height += years * growth_per_year

    def is_taller(self, other_tree_height: float) -> bool:
        """
        Проверяет, выше ли текущее дерево другого дерева.

        :param other_tree_height: Высота другого дерева.
        :return: True, если текущее дерево выше, иначе False.
        :raises ValueError: Если высота другого дерева <= 0.
        Пример:
        >>> tree = Tree("дуб", 5.0)
        >>> tree.is_taller(4.0)
        True
        """
        if other_tree_height <= 0:
            raise ValueError("Высота другого дерева должна быть больше 0.")
        return self.height > other_tree_height


class Stack:
    """
    Класс для описания стека.
    """

    def __init__(self, max_size: int = 40, name: str = "DefaultStack"):
        """
        Инициализация стека.

        :param max_size: Максимальное количество элементов в стеке. Должно быть больше 0.
        :param name: Имя стека для идентификации.
        :raises ValueError: Если max_size <= 0.
        """
        if max_size <= 0:
            raise ValueError("Максимальный размер должен быть больше 0.")
        self.items = []
        self.max_size = max_size
        self.name = name

    def push(self, item: int) -> None:
        """
        Добавляет элемент в стек.

        :param item: Элемент, который нужно добавить.
        :raises OverflowError: Если стек переполнен.
        Пример:
        >>> stack = Stack(max_size=2, name="MyStack")
        >>> stack.push(1)
        >>> stack.push(2)
        >>> stack.push(3)
        Traceback (most recent call last):
        ...
        OverflowError: Невозможно добавить элемент: стек переполнен.
        """
        if len(self.items) >= self.max_size:
            raise OverflowError("Невозможно добавить элемент: стек переполнен.")
        self.items.append(item)

    def pop(self) -> int:
        """
        Удаляет и возвращает верхний элемент стека.

        :return: Верхний элемент стека.
        :raises IndexError: Если стек пуст.
        Пример:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.pop()
        1
        """
        if not self.items:
            raise IndexError("Невозможно удалить элемент из пустого стека.")
        return self.items.pop()

    def peek(self) -> int:
        """
        Возвращает верхний элемент стека без удаления.

        :return: Верхний элемент стека.
        :raises IndexError: Если стек пуст.
        Пример:
        >>> stack = Stack()
        >>> stack.push(1)
        >>> stack.peek()
        1
        """
        if not self.items:
            raise IndexError("Невозможно просмотреть верхний элемент пустого стека.")
        return self.items[-1]