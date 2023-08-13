_result = dict()

def calculate_portfolio_value(stocks: dict, prices: dict) -> float:
    global _result
    result = {key: value * prices.get(key) for key, value in stocks.items() if key in prices.keys()}    
    _result = result
    return sum(result.values())

def calculate_portfolio_return(initial_value: float, current_value: float) -> float:
    resutl = ((current_value * 100) / initial_value) - 100
    return f'{resutl}%'

def get_most_profitable_stock(stocks: dict, prices: dict) -> str:
    global _result
    most_profitable_stock = None
    max_profit = 0

    for key in stocks:
        current_profit = _result[key] - prices[key]
        if current_profit > max_profit:
            most_profitable_stock = key
            max_profit = current_profit

    return most_profitable_stock