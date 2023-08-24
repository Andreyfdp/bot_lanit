from pydantic import BaseModel
from utils.base_api import BaseAPI
from configuration import settings


class Weather(BaseModel):
    location_name: str
    description: str
    temp: int
    temp_min: int
    temp_max: int
    wind_speed: int

    def __str__(self):
        return (f"Погода в {self.location_name}:\n"
                f"Сейчас {self.description}\n"
                f"Температура: {self.temp}\n"
                f"Минимальная температура: {self.temp_min}\n"
                f"Максимальная температура {self.temp_max}\n"
                f"Скорость ветра: {self.wind_speed} м/с ")


class WeatherAPI(BaseAPI):
    def __init__(self):
        super().__init__(base_link=settings.OPENWEATHER_API_LINK)

        self._token = settings.OPENWEATHER_API_TOKEN

    async def get_weather_info(self, latitude: float, longitude: float) -> Weather | None:
        params: dict[str, float | str] = {
            "appid": self._token,
            "lat": latitude,
            "lon": longitude,
            "units": "metric",
            "lang": "ru"
        }
        async def all_url(params):
            all_url = ''
            for i in params:
                all_url += i+'='+str(params[i])+'&'
            return all_url[:-1]
        dop_url = await all_url(params)
        #answer = await self.get_json(f"https://api.openweathermap.org/data/2.5/weather?lat={params['lat']}&lon={params['lon']}&units={params['units']}&lang={params['lang']}&appid={params['appid']}")
        answer = await self.get_json(f"/data/2.5/weather?{dop_url}")

        print(params)
        print(answer)
        if answer:
            return Weather(
                location_name=answer['name'],
                description=answer['weather'][0]['description'],
                temp=int(answer['main']['temp']),
                temp_min=int(answer['main']['temp_min']),
                temp_max=int(answer['main']['temp_max']),
                wind_speed=int(answer['wind']['speed']),
            )
        else:
            return None