from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parent.parent


def html(markup: str) -> str:
    """Flatten indented markup so Markdown never treats it as a code block."""
    return "".join(line.strip() for line in markup.splitlines())


def render(markup: str) -> None:
    st.markdown(html(markup), unsafe_allow_html=True)


def load_css() -> None:
    css = (ROOT / "styles.css").read_text(encoding="utf-8")
    css = "\n".join(line for line in css.splitlines() if line.strip())
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)


def section_head(anchor: str, title: str, sub: str = "") -> str:
    sub_html = f'<p class="sub">{sub}</p>' if sub else ""
    return f'<div id="{anchor}" class="anchor"></div><div class="sec-head"><h2>{title}</h2>{sub_html}</div>'


def chips(items, cls: str = "chip") -> str:
    return "".join(f'<span class="{cls}">{i}</span>' for i in items)
