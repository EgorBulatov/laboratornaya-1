from task_1 import Table, Tree, Stack

if __name__ == "__main__":
    # Инстанцирование класса Table
    table = Table(material="дерево", length=2.0, width=1.5)

    # Инстанцирование класса Tree
    tree = Tree(species="дуб", height=5.0)

    # Инстанцирование класса Stack
    stack = Stack(2)


    try:
        # Попытка установить некорректный размер комнаты в методе is_suitable
        table.is_suitable(room_area=-10)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # Попытка увеличить высоту дерева с отрицательным количеством лет
        tree.grow(years=-3)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        # Попытка добавить элемент в стек, превышая максимальный размер
        stack.push(10)
        stack.push(20)
        stack.push(200)  # Этот вызов должен вызвать OverflowError
    except OverflowError:
        print('Ошибка: неправильные данные')
