import argparse

import requests

from co2_collector.device import read_average

parser = argparse.ArgumentParser("coe_notifer")
parser.add_argument("--url", required=True)
args = parser.parse_args()


def cli():
    average = int(read_average(10, 60))

    url = f"{args.url}/?co2={average}"
    print(url)
    requests.post(url)
