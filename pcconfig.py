from env import *
import pynecone as pc

config = pc.Config(
    app_name="pynecone_example",
    api_url=API_URL,
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=5000
)
