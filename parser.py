import csv
import random
import datetime

class covid_19(object):
    def __init__(self, state, country, lat, long, dates ):
        self.state = state
        self.country = country
        self.lat = lat
        self.long = long
        self.dates = dates

def reader(path_name_csv):
    with open(path_name_csv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        list_data = []
        for row in csv_reader:
            state , country , lat , long, dates = '','','','',[]
            for idx,col in enumerate(row):
                if idx == 0:
                    state = col
                elif idx == 1:
                    country = col
                elif idx == 2:
                    lat = col
                elif idx == 3:
                    long = col
                else:
                    dates.append(col)
            list_data.append(covid_19(state , country , lat , long, dates))
    return list_data


def init_start():
    g = input("Enter 1 for deaths or 2 for confirmed from covid-19 : ") 

    if g == '1' :
        deaths = reader("dataset/covid_19_deaths.csv")
        country = input("Which contry (the first letter in uppercase): ")
        for i in deaths :
            if i.country == country :
                lists=zip(deaths[0].dates , per_day(i.dates))
        writer(list(lists))

    elif g == '2' :
        confirmed = reader("dataset/covid_19_confirmed.csv")    
        country = input("Which contry (the first letter in uppercase): ")
        for i in confirmed :
            if i.country == country :
                lists=zip(confirmed[0].dates , per_day(i.dates))
        writer(list(lists))

    else :
        print("wrong input, try again...")
        

def per_day(list_data):
    int_data = [int(item) for item in list_data]
    temp_data=[y - x for x, y in zip(int_data, int_data[1:])]
    return temp_data

def writer(list_pairs):
    with open('dataset/chosenCountry.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        for x in list_pairs :
            writer.writerow([x[0],int(x[1])])
            
