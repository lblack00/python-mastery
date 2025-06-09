if __name__ == "__main__":
    total_cost = 0
    with open("../Data/portfolio.dat") as f:
        for line in f:
            stock_list = line.split()
            total_cost += int(stock_list[1]) * float(stock_list[2])

    print("Total cost of purchasing portfolio: $%.2f" % total_cost)

