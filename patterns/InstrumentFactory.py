

class InstrumentFactory:
    def create_instrument(data:dict):

        symbol = data['Symbol']
        type_ins = data['Type']
        price = data['Price']
        sector = data['Sector']
        issuer = data['Issuer']

        if type_ins == 'Stock':
            return Stock(symbol,type_ins, price,sector,issuer)
        elif type_ins == 'Bond':
            maturity = data['Maturity']
            return Bond(symbol,type_ins, price,sector,issuer,maturity)
        elif type_ins == 'ETF':
            return ETF(symbol,type_ins, price,sector,issuer)
        else:
            raise ValueError('Unknown Instrument')
        

class Stock:
    def __init__(self,symbol,typeS,price,sector,issuer):
        self.symbol = symbol
        self.type = typeS
        self.price = price
        self.sector = sector
        self.issuer = issuer

    def get_metrics(self):
        return {
            "symbol": self.symbol,
            "type": self.type,
            "price": self.price,
            "sector": self.sector,
            "issuer": self.issuer
        }

class ETF:
    def __init__(self,symbol,typeS,price,sector,issuer):
        self.symbol = symbol
        self.type = typeS
        self.price = price
        self.sector = sector
        self.issuer = issuer

    def get_metrics(self):
        return {
            "symbol": self.symbol,
            "type": self.type,
            "price": self.price,
            "sector": self.sector,
            "issuer": self.issuer
        }

class Bond:
    def __init__(self,symbol,typeS,price,sector,issuer, maturity):
        self.symbol = symbol
        self.type = typeS
        self.price = price
        self.sector = sector
        self.issuer = issuer
        self.maturity = maturity
    
    def get_metrics(self):
        return {
            "symbol": self.symbol,
            "type": self.type,
            "price": self.price,
            "sector": self.sector,
            "issuer": self.issuer,
            "maturity":self.maturity
        }

