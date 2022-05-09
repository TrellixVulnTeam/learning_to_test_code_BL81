# Credits.
# https://auth0.com/blog/state-pattern-in-python/


# my example
class LightBulb:
    # be careful with default parameters in init constructor
    def __init__(self, state: str) -> None:
        self.state = state

    def change_state(self, new_state: str) -> None:
        print(f"[INFO] old state: {self.state}")
        self.state = new_state
        print(f"[INFO] new state: {self.state}")


# their example
class LightBulb2:
    _state = "off" # initial state of bulb

    def change_state(self, switch: str) -> None:
        if switch == "ON":
            self._state = switch
        elif switch == "OFF":
            self._state = switch
        else:
            # continue # can't do this even though shows this in tutorial
            print("cant do that")
        
        print(f"[INFO] current state: {self._state}")


if __name__ == "__main__":
    lb = LightBulb("starting state.")
    lb.change_state("some new state.")
    

    lb = LightBulb2()
    lb.change_state("ON")
    lb.change_state("OFF")
    lb.change_state("something not allowed.")