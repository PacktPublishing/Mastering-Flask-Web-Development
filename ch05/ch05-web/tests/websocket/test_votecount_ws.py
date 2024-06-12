import websockets
import pytest
import json
import pytest_asyncio

from main import app as flask_app

pytest_plugins = ('pytest_asyncio',)

async def simulated_add_votecount_view(websocket):
    async for message in websocket:
        print("receieved: ",message)
        # Place here the VoteCount repo transactions
        await websocket.send("data added")

@pytest_asyncio.fixture
async def create_ws_server():
    async with websockets.serve(simulated_add_votecount_view, "localhost", 5001) as server:
        yield server
        
@pytest.fixture(scope="module", autouse=True)
def vote_tally_details():
    tally = {"election_id":"1", "precinct": "110-C", "final_tally": "6000", "approved_date": "2024-10-10"}
    yield tally
    tally = None

@pytest.mark.asyncio
async def test_votecount_ws(create_ws_server,vote_tally_details):
        async with websockets.connect("ws://localhost:5001/ch05/vote/save/ws") as websocket:
            await websocket.send(json.dumps(vote_tally_details))
            response = await websocket.recv()
            assert response == "data added"
            
    
    
        

    