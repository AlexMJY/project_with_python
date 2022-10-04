# 1달러 원화로 변환

from currency_converter import CurrencyConverter

cc = CurrencyConverter('http://www.ecb.europa.eu/stats/eurofxref/eurofxref.zip')

print(cc.convert(1, 'USD', 'KRW'))