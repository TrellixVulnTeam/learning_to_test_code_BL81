import random
from typing import Type


class Flyer:
    def __init__(self, callsign: str) -> None:
        self.callsign = callsign

    def takeoff(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        raise NotImplementedError

# important that all Flyer objects share something in common..aka callsign..that way different types of objects can be created by the abstract factory
class Airplane(Flyer):
    def takeoff(self) -> None:
        print("swoooooosh!")
        
    def __str__(self) -> str:
        return f"Airplane<{self.callsign}>"

class Helicopter(Flyer):
    def takeoff(self) -> None:
        print("chop chop chop!")
        
    def __str__(self) -> str:
        return f"Helicopter<{self.callsign}>"
    

class ATCShop:
    """An ATC controller shop"""
    
    def __init__(self, flight_factory: Type[Flyer]) -> None:
        """clearance_factory is our abstract factory. We can set it at will"""
        
        self.clearance_factory = flight_factory
        
    def create_clearance(self, callsign: str) -> Flyer:
        clear_flyer = self.clearance_factory(callsign)
        print(f"{clear_flyer} is clear for takeoff")
        return clear_flyer
    
def main() -> None:
    atc_shop = ATCShop(Airplane)
    flight = atc_shop.create_clearance("N422R")
    flight.takeoff()
    
    
if __name__ == "__main__":
    main()