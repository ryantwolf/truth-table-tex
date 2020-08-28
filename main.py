from TruthTable import TruthTable
def get_extra_cols():
    num_extra_cols = -1
    while num_extra_cols < 0:
        try:
            num_extra_cols = int(input("How many additional columns do you need? "))
            while num_extra_cols < 0:
                num_extra_cols = int(input("The number of additional columns cannot be negative, please enter in a new number:"))
        except:
            print('Please only enter numbers.')
    return num_extra_cols
def main():
    #Get the number of pure variables
    vars = input("Enter the names of the variables (Space Separated):").split()
    while len(vars) <= 0:
        vars = input("You must supply at least one variable name, try again:").split()

    table = TruthTable(vars)

    #See how many extra columns to generate
    num_extra_cols = get_extra_cols()

    table.make_columns(num_extra_cols)

    table.write_to_file('output.tex')
if __name__ == '__main__':
    main()