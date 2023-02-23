import minesweeper_controller
import minesweeper_model
import minesweeper_view_alphabet_digital

if __name__ == '__main__':
    model = minesweeper_model.MinesweeperModel()
    controller = minesweeper_controller.MinesweeperController(model)
    view = minesweeper_view_alphabet_digital.MinesweeperView(model, controller)
    view.create_board()
    view.main_loop()
    #view.__init__(model, controller)
