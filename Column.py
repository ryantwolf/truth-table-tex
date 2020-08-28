from Operation import Operation
class Column:
    """
    A column in the truth table
    """
    def __init__(self, header, operation=None):
        """
        Create a column with the given header, and an operation if the column is operating off another.
        """
        self.operation = operation
        self.values = [header]
    def get_header(self):
        return self.values[0]
    def add_value(self, value):
        self.values.append(value)
    def get_values(self):
        """
        Gets a list of True or False values in the column
        """
        return self.values[1:]
    def generate_values(self, left_col, right_col=None):
        """
        Generates a list of values for the column based on the operation provided in the
        constructor and the columns in the arguments. Provide a left_col and right_col
        unless the operator is NOT.
        """
        if self.operation == Operation.NOT:
            self.values += [not val for val in left_col.values[1:]]
        elif self.operation == Operation.AND:
            self.values += [left_col.values[i] and right_col.values[i] for i in range(1, len(left_col.values))]
        elif self.operation == Operation.OR:
            self.values += [left_col.values[i] or right_col.values[i] for i in range(1, len(left_col.values))]
        else:
            #Implies
            self.values += [not left_col.values[i] or right_col.values[i] for i in range(1, len(left_col.values))]
