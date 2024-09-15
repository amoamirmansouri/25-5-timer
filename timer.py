import time
from winotify import Notification, audio

notif = Notification(app_id="Timer",
                     title="time's up!!!",
                     duration="long",
                     msg="<< 25m is over starting last 5m >>")
notif2 = Notification(app_id="Timer",
                     title="time's up!!!",
                     duration="long",
                     msg="<< 5m is over!!! >>")

notif.set_audio(sound=audio.Reminder, loop=False)
notif2.set_audio(sound=audio.Mail, loop=False)
def timer(second: int=1500):
    """30min timer for study."""
    breaker: bool = False
    while second  >= 0:
        mint, sec = divmod(second,60)
        time_txt = '{:02d}:{:02d}'.format(mint, sec)
        print(time_txt)
        if second == 0:
            if breaker:
                notif2.show()
                break
            else:
                second = 300
                print("<<5m started>>")
                notif.show()
                breaker = True
        time.sleep(1)
        second-=1