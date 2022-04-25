import os
from jina import Flow
from docarray import Document, DocumentArray
import pathlib
import shutil

# https://docarray.jina.ai/datatypes/text/?utm_source=learning-portal

d = Document(uri='data/batman.txt').load_uri_to_text()
d.summary()
da = DocumentArray(Document(text=s.strip()) for s in d.text.split('\n') if s.strip())
da.summary()
da.apply(lambda d: d.embed_feature_hashing())

# remove current workspace if exists
current_dir = pathlib.Path(__file__).parent.resolve()
if os.path.exists(os.path.join(current_dir, "workspace")):
    print("[INFO] removing existing workspace...")
    shutil.rmtree(os.path.join(current_dir, "workspace"))

q = (
    Document(text='embrace the chaos of the masses')
    .embed_feature_hashing()
    .match(da, limit=5, exclude_self=True, metric='jaccard', use_scipy=True)
)

print(q.matches[:, ('text', 'scores__jaccard')])

