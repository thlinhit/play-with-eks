#!/usr/bin/env python3
import time
import threading


def child_function(param1):
    print(f'Open thread {param1}')
    while True:
        # print("doing some stuff")
        time.sleep(3)


from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    print("Initializing some things.")
    for i in range(1100):
        x = threading.Thread(target=child_function, args=(i, ))
        x.start()
    return {"message": "Hello World"}
