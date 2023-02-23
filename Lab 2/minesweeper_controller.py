class MinesweeperController:
    def __init__(self, model):
        self.model = model

    def set_view(self, view):
        self.view = view

    def start_new_game(self):
        game_settings = self.view.get_game_settings()
        try:
            self.model.start_game(*map(int, game_settings))
        except:
            self.model.start_game(self.model.row_count, self.model.column_count, self.model.mine_count)

        self.view.create_board()

    def on_left_click(self, row, column):
        self.model.open_cell(row, column)
        self.view.sync_with_model()
        if self.model.is_win():
            self.view.show_win_message()
            self.start_new_game()
        elif self.model.is_game_over():
            self.view.show_game_over_message()
            self.start_new_game()

    def on_right_click(self, row, column):
        self.model.next_cell_mark(row, column)
        self.view.block_cell(row, column, self.model.get_cell(row, column).state == 'flagged')
        self.view.sync_with_model()
