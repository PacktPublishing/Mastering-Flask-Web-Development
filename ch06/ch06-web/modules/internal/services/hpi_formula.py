from celery import shared_task
from json import loads
from asyncio import run
from datetime import time, datetime

from pandas import DataFrame

@shared_task(ignore_result=False)
def compute_hpi_laspeyre(df_json):
    async def compute_hpi_task(df_json):
        try:
            df_dict = loads(df_json)
            df = DataFrame(df_dict)
            df["p1*q0"] = df["p1"] * df["q0"]
            df["p0*q0"] = df["p0"] * df["q0"]
            print(df)
            numer = df["p1*q0"].sum()
            denom = df["p0*q0"].sum()
            hpi = numer/denom
            return hpi
        except Exception as e:
            print(e)
            return 0
    return run(compute_hpi_task(df_json))