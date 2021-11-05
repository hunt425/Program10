#######################################################################
# Hunter Tysdal
# CompSci Lab
# Week 10

import csv


def month_from_number(n):
    month_dict = {'01': 'January',
                  '02': 'February',
                  '03': 'March',
                  '04': 'Apirl',
                  '05': 'May',
                  '06': 'June',
                  '07': 'July',
                  '08': 'August',
                  '09': 'Septermber',
                  '10': 'October',
                  '11': 'November',
                  '12': 'December',
                  }
    return month_dict[str(n)]


def read_in_file(filename):
    data = []
    try:
        f = open(filename, 'r', encoding='UTF-8')
    except:
        return -1
    fcsv = csv.reader(f)
    for i in fcsv:
        data.append(i)
    f.close()
    return data


def create_dict(data, name):
    overall = {}
    x = data[0].index(name)
    for j in data[1:]:
        if j[x] in overall:
            overall[j[x]] += 1
        else:
            overall[j[x]] = 1
        return overall


def create_reported_date(data):
    return create_dict(data, 'Reported_Date')


def create_reported_month_dict(data):
    monthDict = {}
    # skips heading
    for i in data[1:]:
        # focuses on the first two characters of the date (month)
        month = i[1][0:2]
        if month in monthDict:
            monthDict[month] += 1
        else:
            monthDict[month] = 1

    return monthDict


def create_offense_dict(data):
    return create_dict(data, 'Offense')


def create_offense_by_zip(data):
    zipDict = {}
    for i in data[1:]:
        tempor = i[7]
        if tempor in zipDict:
            offense_dict = zipDict[tempor]
            if i[13] in offense_dict:
                offense_dict[i[13]] += 1
            else:
                offense_dict[i[13]] = 1
        else:
            zipDict[tempor] = {i[13]: 1}
    return zipDict



def main():
    filename = ''
    while filename != 'q' and filename != 'Q':
        filename = input("Enter the name of the crime data file (q to quit): \n")
        if filename == 'q' or filename == 'Q':
            print('Thank you')
            break
        data = read_in_file(filename)
        if data == -1:
            print('Could not find the file specified. {} not found'.format(filename))
            continue

        converted_month = create_reported_month_dict(data)
        # print(converted_month)

        maxim = max(converted_month, key=converted_month.get)
        print('The month with the highest number of crimes is {} with {} offenses'.format(month_from_number(maxim),
                                                                                          str(converted_month[maxim])))

        offense = create_offense_dict(data)
        maxim_offense = max(offense, key=offense.get)
        print('The offense with the highest number of crimes is {} with {} offences'.format(maxim_offense, str(
            offense[maxim_offense])))

        zipoffense = create_offense_by_zip(data)

        while True:
            offensive = input('Enter an offense\n')
            if offensive not in zipoffense:
                print('Not a valid offense, try again')
                continue

            print('{} offense by Zipcode:'.format(offensive))
            print('Zipcode     # of offences')
            print('=========================')
            for zipcode, num in zipoffense[offensive].items():
                print('{}            {}'.format(zipcode, num))
            break


main()

