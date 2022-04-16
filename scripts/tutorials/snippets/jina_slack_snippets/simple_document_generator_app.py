# I got this example from slack when someone asked in #support if there was a bug with one of the Jina AI demos (section 4). This example replaces it.
# 4-16-22 KZ

# In this example we do the following:
# 1. Use "from_csv" to load Documents
# 2. Remove our original "docs" DocumentArray

from jina import Flow
from docarray import Document, DocumentArray

# Pull Documents from a CSV file. For each line of the file, create one Document where `Document.text` comes from the line's content.
docs = DocumentArray.from_csv("data.csv")

flow = (
    Flow()
    .add(
        uses="jinahub+sandbox://CLIPTextEncoder",
    )
    .add(
        uses="jinahub+sandbox://SimpleIndexer",
        uses_metas={"workspace": "workspace"},
        volumes="./workspace:/workspace/workspace",
        name="indexer",
    )
)

with flow:
    flow.index(inputs=docs)
    query = Document(text=input("Please enter your search term: "))
    response = flow.search(inputs=query)

print("[INFO] program finished.")