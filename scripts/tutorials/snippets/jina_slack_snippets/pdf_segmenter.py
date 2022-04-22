from docarray import DocumentArray, Document
from jina import Flow

# This will give relative import errors. Run from "jina_slack_snippets" instead of from the "learning_to_test_code" root folder
doc = DocumentArray([Document(uri='./data/cats_are_awesome.pdf')]) 
doc[0].load_uri_to_blob()
print(doc[0])

f = Flow().add(
    uses='jinahub://PDFSegmenter',
)
with f:
    resp = f.post(on='/craft', inputs=doc)
    print(f'{[c.mime_type for c in resp[0].chunks]}')

resp.summary()
resp[0].chunks[0].summary() # image here
resp[0].chunks[1].summary() # image here
resp[0].chunks[2].summary() # text here
