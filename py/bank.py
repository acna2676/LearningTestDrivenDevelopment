from money import Money

# class MoneyAndIsValidRate:
#     def __init__(self, money, rate):
#         self.money = money
#         self.rate = rate

#     def __add__(self, a):
#         # add_rate = a.rate if not self.rate else "," + a.rate
#         return MoneyAndIsValidRate(self.amount+a.amount, self.rate + a.rate if not self.rate else "," + a.rate)

# class Bank:
#     def __init__(self):
#         self.exchangeRates = {}

#     def addExchangeRate(self, currencyFrom, currencyTo, rate):
#         key = currencyFrom + "->" + currencyTo
#         self.exchangeRates[key] = rate

#     def convert(self, aMoney, aCurrency):
#         if aMoney.currency == aCurrency:
#             return Money(aMoney.amount, aCurrency), ""
#         key = aMoney.currency + "->" + aCurrency
#         if key in self.exchangeRates:
#             return Money(aMoney.amount * self.exchangeRates[key], aCurrency), ""
#         return Money(0, aCurrency), key
#         # raise Exception(key)


class Bank:
    def __init__(self):
        self.exchangeRates = {}

    def addExchangeRate(self, currencyFrom, currencyTo, rate):
        key = currencyFrom + "->" + currencyTo
        self.exchangeRates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency), None
        key = aMoney.currency + "->" + aCurrency
        if key in self.exchangeRates:
            return Money(aMoney.amount * self.exchangeRates[key], aCurrency), None
        return None, key
        # raise Exception(key)
