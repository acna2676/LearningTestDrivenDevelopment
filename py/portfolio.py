import functools
import operator

from money import Money


class Portfolio:
    def __init__(self):
        self.moneys = []
        # self._eur_to_usd = 1.2

    def add(self, *moneys):
        self.moneys.extend(moneys)

    # def evaluate(self, currency):
    def evaluate(self, bank, currency):
        # total = 0.0
        # failures = []
        # for m in self.moneys:
        #     try:
        #         total += bank.convert(m, currency).amount
        # #     except KeyError as ke:
        # #         failures.append(ke)
        # # if len(failures) == 0:
        # #     return Money(total, currency)
        # # failureMessage = ",".join(f.args[0] for f in failures)
        # # raise Exception("Missing exchange rate(s):[" + failureMessage + "]")
        #     except Exception as ex:
        #         failures.append(ex)
        # if not failures:
        #     return Money(total, currency)
        # failureMessage = ",".join(f.args[0] for f in failures)
        # raise Exception("Missing exchange rate(s):[" + failureMessage + "]")

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

        # total = functools.reduce(operator.add, map(lambda m: bank.convert(m, currency)[0], self.moneys), 0)
        # failure = functools.reduce(operator.add, map(lambda m: bank.convert(m, currency)[1], self.moneys), 0)
        # failures += k if not failures else "," + k
        raise Exception("Missing exchange rate(s):[" + failures + "]")

    # def __convert(self, aMoney, aCurrency):
    #     exchangeRates = {'EUR->USD': 1.2, 'USD->KRW': 1100}
    #     if aMoney.currency == aCurrency:
    #         return aMoney.amount
    #     else:
    #         key = aMoney.currency + '->' + aCurrency
    #         return aMoney.amount * exchangeRates[key]
        # return aMoney.amount * self._eur_to_usd
