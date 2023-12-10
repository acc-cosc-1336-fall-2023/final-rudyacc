#add import
def create_multiplication_table():
    table = []
    for i in range(1, 6):
        row = []
        for j in range(1, 11):
            row.append(i * j)
        table.append(row)
    return table

def display_multiplication_table(table):
    for row in table:
        for item in row:
            print(item, end='\t')
        print()

while True:
    multiplication_table = create_multiplication_table()
    display_multiplication_table(multiplication_table)

    choice = input("Do you want to continue? (yes/no): ")
    if choice.lower() != 'yes':
        break