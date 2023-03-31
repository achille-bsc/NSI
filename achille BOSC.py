monday = 0
thuesday = 0
wednesday = 0
thursday = 0
friday = 0
saturday = 0
sunday = 0

def number_dates_per_days(dates):
    for date in dates:
        if (find_day(date) == "Lundi"):
            monday += 1
        elif (find_day(date) == "Mardi"):
            thuesday += 1
        elif (find_day(date) == "Mercredi"):
            wednesday += 1
        elif (find_day(date) == "Jeudi"):
            thursday += 1
        elif (find_day(date) == "Vendredi"):
            friday +=1
        elif (find_day(date) == "Samedi"):
            saturday += 1
        elif (find_day(date) == "Dimanche"):
            sunday += 1
    return [monday, thuesday, wednesday, thursday, friday, saturday, sunday]