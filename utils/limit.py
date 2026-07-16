import datetime
import config

def can_order(user):
    today = datetime.date.today()
    if user.last_order_date != today:
        user.orders_today = 0
        user.last_order_date = today
    total_limit = config.DAILY_FREE_LIMIT + user.extra_limits_bought
    return user.orders_today < total_limit
