# test_server.py

from hypothesis import given, strategies as st
from fastapi.testclient import TestClient

from scripts.tutorials.arjan.pydantic_vs_dataclasses.server import app

client = TestClient(app)


@given(st.integers())
def test_home(s):
    res = client.get(f"/api/home/{s}")

    assert res.status_code == 200
    assert res.json() == {"message": s * s}
    
@given(st.integers())
def test_endpoint(i: int):
    res = client.get(f"/api/int/{i}")

    assert res.status_code == 200
    assert res.json() == {"i": i}
    
