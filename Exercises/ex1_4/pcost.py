def calculate_total_pcost(filepath):
    total_cost = 0

    with open(filepath) as f:
        for line in f:
            stock_list = line.split()
            try:
                total_cost += int(stock_list[1]) * float(stock_list[2])
            except ValueError as e:
                print("Warning:", e)

    return total_cost

if __name__ == "__main__":
    print(calculate_total_pcost('../Data/portfolio3.dat'))
