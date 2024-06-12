import pytest
import websockets
import json

pytest_plugins = ('pytest_asyncio',)

@pytest.fixture(scope="module", autouse=True)
def vote_tally_details():
    tally = {"election_id":"1", "precinct": "111-C", "final_tally": "6000", "approved_date": "2024-10-10"}
    yield tally
    tally = None

@pytest.mark.asyncio
async def test_websocket_actual(vote_tally_details):
     async with websockets.connect("ws://localhost:5001/ch05/vote/save/ws") as websocket:
            await websocket.send(json.dumps(vote_tally_details))
            response = await websocket.recv()
            assert response == "data not added" 