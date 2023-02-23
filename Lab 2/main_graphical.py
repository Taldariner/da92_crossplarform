import minesweeper_controller
import minesweeper_model
import minesweeper_view_graphical

if __name__ == '__main__':
    model = minesweeper_model.MinesweeperModel()
    controller = minesweeper_controller.MinesweeperController(model)
    view = minesweeper_view_graphical.MinesweeperView(model, controller)
    view.pack()
    view.mainloop()
