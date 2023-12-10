class Stock:
    def __init__(self, symbol, company_name):
        self._symbol = symbol
        self._company_name = company_name

    def get_symbol(self):
        return self._symbol

    def get_company_name(self):
        return self._company_name


def get_stock_list(file_path):
    stock_dict = {}
    with open(file_path, 'r') as file:
        for line in file:
            symbol, company_name = line.strip().split(' ', 1)
            stock = Stock(symbol, company_name)
            stock_dict[symbol] = stock
    return stock_dict

def display_stock_list(stock_list):
    for symbol, stock in stock_list.items():
        print(f"{stock.get_company_name()} {stock.get_symbol()}")


def create_stock_file(file_path):
    enter_file = open(file_path, "w")
    symbols = ["AAPL", "CAT", "EK", "GOOG", "MSFT"]
    company = ["Apple Inc", "Caterpillar", "Eastman Kodak", "Google", "Microsoft"]

    for i in range (len(symbols)):
        enter_file.write(symbols [i] + " " + company [i] + "\n")

    enter_file.close()

if __name__ == "__main__":
    create_stock_file("get_stock_list.txt")
    stock_list = (get_stock_list("get_stock_list.txt"))
    display_stock_list(stock_list)