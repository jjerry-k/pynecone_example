import random

import pynecone as pc
from pynecone_example.state import State

class IndexState(State):
    """The app state."""

    count = 0

    def increment(self):
        """Increment the count."""
        self.count += 1

    def decrement(self):
        """Decrement the count."""
        self.count -= 1

    def random(self):
        """Randomize the count."""
        self.count = random.randint(0, 100)
        
def index():
    """The main view."""
    return pc.center(
        pc.vstack(
            pc.hstack(
                pc.circular_progress(
                    pc.circular_progress_label("50", color="green"),
                    value=50,
                ),
                pc.circular_progress(
                    pc.circular_progress_label(
                        "∞", color="rgb(107,99,246)"
                    ),
                    is_indeterminate=True,
                ),
            ),
            pc.heading(IndexState.count),
            pc.hstack(
                pc.button("Decrement", on_click=IndexState.decrement, color_scheme="red"),
                pc.button(
                    "Randomize",
                    on_click=IndexState.random,
                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176,34,1) 100%)",
                    color="white",
                ),
                pc.button("Increment", on_click=IndexState.increment, color_scheme="green"),
            ),
            padding="1em",
            bg="#ededed",
            border_radius="1em",
            box_shadow="lg",
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
    )