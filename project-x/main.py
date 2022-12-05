from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from fastapi import FastAPI, BackgroundTasks, Request, Response
import uvicorn
import time
import convert_numbers
import uuid


app = FastAPI()


#connection be mongodb
def dbc():
    mongo = MongoClient("mongodb://amirleo:jx1g1yAfO4iglIIO@ac-neuf2lx-shard-00-00.zhnupp7.mongodb.net:27017,ac-neuf2lx-shard-00-01.zhnupp7.mongodb.net:27017,ac-neuf2lx-shard-00-02.zhnupp7.mongodb.net:27017/?ssl=true&replicaSet=atlas-zjmtmr-shard-0&authSource=admin&retryWrites=true&w=majority")
    dbc = mongo.exchange
    return dbc

# selenium ke ba chrome gheymato az site irajib.ir migire
def getDollar():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    browser.get('https://www.iranjib.ir/showgroup/23/realtime_price/')
    dollar = browser.find_element(By.ID, 'f_16390_68_pr').text
    browser.quit()
    return dollar
    # payload = {
    #     "price" : dollar
    # }
    
    # dbc().prices.insert_one(payload)


# API endpoint
@app.get("/dollar")
def price():
    getDollar()
    price = dbc().prices.find_one()
    return {
        "gheymat" : price['price']
    }

# API buy
@app.get("/buy/{amount}")
def buy(amount):
    dollar = getDollar()
    
    total = int(convert_numbers.persian_to_english(dollar)) * int(amount)
    payload = {
        "clientID" : uuid.uuid4().hex,
        "amount" : amount,
        "dollar" : convert_numbers.persian_to_english(dollar),
        "total" : total
    }
    # BackgroundTasks.add_task()
    dbc().order.insert_one(payload)
    return {
        "clientID" : payload.get("clientID"),
        "amount" : payload.get("amount"),
        "dollar" : payload.get("dollar"),
        "total" : payload.get("total")
    }
# API order
@app.get("/order/{clientID}")
def order(clientID):
    checkOrder = dbc().order.find_one({'clientID' : clientID})
    return { 
        "amount" : checkOrder["amount"],
        "dollar" : checkOrder["dollar"],
        "total" : checkOrder["total"]
     }


    
    






# web server ke roye port 3000 karato mikone
if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=3000, log_level="info" , reload=True)
