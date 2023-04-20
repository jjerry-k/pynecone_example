"""Welcome to Pynecone! This file create a counter app."""
import pynecone as pc
from pynecone_example.state import State
from .pages import index, about

# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index.index, route="/")
app.add_page(about.about, route="/about")

app.compile()