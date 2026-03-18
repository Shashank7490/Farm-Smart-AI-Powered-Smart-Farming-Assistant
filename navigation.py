# ui/navigation.py

import streamlit as st


def init_navigation(default_step: int = 0):
    """
    Initialize navigation state if not present.
    Call once at app start.
    """
    if "crop_step" not in st.session_state:
        st.session_state.crop_step = default_step


def go_to_crop_step(step: int):
    """
    Move to a specific step in the multi-step flow.
    """
    st.session_state.crop_step = step
    st.rerun()


def next_step():
    """
    Move to the next step.
    """
    st.session_state.crop_step += 1
    st.rerun()


def previous_step():
    """
    Move to the previous step (with safety).
    """
    if st.session_state.crop_step > 0:
        st.session_state.crop_step -= 1
        st.rerun()


def render_back_button(label: str = "⬅️ Back"):
    """
    Renders a back button that moves to the previous step.
    """
    if st.button(label):
        previous_step()


def render_next_button(label: str = "Next ➡️"):
    """
    Renders a next button that moves to the next step.
    """
    if st.button(label):
        next_step()


def get_current_step() -> int:
    """
    Returns the current step index.
    """
    return st.session_state.get("crop_step", 0)


def reset_navigation():
    """
    Reset navigation flow to step 0.
    """
    st.session_state.crop_step = 0
    st.rerun()