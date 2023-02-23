import minesweeper_model


class MinesweeperView():
    def __init__(self, model, controller, parent=None):
        self.model = model
        self.controller = controller
        self.controller.set_view(self)


        #self.state_dict = {'closed': '#', 'flagged': '!', 'opened': '_'}
        #self.create_board()

        self.row_count = int(input("Enter row count for a game(5 to 30): "))
        self.model.row_count = self.row_count
        print("Rows count: ", self.row_count)

        self.column_count = int(input("Enter column count for a game(5 to 30): "))
        self.model.column_count = self.column_count
        print("Columns count: ", self.column_count)

        self.mine_count = int(input("Enter mine count for a game(1 to 800): "))
        self.model.mine_count = self.mine_count
        print("Mines count: ", self.mine_count)

    def create_board(self):
        print("\nNew game started!\n")
        self.sync_with_model()

    def sync_with_model(self):
        symbol_table = ''
        for i in range(int(self.model.row_count)):
            symbol_line = ''
            for j in range(int(self.model.column_count)):
                cell = self.model.cells_table[i][j]
                # symbol_line += self.state_dict[self.model.cells_table[i][j].state]
                if cell.state == 'closed':
                    symbol_line += '#'
                elif cell.state == 'opened':
                    if cell.counter > 0:
                        symbol_line += str(cell.counter)
                    elif cell.mined:
                        symbol_line += '*'
                    else:
                        symbol_line += '_'
                elif cell.state == 'flagged':
                    symbol_line += '!'
            symbol_table += symbol_line + '\n'
        print(symbol_table)

    def main_loop(self):
        while(True):
            #self.sync_with_model()
            command = input("Введіть команду: ")
            self.parse_command(command)

    def parse_command(self, command):
        command = command.split()
        if command[0] == 'open':
            print("Tried to open cell on position ", command[1], command[2])
            self.controller.on_left_click(int(command[1]) - 1, int(command[2]) - 1)
        elif command[0] == 'flag':
            print("Flagged cell on position ", command[1], command[2])
            self.controller.on_right_click(int(command[1]) - 1, int(command[2]) - 1)

    def block_cell(self, row, column, block=True):
        pass

    def get_game_settings(self):
        return self.row_count, self.column_count, self.mine_count

    def show_win_message(self):
        print('\nCongratulations!', 'You won!\n')

    def show_game_over_message(self):
        print('\nGame over!', 'You lose!\n')
