"""
Basic example srowing row to read and validate data from a file using Pydantic.
"""
import asyncio

from importlib.resources import path
import json
from typing import List, Optional

from pydantic import BaseModel

from hypothesis import given
from hypothesis.strategies import from_type

import requests
import httpx


class Ticker(BaseModel):
    name: str
    
    def __init__(self, name: str):
        super().__init__(name=name)

    # required for API_PATTERN format string in StockData constructor    
    def __str__(self):
        return str(self.name)

class StockData:
    def __init__(self, path: str) -> None:
        self.API_PATTERN = ("https://api.polygon.io/v2/aggs/ticker/{}/prev?adjusted=true&apiKey=MZKYHNEuNItauIYo2MrQUF2EPeOPo1Zt")
        self.path = path   
        self.tasks = []
        self.results = []
        
    async def get_ticker_async(self, ticker):
        async with httpx.AsyncClient() as client:
            response = await client.get(self.API_PATTERN.format(ticker))
            self.results.append(response.json())
            # return 
            
    async def gather_async(self):
        tickers = ["AAPL", "FB"]
        for ticker in tickers:
            ticker = Ticker(ticker)
            self.tasks.append(self.get_ticker_async(ticker))
        await asyncio.gather(*self.tasks)
        return self.results

    def get_and_save_json(self, ticker: str) -> None:
        ticker = Ticker(ticker)
        url = self.API_PATTERN.format(ticker)
        
        # request data (text)
        r = httpx.get(url)
        print(type(r.text)) # str
        print(type(r.json())) # dict
        
        # print("-", type(json.loads(r.text))) # dict
        # print("-", json.loads(r.text))
        
        # save dict to disk
        with open(self.path, "w") as outfile:
            json.dump(r.json(), outfile)

    def main(self) -> None:
        """Main function."""

        # Read data from a JSON file
        with open("scripts/tutorials/arjan/pydantic_vs_dataclasses/aapl_fb.json") as file:
            data = json.load(file) # dict
            tickers: List[Ticker] = [Ticker(item["ticker"]) for item in data["data"]]
            print(tickers[0].name)
        return tickers
            
# res = []
# for item in data["data"]:
#     print(item)
#     ticker = Ticker(item["ticker"])
#     res.append(ticker)
#     print('-')
    
# return res



if __name__ == "__main__":
    
    sd = StockData("scripts/tutorials/arjan/pydantic_vs_dataclasses/aapl_fb.json")
    
    res = sd.main()
    print(res)    
    
    
    # THIS IS FOR GETTING DATA
    # print(asyncio.run(sd.gather_async()))
    # data = asyncio.run(sd.gather_async())
    # data = {"data" : data}
    # print(data)
    # with open(sd.path, "w") as outfile:
    #     json.dump(data, outfile)
