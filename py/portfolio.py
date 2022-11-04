import functools
import operator

# from bank import Bank, MoneyAndIsValidRate
from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        # self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    # def evaluate(self, currency):
    def evaluate(self, bank, currency):

        total = Money(0, currency)
        failures = ""
        for m in self.moneys:
            c, k = bank.convert(m, currency)
            if k is None:
                total += c
            else:
                failures += k if not failures else "," + k
        if not failures:
            return total

        # bank = Bank()
        # result = functools.reduce(operator.add, map(lambda m: bank.convert(m, currency)[0], self.moneys), 0)
        # if not result.rate:
        #     return result.money
        raise Exception("Missing exchange rate(s):[" + failures + "]")
