# This file demonstrates what a DocArray looks like when you read in from a csv using the popular iris dataset.

from docarray import Document, DocumentArray

docs = DocumentArray.from_csv("data/anime.csv")
docs[0].summary()
print(docs[0].tags.get("Favorites"))
# print(docs[0].matches)
# docs.summary()