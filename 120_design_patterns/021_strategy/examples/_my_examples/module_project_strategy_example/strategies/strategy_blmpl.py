from strategies.strategy import Strategy

class StrategyBlmpl(Strategy):
    def calculate(value):
        return value * 0.05

    def toString(self):
        return 'Strategy B'