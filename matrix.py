import copy
class Matrix:
    """ Given a string representing a matrix of numbers, return the rows and columns of that matrix.
        So given a string with embedded newlines like:
        9 8 7
        5 3 2
        6 6 7
        representing this matrix:
         1  2  3
          |---------
        1 | 9  8  7
        2 | 5  3  2
        3 | 6  6  7
        your code should be able to spit out:
        A list of the rows, reading each row left-to-right while moving top-to-bottom across the rows,
        A list of the columns, reading each column top-to-bottom while moving from left-to-right.
        The rows for our example matrix:

        9, 8, 7
        5, 3, 2
        6, 6, 7
        And its columns:

        9, 5, 6
        8, 3, 6
        7, 2, 7
    """

    # Initializer / Instance Attributes
    def __init__(self, matrix):
        self.matrix = list(matrix.replace(" ", ""))

    def rows(self):
        print("In rows: ")
        row_matrix_str = ""
        row_matrix = "".join([("" if (self.matrix[i] == "\n" or self.matrix[i-1] == "\n") else ", ")+ self.matrix[i] for i in range(len(self.matrix))])
        row_matrix = row_matrix.strip(", ")
        return row_matrix

    def columns(self):
        print("In columns: ")
        self.matrix.append('\n')

        outer_list = []
        inner_list = []
        for index in range(len(self.matrix)):
            if self.matrix[index] != '\n':
                inner_list.append(self.matrix[index])
            else:
                outer_list.append(inner_list)
                inner_list = []

        col_matrix = copy.deepcopy(outer_list)
        for outer_index in range(len(outer_list)):
            for inner_index in range(len(outer_list[outer_index])):
                if len(outer_list[outer_index]) != len(outer_list):
                    raise Exception("Please enter a square Matrix")
                else:
                    col_matrix[outer_index][inner_index] = outer_list[inner_index][outer_index]

        col_matrix_str = ""
        for item_li in col_matrix:
            for i in range(1):
                col_matrix_str += ", ".join(item_li )
            col_matrix_str += "\n"
        col_matrix_str = col_matrix_str.strip()
        return col_matrix_str

if __name__ == '__main__':
    given = " 9 8 7\n 5 3 2\n 6 6 7\n 6 6 7"
    matrix = Matrix(given)
    print(matrix.matrix)
    print(matrix.rows())
    print(matrix.columns())
