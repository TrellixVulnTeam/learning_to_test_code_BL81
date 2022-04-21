# I got this example from slack when someone asked in #support if there was a bug with one of the Jina AI demos (section 4). This example replaces it.
# 4-16-22 KZ

# In this example we do the following:
# 1. Use "from_csv" to load Documents
# 2. Index Document
# 3. Perform Search

import os
from jina import Flow
from docarray import Document, DocumentArray
import pathlib
import shutil


def print_search_results(docs):
    left_da = docs[0]
    
    print(f"\nYour search results for: {left_da.text}")
    print("-------------------\n")
    
    for match in left_da.matches:
        print(f"> {match.scores['cosine'].value:.3f} - {match.text}")


docs = DocumentArray.from_csv("data/data.csv")

current_dir = pathlib.Path(__file__).parent.resolve()
if os.path.exists(os.path.join(current_dir, "workspace")):
    print("[INFO] removing existing workspace...")
    shutil.rmtree(os.path.join(current_dir, "workspace"))

flow = (
    Flow(
        port=12345
    ).add(
        uses="jinahub://CLIPTextEncoder/latest",
        name="encoder",
        uses_with={"device": "cpu"},
    ).add(
        uses="jinahub://SimpleIndexer/latest",
        name="indexer",
        install_requirements=True
    )
)

with flow:
    flow.index(inputs=docs, show_progress=True)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query)

print_search_results(response)
# print(response[0].matches[:1, ('text', 'scores__cosine__value')])
print("[INFO] program finished.")