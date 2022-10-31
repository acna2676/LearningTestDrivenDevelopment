
import unittest

from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):

    # def testMultiplication(self):
    #     fiver = Dollar(5)
    #     tenner = fiver.times(2)
    #     self.assertEqual(10, tenner.amount)

    def testMultiplication(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = tenEuros.times(2)
        self.assertEqual(20, twentyEuros.amount)
        self.assertEqual("EUR", twentyEuros.currency)

    # def testMultiplicationInDollars(self):
    #     fiver = Money(5, "USD")
    #     tenner = fiver.times(2)
    #     self.assertEqual(10, tenner.amount)
    #     self.assertEqual("USD", tenner.currency)

    def testDivision(self):
        originalMoney = Money(4002, "KRW")
        actualMoneyAfterDivision = originalMoney.divide(4)
        expectedMoneyAfterDivision = Money(1000.5, "KRW")
        self.assertEqual(expectedMoneyAfterDivision.amount,
                         actualMoneyAfterDivision.amount)
        self.assertEqual(expectedMoneyAfterDivision.currency,
                         actualMoneyAfterDivision.currency)

    # def testMultiplicationInDollars(self):
    #     fiveDollars = Money(5, "USD")
    #     tenDollars = Money(10, "USD")
    #     self.assertEqual(tenDollars, fiveDollars.times(2))

    def testAddition(self):
        fiveDollars = Money(5, "USD")
        tenDollars = Money(10, "USD")
        fifteenDollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenDollars)
        self.assertEqual(fifteenDollars, portfolio.evaluate("USD"))

    def testAdditionOfDollarsAndEuros(self):
        fiveDollars = Money(5, "USD")
        tenEuros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(fiveDollars, tenEuros)
        expectedValue = Money(17, "USD")
        actualValue = portfolio.evaluate("USD")
        # self.assertEqual(expectedValue, actualValue)
        self.assertEqual(
            expectedValue, actualValue, "%s != %s" % (expectedValue, actualValue)
        )


if __name__ == '__main__':
    unittest.main()
