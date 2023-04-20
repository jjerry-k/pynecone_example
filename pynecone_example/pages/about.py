import random

import pynecone as pc 
from pynecone_example.state import State

class AboutState(State):
    """The app state."""

    count = 0

    def random(self):
        """Randomize the count."""
        self.count = random.randint(0, 100)
        
def about():
    return pc.center(
        pc.vstack(
            pc.avatar(
                name="Jerry",
                ),
            pc.button(
                "Fancy Button",
                border_radius="1em",
                box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                box_sizing="border-box",
                color="white",
                on_click=AboutState.random,
                _hover={
                    "opacity": 0.85,
                },
            ),
            pc.heading(AboutState.count)
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
)