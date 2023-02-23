import random

MIN_ROW_COUNT = 5
MAX_ROW_COUNT = 30

MIN_COLUMN_COUNT = 5
MAX_COLUMN_COUNT = 30

MIN_MINE_COUNT = 1
MAX_MINE_COUNT = 800


class MinesweeperCell:
    #   closed, opened, flagged, questioned

    mark_sequence = ['closed', 'flagged']

    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.state = 'closed'
        self.mined = False
        self.counter = 0

    def next_mark(self):
        if self.state in self.mark_sequence:
            state_index = self.mark_sequence.index(self.state)
            self.state = self.mark_sequence[(state_index + 1) % len(self.mark_sequence)]

    def open(self):
        if self.state != 'flagged':
            self.state = 'opened'


class MinesweeperModel:
    def __init__(self, row_count=15, column_count=15, mine_count=15):
        self.start_game()

    def start_game(self, row_count=15, column_count=15, mine_count=15):
        if row_count in range(MIN_ROW_COUNT, MAX_ROW_COUNT + 1):
            self.row_count = row_count

        if column_count in range(MIN_COLUMN_COUNT, MAX_COLUMN_COUNT + 1):
            self.column_count = column_count

        if mine_count < self.row_count * self.column_count:
            if mine_count in range(MIN_MINE_COUNT, MAX_MINE_COUNT + 1):
                self.mine_count = mine_count
        else:
            self.mine_count = self.row_count * self.column_count - 1

        self.first_step = True
        self.game_over = False
        self.cells_table = []
        for row in range(self.row_count):
            cells_row = []
            for column in range(self.column_count):
                cells_row.append(MinesweeperCell(row, column))
            self.cells_table.append(cells_row)

    def get_cell(self, row, column):
        if int(row) < 0 or int(column) < 0 or self.row_count <= row or self.column_count <= column:
            return None

        return self.cells_table[row][column]

    def is_win(self):
        for row in range(self.row_count):
            for column in range(self.column_count):
                cell = self.cells_table[row][column]
                if not cell.mined and (cell.state != 'opened' and cell.state != 'flagged'):
                    return False

        return True

    def is_game_over(self):
        return self.game_over

    def open_cell(self, row, column):
        cell = self.get_cell(row, column)
        if not cell:
            return

        cell.open()

        if cell.mined:
            self.game_over = True
            return

        if self.first_step:
            self.first_step = False
            self.generate_mines()

        cell.counter = self.count_mines_around_cell(row, column)
        if cell.counter == 0:
            neighbours = self.get_cell_neighbours(row, column)
            for n in neighbours:
                if n.state == 'closed':
                    self.open_cell(n.row, n.column)

    def next_cell_mark(self, row, column):
        cell = self.get_cell(row, column)
        if cell:
            cell.next_mark()

    def generate_mines(self):
        for i in range(self.mine_count):
            while True:
                row = random.randint(0, self.row_count - 1)
                column = random.randint(0, self.column_count - 1)
                cell = self.get_cell(row, column)
                if not cell.state == 'opened' and not cell.mined:
                    cell.mined = True
                    break

    def count_mines_around_cell(self, row, column):
        neighbours = self.get_cell_neighbours(row, column)
        return sum(1 for n in neighbours if n.mined)

    def get_cell_neighbours(self, row, column):
        neighbours = []
        for r in range(row - 1, row + 2):
            neighbours.append(self.get_cell(r, column - 1))
            if r != row:
                neighbours.append(self.get_cell(r, column))
            neighbours.append(self.get_cell(r, column + 1))

        return filter(lambda n: n is not None, neighbours)
