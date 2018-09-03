from log import Logger
import requests
from tokenGenerator import TokenGenerator
from exception import Exception
from database import DatabaseHelper

logger = Logger.getLogger("taskHelper")
YELP_API_KEY = 'w4BDPxLw2vH2km3WZ-V6V_t5dCMCNkn7ogkman1BxvCj16DnDejtFfqUGBa8Kumd8kesThG0N5w34SHFoAaBQr632ydG-0XrkJVVRg6R0pAnr1vYKm0rR19_fBZ3W3Yx'
YELP_BASE_URL = 'https://api.yelp.com/v3/businesses/search?'


def setUpTask(long, lat, userToken, radius, search_string):
    logger.info("Long: {}, Lat: {}, UserToken: {}, Radius: {} ".format(long, lat, userToken, radius))
    radius = 50 if not radius else radius
    task_token = TokenGenerator.generate_task_token(long, lat, radius, search_string)
    if DatabaseHelper.task_exist(task_token):
        return task_token
    restaurant_info = get_restaurant_info(long, lat, radius, search_string=search_string)
    DatabaseHelper.store_task(task_token, restaurant_info)
    # TODO: Send to Google PubSub
    return task_token


def get_restaurant_info(long, lat, radius, search_string):
    headers = {'Authorization': 'Bearer ' + YELP_API_KEY}
    request_url = YELP_BASE_URL + 'latitude=' + str(lat) + '&longitude=' \
                  + str(long) + '&term=' + search_string + '&limit=50' + '&radius=' + str(radius)
    response = requests.get(request_url, headers=headers)
    logger.info(response.content)
    return response.json()['businesses']
