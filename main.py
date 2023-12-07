from datetime import date, datetime


def get_birthdays_per_week(users):
    res = {}
    weekends = ["Saturday", "Sunday"]
    first_weekday = "Monday"

    if len(users) == 0:
        return res

    # today = date.today()
    today = datetime(2023, 12, 27).date()
    for dic in users:
        if dic["birthday"].month == 1 and today.month == 12 and ((7 - dic["birthday"].day) > 1):
            check_year = today.year + 1
        else:
            check_year = today.year
        datus_curyear = datetime(check_year, dic["birthday"].month, dic["birthday"].day).date()

        if 0 <= (datus_curyear - today).days < 7:

            week_day = datus_curyear.strftime('%A')
            today_wday = today.strftime('%A')

            if week_day in weekends:
                if today_wday == first_weekday:
                    continue
                else:
                    if first_weekday in res:
                        res[first_weekday].append(dic["name"])
                    else:
                        res.setdefault(first_weekday, [dic["name"]])
            else:
                if week_day in res:
                    res[week_day].append(dic["name"])
                else:
                    res.setdefault(week_day, [dic["name"]])

    return res


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(1976, 1, 1).date()},
        {"name": "Steve Jobs", "birthday": datetime(1955, 10, 28).date()},
        {"name": "Greg Tores", "birthday": datetime(1975, 12, 11).date()},
        {"name": "Galina Ignatieva", "birthday": datetime(1987, 12, 10).date()},
        {"name": "Piter Yohan", "birthday": datetime(1977, 12, 7).date()},
        {"name": "Dmitriy Kazumoto", "birthday": datetime(1977, 12, 13).date()},
        {"name": "Gorge Groysman", "birthday": datetime(1977, 12, 14).date()},
        {"name": "Yohan Miloshevich", "birthday": datetime(1977, 12, 9).date()},
        {"name": "Tomas Edison", "birthday": datetime(1977, 1, 1).date()},
        {"name": "Jef Horson", "birthday": datetime(1977, 12, 25).date()}
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
