class Context:
    def __init__(self, state: str) -> None:
        self.state = state

    @property
    def state(self) -> str:
        print("getting state...")
        return self._state
    
    @state.setter
    def state(self, state: str) -> None:
        print(f"setting state to {state}...")
        if "error" in state:
            raise ValueError("can't have error in state string")
        self._state = state
    
    def __str__(self):
        return f"current state: {self.state}"


if __name__ == "__main__":
    context1 = Context("state0")
    # context1 = Context("state0error") # expected to raise error for containing error
    print(context1)
    # print(context1.state)