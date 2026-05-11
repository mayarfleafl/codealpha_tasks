stock_prices = {
    "TSLA": 250,
    "AAPL": 180,
    "MSFT": 330,
    "AMZN": 145
}

name = input("Enter the stock name: ").strip().upper()
no_stocks =  int(input("Enter the number of stocks you want to buy: ").strip())

if name in stock_prices:
    total = stock_prices[name] * no_stocks


with open("result.csv", "w") as file:
    file.write(f"Stock name: {name}\n")
    file.write(f"Quantity: {no_stocks}\n")
    file.write(f"Total cost: ${total}")
