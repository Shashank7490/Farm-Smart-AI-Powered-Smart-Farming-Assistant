import streamlit as st
import plotly.graph_objects as go


# =========================
# Gauge Component
# =========================
def render_gauge(
    label: str,
    value: float,
    min_val: float,
    max_val: float,
    unit: str = "",
    height: int = 250,
):
    """
    Renders a Plotly gauge chart in Streamlit.

    Args:
        label (str): Gauge title
        value (float): Current value
        min_val (float): Minimum gauge value
        max_val (float): Maximum gauge value
        unit (str): Unit suffix (e.g., °C, %, mm)
        height (int): Chart height
    """

    fig = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=value,
            number={"suffix": f" {unit}"},
            title={"text": label},
            gauge={
                "axis": {"range": [min_val, max_val]},
                "bar": {"thickness": 0.25},
            },
        )
    )

    fig.update_layout(
        height=height,
        margin=dict(l=10, r=10, t=40, b=10),
    )

    st.plotly_chart(fig, use_container_width=True)


# =========================
# Section Header
# =========================
def section_header(text: str):
    """
    Styled section header for consistent UI.
    """
    st.markdown(
        f"""
        <h3 style="margin-top: 1.5rem; margin-bottom: 0.5rem;">
            {text}
        </h3>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Info Card
# =========================
def info_card(title: str, content: str):
    """
    Simple bordered information card.
    """
    st.markdown(
        f"""
        <div style="
            border: 1px solid #e6e6e6;
            border-radius: 10px;
            padding: 1rem;
            margin-bottom: 1rem;
            background-color: #fafafa;
        ">
            <h4>{title}</h4>
            <p>{content}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


# =========================
# Metric Row
# =========================
def metric_row(metrics: dict):
    """
    Displays multiple metrics in a row.

    Args:
        metrics (dict): {label: value}
    """
    cols = st.columns(len(metrics))
    for col, (label, value) in zip(cols, metrics.items()):
        col.metric(label, value)


# =========================
# Image Preview Box
# =========================
def image_preview(image, caption: str = ""):
    """
    Displays an image with consistent styling.
    """
    st.image(image, caption=caption, use_container_width=True)


# =========================
# Divider
# =========================
def divider():
    """
    Horizontal divider.
    """
    st.markdown("---")


# =========================
# Status Badge
# =========================
def status_badge(text: str, status: str = "info"):
    """
    Displays a colored status badge.

    status: info | success | warning | error
    """

    colors = {
        "info": "#dbeafe",
        "success": "#dcfce7",
        "warning": "#fef3c7",
        "error": "#fee2e2",
    }

    bg = colors.get(status, "#e5e7eb")

    st.markdown(
        f"""
        <span style="
            background-color: {bg};
            padding: 6px 12px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 500;
        ">
            {text}
        </span>
        """,
        unsafe_allow_html=True,
    )