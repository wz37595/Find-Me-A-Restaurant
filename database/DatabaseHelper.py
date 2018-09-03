from log import Logger
from exception import Exception
from api import model, db

logger = Logger.getLogger('databaseHelper')


def add_task(task_token, userToken):
    logger.info("Adding task: {} for user: {} into database".format(task_token, userToken))
    user = model.User()
    return True


def get_task_status(task_token, user_token):
    if not task_token:
        logger.error("taskToken is none... We need a taskToken to find the task")
        raise Exception.NoTaskTokenError
    # TODO: do some data base look up here....
    # Exception: Doesn't exist
    # returnValue: COMPLETE PENDING STARTE


def store_task(task_token, restaurant_info):
    logger.info("Storing task{}".format(task_token))
    task = model.Task(TaskToken=task_token)
    db.session.add(task)
    for restaurant in restaurant_info:
        logger.info("Adding restaurant {}".format(restaurant['name']))
        restaurant_url = restaurant['url']
        rest = model.Restaurant(RestaurantToken=restaurant['id'], Name=restaurant['name'],
                                YelpScore=restaurant['rating'], ReviewCount=restaurant['review_count'],
                                URL=restaurant_url)
        rest_temp = model.Restaurant.query.get(restaurant['id'])

        if not rest_temp:
            db.session.add(rest)
        else:
            rest = rest_temp
        task.Restaurants.append(rest)
    db.session.commit()


def task_exist(task_token):
    return model.Task.query.get(task_token) is not None
