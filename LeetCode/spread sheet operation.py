class SpreadSheet:
    def __init__(self):
        self.sheet = {}


    def set_value(self, cell: str, value: str) -> None:
        # data structure: use hash table to store the cell
        # use an array to store the value [val1, val2, operation]

        if not value.startswith("="):
            self.sheet[cell] = [value, "0", "+"]
            return

        value = value[1:]

        for opr in ['+', '-', '*', '/']:
            if opr in value:
                first, second = value.split(opr)
                self.sheet[cell] = [first, second, opr]
                return

    def get_value(self, cell: str, visit=None) -> int:

        def get_cell_val(ref: str, visit) -> int:
            if ref.isdigit():
                return int(ref)
            return self.get_value(ref, visit)

        if not visit:
            visit = set()
        if cell in visit:
            raise ValueError("Infinity loop")
        visit.add(cell)

        first, second, opr = self.sheet[cell]
        first = get_cell_val(first, visit)
        second = get_cell_val(second, visit)
        visit.remove(cell)  # backtracking

        if opr == '+':
            return first + second
        if opr == '-':
            return first - second
        if opr == '*':
            return first * second
        if opr == '/':
            return first // second


if __name__ == '__main__':
    ss = SpreadSheet()
    ss.set_value("A1", "5")
    ss.set_value("A2", "3")
    ss.set_value("B1", "=A1+A2")
    assert ss.get_value("A1") == 5

    ss.set_value("A1", '10')
    assert ss.get_value("B1") == 13

    # you should throw error, infinity loop
    # ss.set_value("A1", "=B1+A2")
    # ss.get_value("A1")

    ss.set_value("B2", "=B1+A1")
    ss.set_value("B3", "=B1+B2")
    assert ss.get_value("B3") == 36


