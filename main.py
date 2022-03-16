from datetime import datetime
import requests


def get_location_coords(location):
    return requests.get(f"https://geocode.xyz/{location}?json=1").json()


def get_loc_until_response(location):

    #free service... too many requests...

    def check_for_throttle(loc):
        done = False
        while not done:
            response = get_location_coords(loc)
            if "error" in response:
                if response["error"]["code"] == "006":  # throttling
                    pass
                if response["error"]["code"] == "008":  # false request
                    return None
            else:
                return response

    return check_for_throttle(location)


def get_weather(coords):
    latt, long = coords
    return requests.get(f"https://api.open-meteo.com/v1/forecast"
                        f"?latitude={latt}&longitude={long}&hourly=temperature_2m").json()


def pretty_print_weather(weather):
    times = weather["hourly"]["time"]
    temperature = weather["hourly"]["temperature_2m"]
    curr = datetime.fromisoformat(times[0])
    last_day = curr.weekday()
    print_weekday_header(curr)

    curr_line = "║" + "-----│" * curr.hour

    for time in range(len(times)):
        curr = datetime.fromisoformat(times[time])
        if curr.weekday() != last_day:
            print("╟" + "┈┈┈┈┈┼" * 23 + "┈┈┈┈┈╢")
            print(curr_line)
            print("╚" + "═════╧" * 23 + "═════╝")
            curr_line = "║"
            print_weekday_header(curr)
        if curr.hour == 23:
            curr_line += "{: 5.1f}║".format(temperature[time])
        else:
            curr_line += "{: 5.1f}│".format(temperature[time])

        last_day = curr.weekday()
    print("╟" + "┈┈┈┈┈┼" * 23 + "┈┈┈┈┈╢")
    print(curr_line)
    print("╚" + "═════╧" * 23 + "═════╝")


def print_weekday_header(weekday):
    weekday_str = weekday.strftime("%A")#%A	Sunday	Weekday as locale’s full name.
    ordinal = "th"
    if weekday.day == 1:
        ordinal = "st"
    elif weekday.day == 2:
        ordinal = "nd"
    elif weekday.day == 3:
        ordinal = "rd"
    header_text = f"- - --{weekday_str}, {weekday.day}{ordinal}-- - -"

    print("{:}".format(header_text))
    print("╔" + "═════╤" * 23 + "═════╗")
    print("║12 AM│ 1 AM│ 2 AM│ 3 AM│ 4 AM│ 5 AM│ 6 AM│ 7 AM│ 8 AM│ 9 AM│10 AM│11 AM│12 PM│ 1 PM│ 2 PM│ 3 PM│ 4 PM│ 5 "
          "PM│ 6 PM│ 7 PM│ 8 PM│ 9 PM│10 PM│11 PM║")

#old
#'%10s' % ('test',)
#New
#'{:>10}'.format('test')

def menu_loop():
    print("WeatherTool")
    done = False  #keep asking ...
    while not done:
        print("Please input the location to look for weather, or type 'exit' to exit.")
        location = input()
        if location == "exit":
            break
        print("Processing...", end='') 
        locdata = get_loc_until_response(location)
        if locdata is None:
            print("Location not found.")
            continue
        print("Location found, getting weather data...", end='')
        weather = get_weather((locdata["latt"], locdata["longt"]))
        print(f"Weather data received - temperatures are in {weather['hourly_units']['temperature_2m']}.")
        pretty_print_weather(weather)


if __name__ == '__main__':
    menu_loop()
