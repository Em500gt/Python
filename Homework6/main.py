from portfolio import calculate_portfolio_return as cpr
from portfolio import calculate_portfolio_value as cpv
from portfolio import get_most_profitable_stock as gmps

stocks = {"AAPL": 10, "GOOGL": 5, "MSFT": 8}
prices = {"AAPL": 150.25, "GOOGL": 2500.75, "MSFT": 300.50}

print(cpv(stocks, prices))
print(cpr(10000,15000))
print(gmps(stocks, prices))