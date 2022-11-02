from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from pymongo import MongoClient
from fastapi import FastAPI, BackgroundTasks, Request, Response
import uvicorn
import time

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
    dollar = browser.find_element(By.ID, 'f_127_63_pr').text
    browser.quit()
    
    payload = {
        "price" : dollar
    }
    
    dbc().prices.insert_one(payload)


# API endpoint
@app.get("/dollar")
def price():
    getDollar()
    price = dbc().prices.find_one()
    return {
        "gheymat" : price['price']
    }




# web server ke roye port 3000 karato mikone
if __name__ == "__main__":
   uvicorn.run("main:app", host="0.0.0.0", port=3000, log_level="info" , reload=True)
