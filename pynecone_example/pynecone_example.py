"""Welcome to Pynecone! This file create a counter app."""
import pynecone as pc
from .state import State

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
            pc.heading(State.count),
            pc.hstack(
                pc.button("Decrement", on_click=State.decrement, color_scheme="red"),
                pc.button(
                    "Randomize",
                    on_click=State.random,
                    background_image="linear-gradient(90deg, rgba(255,0,0,1) 0%, rgba(0,176,34,1) 100%)",
                    color="white",
                ),
                pc.button("Increment", on_click=State.increment, color_scheme="green"),
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
                on_click=State.random,
                _hover={
                    "opacity": 0.85,
                },
            ),
            pc.heading(State.count)
        ),
        padding_y="5em",
        font_size="2em",
        text_align="center",
)
# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, route="/")
app.add_page(about, route="/about")
app.compile()