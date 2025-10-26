
from models import Stock,Bond,ETF

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
        
