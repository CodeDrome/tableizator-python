import tableizator


def main():

    headings = ["ID", "Name", "Description", "Price £", "Stock"]

    data = [[37,"Tiny widget","A very tiny but useful widget", 2.99, 12],
            [19,"Small widget","Our best selling widget, fits in any pocket", 3.99, 27],
            [23,"Medium widget","For those who prefer a slightly larger widget", 5.99, 39],            
            [44,"Absolutely enormous widget","You need to be very strong to carry this widget around", 9.99, 19]]

    tableizator.tableize(headings, data)


if __name__ == "__main__":

    main()