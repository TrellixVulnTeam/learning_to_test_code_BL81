# https://ains.co/blog/things-which-arent-magic-flask-part-1.html
# KZ 4-7-22

# FlowManager is abstraction layer thats more abstract than the most abstract thing in Jina which is the Flow. This FlowManager abstraction layer will allow us to move up one abstraction layer and force specific Flows to be implemented..namely 1) indexing and 2) searching.




class NotFlask:
    def __init__(self):
        self.routes = {}

    def route(self, route_str):
        # note you aren't calling the function you're wrapping in the decorator. you're just using the decorator to put it in the self.routes dictionary and then returning the function. you will actually call this decorated function when you do a app.serve("/path")
        def decorator(f):
            self.routes[route_str] = f
            return f
        return decorator

    def serve(self, path):  # sourcery skip: use-named-expression
        view_function = self.routes.get(path)
        if view_function:
            return view_function()
        else:
            raise ValueError(f"route {path} not registered.")
        

app = NotFlask()

@app.route("/index")
def index():
    return "[INFO] running index."

@app.route("/search")
def search():
    return "[INFO] running search."


if __name__ == "__main__":
    print(app.serve("/index"))

