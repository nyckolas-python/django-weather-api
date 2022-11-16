from urllib.request import Request, urlopen
from bs4 import BeautifulSoup as bs
from datetime import datetime
from typing import List


def _scrap_weather_info() -> List[dict]:
    """The function parses and returns weather data from the site:
    https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/week/
    
    According to the task: only 6 records are returns
    
    Returns: list of dictionaries
    Example: 
    [
        {'date': '2022-11-14', 
        'temperature': '+7°',
        'weather_description': 'мінлива хмарність, без опадів, прохолодно'
        },
    ]
    """
    try:
        url = "https://pogoda.meta.ua/ua/Kyivska/Kyivskiy/Kyiv/week/"
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Accept-Language': 'en-US,en;q=0.8',
                'Connection': 'keep-alive'}

        req = Request(url,headers=headers)
        html = urlopen(req)
        soup = bs(html, "html.parser")
        today = datetime.now()
        month_year = datetime.strftime(today, '%Y-%m-')
        # select a list of dates from the scraping data
        week_date_list = [
            month_year + x.find("span", "date").text[:3].replace(" ", "")\
            for x in soup.find_all("div", class_="weather-wrapper__date")
            ]
        # select a list of temperatures from the scraping data
        temp_list=[x.text for x in soup.find_all("span", class_="high")]
        # select a list of weather descriptions from the scraping data
        description_list=[x.get('data-tippy-content') for x in soup.find_all("span", class_="seven-days__temp-icon")]
        # create list of tuple and get only 6 records [:-1] - throw away the last one
        six_days_weather = list(zip(week_date_list, temp_list, description_list))[:-1]
        # format data to JSON
        keys = ['date', 'temperature', 'weather_description']
        forecast_json = [dict(zip(keys, values)) for values in six_days_weather]
        # print(forecast_json)
        return forecast_json
    except Exception as ex:
        print(f"[IFNO] Can't parse weather data.\n{ex}")


# if __name__ == '__main__':
#     scrap_weather_info()
