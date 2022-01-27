"""
Basic example srowing row to read and validate data from a file using Pydantic.
"""
import asyncio

from importlib.resources import path
import json
from typing import List, Optional

from pydantic import BaseModel, ValidationError, validator

from hypothesis import given
from hypothesis.strategies import from_type

import requests
import httpx


class Ticker(BaseModel):
    name: str
    
    @validator('name')
    def value_must_equal_aapl(cls, v):
        if v != "AAPL":
            raise ValueError("value must be 'AAPL'")
        return v
    
    @classmethod
    def custom_init(cls, name: str):
        return cls(name=name)

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
            ticker = Ticker.custom_init(ticker)
            self.tasks.append(self.get_ticker_async(ticker))
        await asyncio.gather(*self.tasks)
        
        with open('scripts/tutorials/arjan/pydantic_vs_dataclasses/pretty_data.json', 'w', encoding='utf-8') as f:
            data = {"results" : self.results}
            json.dump(data, f, ensure_ascii=False, indent=4)
        return self.results

    def main(self) -> None:
        """Main function."""

        # Read data from a JSON file
        with open("scripts/tutorials/arjan/pydantic_vs_dataclasses/pretty_data.json") as file:
            data = json.load(file) # loads as dict
            tickers: List[Ticker] = [Ticker.custom_init(item["ticker"]) for item in data["results"]]

            # tickers: List[Ticker] = [Ticker(**item) for item in data]
            # print(tickers[0].name)
            return tickers
            
    def demo_errors(self) -> None:
        # Read data from a JSON file
        with open("scripts/tutorials/arjan/pydantic_vs_dataclasses/pretty_data.json") as file:
            data = json.load(file) # loads as dict
            
        for item in data["results"]:           
            try:
                print(Ticker.custom_init(item["ticker"]))
            except ValidationError as e:
                print(e.errors())        
    
    

if __name__ == "__main__":
    
    sd = StockData("scripts/tutorials/arjan/pydantic_vs_dataclasses/pretty_data.json")
    
    # res = sd.main()
    # print(res)
    sd.demo_errors()    
    
    # THIS IS FOR GETTING DATA
    # print(asyncio.run(sd.gather_async()))
    # data = asyncio.run(sd.gather_async())
    # data = {"data" : data}
    # print(data)
    # with open(sd.path, "w") as outfile:
    #     json.dump(data, outfile)
