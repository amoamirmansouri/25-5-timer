import time

def timer(second: int=1500):
    """30min timer for study."""
    breaker: bool = False
    while second  >= 0:
        if second == 0:
            if breaker:
                break
            print("<< 25m is over starting last 5m >>")
            second = 300
            breaker = True
        mint, sec = divmod(second,60)
        time_txt = '{:02d}:{:02d}'.format(mint, sec)
        print(time_txt)
        time.sleep(1)
        second-=1