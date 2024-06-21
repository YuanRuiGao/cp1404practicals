import csv
FILENAME = "wimbledon.csv"


def main():
    """Control program operation"""

    wimbledon_information = get_information_from_wimbledon()
    champions_information, won_country = champions_information_statistics(wimbledon_information)
    display_champions_information_and_country(champions_information, won_country)


def get_information_from_wimbledon():
    """Get information from wimbledon.csv"""

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)
        information_of_wimbledon = {i[0]: [i[1], i[2], i[3], i[4], i[5]] for i in reader}
    return information_of_wimbledon


def champions_information_statistics(wimbledon_information):
    """Statistics of the champions and country"""

    champions_information = {}
    won_country = []
    for i in wimbledon_information:
        if wimbledon_information[i][1] in champions_information:
            champions_information[wimbledon_information[i][1]] += 1
        else:
            champions_information[wimbledon_information[i][1]] = 1
            if wimbledon_information[i][0] not in won_country:
                won_country.append(wimbledon_information[i][0])
    won_country.sort()
    return champions_information, won_country


def display_champions_information_and_country(champions_information, won_country):
    """Control program display"""

    print("Wimbledon Champions:")
    for i in champions_information:
        print(i, champions_information[i])
    print(f"\nThese {len(won_country)} countries have won Wimbledon:")
    print(", ".join(won_country))


main()
