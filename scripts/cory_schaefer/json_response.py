import json
import requests

class Solution:
    def __init__(self, url):
        self.url = url
    
    def get_data(self):
        return self.json_to_dict(requests.get(self.url).text)

    def json_to_dict(self, json_string):
        return json.loads(json_string)

    def display_data(self):
        print(self.json_to_dict(requests.get(self.url).text))
    def __str__(self):
        return str(self.url)

if __name__ == "__main__":
    url = "https://www.fourteenerstats.com/peaks"
    solution = Solution(url)
    print(solution)

    solution.get_data()
    solution.display_data()
    # print(response.text)


