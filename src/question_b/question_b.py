#write functions here, don't add input('') statements here!
class Stock():
    
    def __init__(self, symbol, company_name):
        self.__symbol = symbol
        self.__company_name = company_name

    def get_symbol(self):
        return self.__symbol

    def get_company_name(self):
        return self.__company_name

def stock_purchase_history():
    s1 = Stock('APPL', 'Apple Inc')
    s2 = Stock('CAT', 'Caterpillar')
    s3 = Stock('EK', 'Eastman Kodak')
    s4 = Stock('GOOG', 'Google')
    s5 = Stock('MSFT','Microsoft')

    stock_dictionary = {
        s1.get_symbol():s1.get_company_name(), 
        s2.get_symbol():s2.get_company_name(), 
        s3.get_symbol():s3.get_company_name(),
        s4.get_symbol():s4.get_company_name(),
        s5.get_symbol():s5.get_company_name()
        }
    
    print("Stock Purchase History")
    print("Symbol\tCompany Name")
    for symbol, company in stock_dictionary.items():
        print(symbol.ljust(7), company)
    print("")