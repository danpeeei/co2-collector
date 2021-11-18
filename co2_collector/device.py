from time import sleep


def read_average(interval: int, duration: int):
    n = int(duration / interval)
    sum = 0
    for _ in range(n):
        sum += read_co2()
        sleep(interval)
    return sum / n


def read_co2():
    try:
        import mh_z19

        ret = mh_z19.read()
        return ret["co2"]
    except Exception:
        return 800
