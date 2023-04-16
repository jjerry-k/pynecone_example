import pynecone as pc

config = pc.Config(
    app_name="pynecone_example",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    port=5000
)
