class Civilization:
    def __init__(self, name):
        self.name = name
        self.cultures = []
        self.trades = []
        self.currency = None
        self.trade_network = []

    def add_culture(self, culture):
        self.cultures.append(culture)

    def set_currency(self, currency):
        self.currency = currency

    def establish_trade(self, trade):
        self.trades.append(trade)

    def create_trade_network(self, connections):
        self.trade_network = connections


class Culture:
    def __init__(self, name, traditions):
        self.name = name
        self.traditions = traditions


class Trade:
    def __init__(self, goods, price):
        self.goods = goods
        self.price = price


class Currency:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


class TradeNetwork:
    def __init__(self):
        self.connections = {}

    def add_connection(self, civilization_a, civilization_b, trade_info):
        if civilization_a not in self.connections:
            self.connections[civilization_a] = []
        self.connections[civilization_a].append((civilization_b, trade_info))

    def get_connections(self, civilization):
        return self.connections.get(civilization, [])
