import streamlit as st

from .content import (ABOUT, CERTIFICATIONS, EDUCATION, EXPERIENCE, PROFILE,
                      PROJECTS, SKILLS, STRENGTHS)
from .helpers import ROOT, chips, render, section_head


def about() -> None:
    paras = "".join(f"<p>{t}</p>" for t in ABOUT)
    cards = "".join(f'<div class="glass mini"><h4>{t}</h4><p>{d}</p></div>' for t, d in STRENGTHS)
    render(f"""
    {section_head("about", "About me", "Who I am and how I work")}
    <div class="about"><div class="about-text">{paras}</div><div class="about-cards">{cards}</div></div>
    """)


def _project(p: dict) -> str:
    flow = '<span class="arrow">›</span>'.join(f'<span class="step">{s}</span>' for s in p["flow"])
    pts = "".join(f"<li>{x}</li>" for x in p["points"])
    val, lab = p["metric"]
    return f"""
    <article class="glass card">
      <div class="card-top"><span class="kind">{p['kind']}</span>
        <div class="metric"><b>{val}</b><span>{lab}</span></div></div>
      <h3>{p['title']}</h3>
      <p class="muted">{p['summary']}</p>
      <div class="flow">{flow}</div>
      <ul>{pts}</ul>
      <div class="tags">{chips(p['tags'])}</div>
      <a class="link" href="{PROFILE['github']}" target="_blank" rel="noopener">View on GitHub</a>
    </article>
    """


def projects() -> None:
    cards = "".join(_project(p) for p in PROJECTS)
    render(f"""
    {section_head("projects", "Featured projects", "Two things I built to understand how software really works")}
    <div class="grid-2">{cards}</div>
    """)


def experience() -> None:
    e = EXPERIENCE
    pts = "".join(f"<li>{x}</li>" for x in e["points"])
    render(f"""
    {section_head("experience", "Experience")}
    <div class="timeline"><div class="glass card exp">
      <div class="exp-head"><div><h3>{e['role']}</h3><p class="muted">{e['company']}, {e['place']}</p></div>
      <span class="pill">{e['period']}</span></div>
      <ul>{pts}</ul><div class="tags">{chips(e['tags'])}</div>
    </div></div>
    """)


def skills() -> None:
    cards = "".join(
        f'<div class="glass mini"><h4>{n}</h4><div class="tags">{chips(items)}</div></div>'
        for n, items in SKILLS
    )
    render(f"""
    {section_head("skills", "Skills", "Tools I use day to day")}
    <div class="grid-3">{cards}</div>
    """)


def education() -> None:
    rows = "".join(
        f'<div class="edu"><div><h4>{d}</h4><p class="muted">{s}</p></div>'
        f'<div class="edu-r"><span>{y}</span><b>{g}</b></div></div>'
        for d, s, y, g in EDUCATION
    )
    certs = "".join(f"<li>{c}</li>" for c in CERTIFICATIONS)
    render(f"""
    {section_head("education", "Education & certifications")}
    <div class="grid-2">
      <div class="glass card">{rows}</div>
      <div class="glass card"><h4>Certifications</h4><ul>{certs}</ul></div>
    </div>
    """)


def resume() -> None:
    render(f"""
    {section_head("resume", "Resume")}
    <div class="glass card resume"><h3>Want the one-page summary?</h3>
    <p class="muted">Download my resume as a PDF and read it at your own pace.</p></div>
    """)
    pdf = ROOT / "assets" / "resume.pdf"
    if pdf.exists():
        st.download_button("Download resume (PDF)", pdf.read_bytes(),
                           file_name="Karuna_M_Naik_Resume.pdf", mime="application/pdf")
    else:
        st.info("Add your resume as assets/resume.pdf to enable the download button.")


def contact() -> None:
    p = PROFILE
    items = [("Email", p["email"], f"mailto:{p['email']}"),
             ("LinkedIn", "linkedin.com/in/karunamnaik", p["linkedin"]),
             ("GitHub", "github.com/karuna174", p["github"])]
    cards = "".join(
        f'<a class="glass mini contact-card" href="{h}" target="_blank" rel="noopener">'
        f'<h4>{t}</h4><p>{v}</p></a>' for t, v, h in items
    )
    render(f"""
    {section_head("contact", "Let's talk", "I'm open to full-time Python and software roles, and happy to talk code.")}
    <div class="grid-3">{cards}</div>
    """)
