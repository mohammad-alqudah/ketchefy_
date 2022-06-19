
from apscheduler.schedulers.background import BackgroundScheduler
import time 
def call_sleep_then_start():
    time.sleep(5)
    while 1:
        pass
    from  scrapper.models import MainappOrder
    p = MainappOrder(channel="ta", brand="alkaram ")
    p.save()
    


def backgroun_job():
	sched = BackgroundScheduler()
	sched.add_job(call_sleep_then_start)

	sched.add_job(call_sleep_then_start)
	sched.add_job(call_sleep_then_start)
	sched.add_job(call_sleep_then_start)

	sched.start()