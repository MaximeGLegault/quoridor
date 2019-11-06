from tkinter import Canvas, CURRENT

from Position import Position


class WindowBoard(Canvas):

    def __init__(self, parent, caseSize=60):
        self.number_of_lines = 9
        self.number_of_columns = 9
        self.caseSize = caseSize
        self.caseRectangle = {}
        self.green_color = '#35a800'

        super().__init__(parent, width=(self.number_of_lines*self.caseSize + 17 * self.number_of_lines),
                         height=(self.number_of_columns * self.caseSize + 17 * self.number_of_columns))

        self.draw_window_board()
        self.change_color_at_position(Position(0, 0))
        self.change_color_at_position(Position(8, 8))

    def _change_color(self, rectangle_id: int) -> None:
        self.itemconfig(rectangle_id, fill=self.green_color)

    def change_color_at_position(self, position: Position):
        id = position.x + 9 * position.y + 1
        self.itemconfig(id, fill=self.green_color)

    def draw_window_board(self):
        for x in range(self.number_of_lines):
            for y in range(self.number_of_columns):
                start_line = (x * self.caseSize) + x * 20
                end_line = start_line + self.caseSize
                start_column = y * self.caseSize + y * 20
                end_column = start_column + self.caseSize

                self.caseRectangle[x, y] = self.create_rectangle(start_column, start_line, end_column, end_line,
                                                                     fill='#154abd', width=2, outline='white',
                                                                     tags='Rect')
                self.tag_bind(self.caseRectangle[x, y], "<Button-1>", self._print_position)
        self.pack()

    def _print_position(self, event) -> None:
        rect_id = self.find_withtag(CURRENT)[0] - 1
        print(f"({(rect_id // 9)}, {rect_id % 9})")
        print()
        print(rect_id)
