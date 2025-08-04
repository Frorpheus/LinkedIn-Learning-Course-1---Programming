import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json",
)



last_twenty_years = response.json()[1][:20]  #  .json()[1][:20] makes it work with a list and the bracketed are the indexes of the lists
# print(last_twenty_years)


for year in last_twenty_years:
    # print(year)
    # print(year["value"])
    if not year["value"]:  # no idea what this means
        continue
    display_width = year["value"] // 10_000_000
    # print(display_width)
    print(f"{year['date']}: {year['value']}", display_width * "=")





