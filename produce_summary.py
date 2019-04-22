files = {"um-deliveries-20140519.txt" : 1, 
"um-deliveries-20140520.txt" : 2,
 "um-deliveries-20140521.txt" : 3}

day = 1
file = "um-deliveries-20140519.txt"
def melon_delivery_report(day, file):
        print(day)
        the_file = open(file)
        for line in the_file:
                line = line.rstrip()
        words = line.split('|')

        melon = words[0]
        count = words[0]
        amount = words[0]

        print("Delivered {} {}s for total of ${}".format(
        count, melon, amount))
        the_file.close()

print(melon_delivery_report(day, file))
