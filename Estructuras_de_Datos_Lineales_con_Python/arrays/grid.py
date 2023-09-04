"""
    Vamos a realizar un array de dos dimensions
"""

from array_1d import Array


class Grid:
    def __init__(self, rows, columns, fill_value=None):
        """
        rows (int): tamaño de filas
        columns (int): tamaño de columnas
        fill_value (_type_, optional): Defaults to None.
        """
        self.data = Array(rows)
        for row in range(rows):
            self.data[row] = Array(columns, fill_value)

    # Definimos metodo de altura
    def get_height(self):
        return len(self.data)

    # Definimos metodo de ancho
    def get_width(self):
        return len(self.data[0])

    def __getitem__(self, index):
        return self.data[index]

    def __str__(self):
        result = ""

        for row in range(self.get_height()):
            for col in range(self.get_width()):
                result += str(self.data[row][col]) + " "

            result += "\n"

        return str(result)


if __name__ == "__main__":
    matrix = Grid(3, 3)
    print(matrix)
    for row in range(matrix.get_height()):
        for column in range(matrix.get_width()):
            matrix[row][column] = row * column
    print(matrix)
    print(matrix.get_height())
    print(matrix.get_width())
    print(matrix.__getitem__(1))
    print(matrix.__getitem__(1)[2])
    print(matrix.__str__())
