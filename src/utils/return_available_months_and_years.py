def return_available_months_and_years(data):
    years = {}
    dates = data["date"]

    for date in dates:
        year = date.year
        month = date.month

        if years.get(year):
            if month not in years[year]:
                years[year].append(month)
        else:
            years[year] = [month]

    return years
