from Operation import Operation
from Column import Column
class TruthTable:
    """
    Defines a table of columns with each row after the header consisting of True and False values
    """
    def __init__(self, headers):
        self.grid = [Column(header) for header in headers]
        self.var_count = len(headers)
        cases = 2**len(headers)
        for i in range(cases):
            for head_index in range(len(headers)):
                self.grid[head_index].add_value((i // 2**(len(headers) - head_index-1)) % 2 == 1)
    def make_columns(self, num_cols):
        for col in range(num_cols):
            #List all the operations
            operation_num = self.__get_operation_num()
            operation = Operation(operation_num)

            #Display current columns
            print("The current columns and their indecies are...")
            for index, item in enumerate(self.grid):
                print(f"{item.get_header()} ({index+1})", end=' ')
            print()

            #NOT must be handled separately since it's the only unary operator
            if operation == Operation.NOT:
                col_num  = self.__get_col_num()
                #Add parenthesises if it's not one of the initial variables
                header = r'\neg '
                if col_num >= self.var_count:
                    header += '(' + self.grid[col_num].get_header() + ')'
                else:
                    header += self.grid[col_num].get_header()
                new_col = Column(header, Operation.NOT)
                new_col.generate_values(self.grid[col_num])
                self.grid.append(new_col)
            else:
                seperators = ['', '', r'\land ', r'\lor ', r'\to ']
                left_col_num, right_col_num = self.__get_col_nums(operation)
                
                #Add parenthesises if it's not one of the initial variables
                if left_col_num >= self.var_count:
                    header = '('+ self.grid[left_col_num].get_header() + ')'
                else:
                    header = self.grid[left_col_num].get_header()
                header += seperators[operation.value]
                if right_col_num >= self.var_count:
                    header += '(' + self.grid[right_col_num].get_header() + ')'
                else:
                    header += self.grid[right_col_num].get_header()
                new_col = Column(header, operation)
                new_col.generate_values(self.grid[left_col_num], self.grid[right_col_num])
                self.grid.append(new_col)
    def __get_operation_num(self):
        operation_num = -1
        while operation_num < 0:
            try:
                print("Which operation would you like to perform?")
                for name, member in Operation.__members__.items():
                    print(f"{name} ({member.value})", end=' ')
                operation_num = int(input())
                valid_operations = set(item.value for item in Operation)
                while operation_num not in valid_operations:
                    operation_num = int(input("Invalid operation, please enter a number from the list above:"))
            except:
                print('Please only enter numbers.')
        return operation_num
    def __get_col_num(self):
        col_num = -1
        while col_num < 0:
            try:
                col_num = int(input('What is the column number would you like to perform NOT on?')) - 1
                while col_num >= len(self.grid) or col_num < 0:
                    col_num = int(input('Invalid column number, please enter a number from the list above:'))
            except:
                print('Please only enter numbers.')
        return col_num
    def __get_col_nums(self, operation):
        left_col_num = -1
        right_col_num = -1
        while left_col_num < 0 or right_col_num < 0:
            columns = input(f'What are the numbers of the columns you would like to perform {operation.name} on? (Space Separated) ').split()
            #Make sure the user supplies two columns
            while len(columns) != 2:
                columns = input('Please enter exactly two space separated numbers:').split()
            try:
                left_col_num, right_col_num = map(lambda x: int(x)-1, columns)
                #Make sure the two numbers passed are valid numbers
                while left_col_num < 0 or right_col_num < 0 or left_col_num >= len(self.grid) or right_col_num >= len(self.grid):
                    columns = input("Please enter only numbers listed above:").split()
                    while len(columns) != 2:
                        columns = input('Please enter exactly two space separated numbers:').split()
                    left_col_num, right_col_num = map(lambda x: int(x)-1, columns)
            except:
                print('Please only enter numbers.')
        return (left_col_num, right_col_num)

    def write_to_file(self, file_name):
        print(f'Writing table to {file_name}')
        out_file = open(file_name, 'w')
        column_format = '|'.join(('c '*len(self.grid)).split())
        #Latex formatting for table
        out_file.write(r'$$\begin{array}{' + column_format + r'} ' + '\n')
        #Write headers
        table_header = ' & '.join([col.get_header() for col in self.grid])
        out_file.write(table_header + r'\\\hline ' + '\n')
        #Write each entry
        for i in range(len(self.grid[0].get_values())):
            row = []
            for col in self.grid:
                if col.get_values()[i]:
                    row.append('T')
                else:
                    row.append('F')
            out_file.write(' & '.join(row) + r' \\' + '\n')
        out_file.write(r'\end{array}$$' + '\n')
        out_file.close()