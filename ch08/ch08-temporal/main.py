from temporalio.client import Client
from modules import create_app
import asyncio

app, celery_app= create_app("../config_dev.toml")

async def connect_temporal(app):
    client = await Client.connect("localhost:7233")
    app.temporal_client = client

if __name__ == "__main__":
    # Create Temporal connection.
    asyncio.run(connect_temporal(app))
    # Start API
    app.run(debug=True)