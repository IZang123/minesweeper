import random


class Minesweeper:
    """Minesweeper Class
    =================

    This module contains the implementation of the Minesweeper game.

    :class:`Minesweeper` Class
    --------------------------

    .. autoclass:: Minesweeper
        :members:
        :undoc-members:
        :show-inheritance:
        :special-members: __init__, create_minefield, set_bombs, set_values, nbors, how_to, check_over, show_bombs, play_game

        Minesweeper class provides methods for creating and playing the Minesweeper game.

        .. autoattribute:: field_attribute
            :annotation:

            The size of the minefield, both in terms of rows and columns.

        .. autoattribute:: bombs_qty
            :annotation:

            The number of bombs on the minefield.

        .. autoattribute:: numbers
            :annotation:

            A 2D list representing the numbers on the minefield.

        .. autoattribute:: values_of_bombs
            :annotation:

            A 2D list representing the values of cells on the minefield.

        .. autoattribute:: flags
            :annotation:

            A list to store the positions of flags on the minefield.

    Methods
    -------

    .. automethod:: create_minefield()
        :annotation:

        Display the current state of the minefield.

    .. automethod:: set_bombs()
        :annotation:

        Set random positions for bombs on the minefield.

    .. automethod:: set_values()
        :annotation:

        Set values for each cell on the minefield based on the bomb positions.

    .. automethod:: nbors(r, col)
        :annotation:

        Recursively explore neighboring cells of the specified cell.

    .. automethod:: how_to()
        :annotation:

        Display instructions on how to play the Minesweeper game.

    .. automethod:: check_over()
        :annotation:

        Check if the game is over by comparing the opened cells with the total number of cells.

    .. automethod:: show_bombs()
        :annotation:

        Reveal the bomb positions on the minefield.

    .. automethod:: play_game()
        :annotation:

        Start and manage the Minesweeper game.

    Usage
    -----

    To use the Minesweeper class, create an instance and call the :meth:`play_game` method.

    Example
    -------

    .. code-block:: python

        if __name__ == "__main__":
            minesweeper = Minesweeper(5, 3)
            minesweeper.play_game()"""

    def __init__(self, field_attribute, bombs_qty):
        self.field_attribute = field_attribute
        self.bombs_qty = bombs_qty
        self.numbers = [[0 for y in range(field_attribute)] for x in range(field_attribute)]
        self.values_of_bombs = [[' ' for y in range(field_attribute)] for x in range(field_attribute)]
        self.flags = []

    def create_minefield(self):
        print()
        print("\t\t\t   САПЕР\n")
        st = "   "
        for i in range(self.field_attribute):
            st = st + "     " + str(i + 1)
        print(st)
        for r in range(self.field_attribute):
            st = "     "
            if r == 0:
                for col in range(self.field_attribute):
                    st = st + "______"
                print(st)
            st = "     "
            for col in range(self.field_attribute):
                st = st + "|     "
            print(st + "|")
            st = "  " + str(r + 1) + "  "
            for col in range(self.field_attribute):
                st = st + "|  " + str(self.values_of_bombs[r][col]) + "  "
            print(st + "|")
            st = "     "
            for col in range(self.field_attribute):
                st = st + "|_____"
            print(st + '|')
        print()

    def set_bombs(self):
        count = 0
        while count < self.bombs_qty:
            val = random.randint(0, self.field_attribute * self.field_attribute - 1)
            r = val // self.field_attribute
            col = val % self.field_attribute
            if self.numbers[r][col] != -1:
                count = count + 1
                self.numbers[r][col] = -1

    def set_values(self):
        for r in range(self.field_attribute):
            for col in range(self.field_attribute):
                if self.numbers[r][col] == -1:
                    continue
                if r > 0 and self.numbers[r - 1][col] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if r < self.field_attribute - 1 and self.numbers[r + 1][col] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if col > 0 and self.numbers[r][col - 1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if col < self.field_attribute - 1 and self.numbers[r][col + 1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if r > 0 and col > 0 and self.numbers[r - 1][col - 1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if r > 0 and col < self.field_attribute - 1 and self.numbers[r - 1][col + 1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if r < self.field_attribute - 1 and col > 0 and self.numbers[r + 1][col - 1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1
                if r < self.field_attribute - 1 and col < self.field_attribute - 1 and self.numbers[r + 1][col + 1] == -1:
                    self.numbers[r][col] = self.numbers[r][col] + 1

    def nbors(self, r, col):
        if [r, col] not in self.vis:
            self.vis.append([r, col])
            if self.numbers[r][col] == 0:
                self.values_of_bombs[r][col] = self.numbers[r][col]
                if r > 0:
                    self.nbors(r - 1, col)
                if r < self.field_attribute - 1:
                    self.nbors(r + 1, col)
                if col > 0:
                    self.nbors(r, col - 1)
                if col < self.field_attribute - 1:
                    self.nbors(r, col + 1)
                if r > 0 and col > 0:
                    self.nbors(r - 1, col - 1)
                if r > 0 and col < self.field_attribute - 1:
                    self.nbors(r - 1, col + 1)
                if r < self.field_attribute - 1 and col > 0:
                    self.nbors(r + 1, col - 1)
                if r < self.field_attribute - 1 and col < self.field_attribute - 1:
                    self.nbors(r + 1, col + 1)

    def how_to(self):
        print("Как играть:")
        print("1. Введи номер СТРОЧКИ и номер СТОЛБЦА (именно в таком порядке) через пробел, чтобы открыть клетку. Например: 2 5")
        print("2. Введи номер СТРОЧКИ, номер СТОЛБЦА и ЗАГЛАВНУЮ АНГЛИЙСКУЮ БУКВУ F (именно в таком порядке) через пробел, чтобы поставить флаг. Пример: 2 5 F")

    def check_over(self):
        count = 0
        for r in range(self.field_attribute):
            for col in range(self.field_attribute):
                if self.values_of_bombs[r][col] != ' ' and self.values_of_bombs[r][col] != 'F':
                    count += 1
        return count == self.field_attribute * self.field_attribute - self.bombs_qty

    def show_bombs(self):
        for r in range(self.field_attribute):
            for col in range(self.field_attribute):
                if self.numbers[r][col] == -1:
                    self.values_of_bombs[r][col] = 'M'

    def play_game(self):
        while True:
            print("Добро пожаловать в игру сапер!")
            print("Выбери уровнь сложности:")
            print("1. Новичок - поле 5x5 и 3 мины")
            print("2. Средний - поле 7x7 и 7 мин")
            print("3. Сложный - поле 9x9 и 10 мин")
            while True:
                try:
                    difficulty = int(input("Для выбора уровня сложности введите соответствующее число (1-3): "))
                    if difficulty == 1:
                        self.field_attribute = 5
                        self.bombs_qty = 3
                        break
                    elif difficulty == 2:
                        self.field_attribute = 7
                        self.bombs_qty = 7
                        break
                    elif difficulty == 3:
                        self.field_attribute = 9
                        self.bombs_qty = 10
                        break
                    else:
                        print("Неверно выбран уровень сложности. Пробуй еще раз.")
                except ValueError:
                    print("Уровень сложности выбирается с помощью числа от 1 до 3")

            self.numbers = [[0 for y in range(self.field_attribute)] for x in range(self.field_attribute)]
            self.values_of_bombs = [[' ' for y in range(self.field_attribute)] for x in range(self.field_attribute)]
            self.flags = []
            self.vis = []  # Add this line to reset vis

            self.set_bombs()
            self.set_values()
            self.how_to()
            over = False

            while not over:
                self.create_minefield()
                inp = input("Введите номер строки, затем пробел и номер столбца. = ").split()

                if len(inp) == 2:
                    try:
                        val = list(map(int, inp))
                    except ValueError:
                        print("НЕВЕРНЫЙ ВВОД!")
                        self.how_to()
                        continue

                elif len(inp) == 3:
                    if inp[2] != 'F' and inp[2] != 'f':
                        print("НЕВЕРНЫЙ ВВОД!")
                        self.how_to()
                        continue

                    try:
                        val = list(map(int, inp[:2]))
                    except ValueError:
                        print("НЕВЕРНЫЙ ВВОД!")
                        self.how_to()
                        continue

                    if val[0] > self.field_attribute or val[0] < 1 or val[1] > self.field_attribute or val[1] < 1:
                        print("НЕВЕРНЫЙ ВВОД!")
                        self.how_to()
                        continue

                    r = val[0] - 1
                    col = val[1] - 1

                    if [r, col] in self.flags:
                        print("Клетка уже помечена!")
                        continue

                    if self.values_of_bombs[r][col] != ' ':
                        print("Клетка уже открыта!")
                        continue

                    if len(self.flags) < self.bombs_qty:
                        print("Флаг установлен")
                        self.flags.append([r, col])
                        self.values_of_bombs[r][col] = 'F'
                        continue
                    else:
                        print("Флаги кончились!")
                        continue

                else:
                    print("Неверный ввод!")
                    self.how_to()
                    continue

                if val[0] > self.field_attribute or val[0] < 1 or val[1] > self.field_attribute or val[1] < 1:
                    print("Неверный ввод!")
                    self.how_to()
                    continue

                r = val[0] - 1
                col = val[1] - 1

                if [r, col] in self.flags:
                    self.flags.remove([r, col])

                if self.numbers[r][col] == -1:
                    self.values_of_bombs[r][col] = 'M'
                    self.show_bombs()
                    self.create_minefield()
                    print("Поражение. Ты встал на мину.")
                    over = True
                    continue

                elif self.numbers[r][col] == 0:
                    self.vis = []  # Add this line to reset vis
                    self.values_of_bombs[r][col] = '0'
                    self.nbors(r, col)

                else:
                    self.values_of_bombs[r][col] = self.numbers[r][col]

                if self.check_over():
                    self.show_bombs()
                    self.create_minefield()
                    print("Победа. Ты нашел все мины.")
                    over = True
                    continue
            again = input("Чтобы начать заново напиши любой символ, чтобы закрыть программу напиши '00': ")
            if again == "00":
                print("Пока!")
                break

if __name__ == "__main__":
    minesweeper = Minesweeper(5, 3)
    minesweeper.play_game()
