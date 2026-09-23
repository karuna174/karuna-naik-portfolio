from .content import PROFILE, STATS
from .helpers import render

NAV = [("about", "About"), ("projects", "Projects"), ("experience", "Experience"),
       ("skills", "Skills"), ("education", "Education"), ("contact", "Contact")]


def nav() -> None:
    links = "".join(f'<a href="#{a}" target="_self">{t}</a>' for a, t in NAV)
    render(f"""
    <nav class="nav">
      <a class="brand" href="#top" target="_self">karuna<span>/</span>naik</a>
      <div class="links">{links}</div>
    </nav>
    """)


def hero() -> None:
    p = PROFILE
    stats = "".join(f'<div class="stat"><b>{v}</b><span>{l}</span></div>' for v, l in STATS)
    render(f"""
    <section id="top" class="hero">
      <div class="orb o1"></div><div class="orb o2"></div>
      <div class="hero-left">
        <div class="badge"><span class="dot"></span>{p['status']}</div>
        <h1>{p['headline']}</h1>
        <p class="lead">{p['lead']}</p>
        <div class="cta">
          <a class="btn primary" href="#projects" target="_self">See my projects</a>
          <a class="btn ghost" href="mailto:{p['email']}">Email me</a>
        </div>
        <div class="stats">{stats}</div>
      </div>
      <div class="hero-right glass term">
        <div class="term-bar"><i></i><i></i><i></i><span>about_me.py</span></div>
        <div class="code">
          <div class="ln"><span class="k">class</span> <span class="f">Karuna</span>(<span class="f">SoftwareEngineer</span>):</div>
          <div class="ln i1"><span class="c"># junior, full-stack, Python-first</span></div>
          <div class="ln i1">stack = [<span class="s">"Python"</span>, <span class="s">"JavaScript"</span>, <span class="s">"SQL"</span>]</div>
          <div class="ln i1">also&nbsp; = [<span class="s">"scikit-learn"</span>, <span class="s">"Pandas"</span>, <span class="s">"Git"</span>]</div>
          <div class="ln i1">based = <span class="s">"Bengaluru"</span></div>
          <div class="ln">&nbsp;</div>
          <div class="ln i1"><span class="k">def</span> <span class="f">ship</span>(self, idea):</div>
          <div class="ln i2">data = self.<span class="f">query</span>(idea)</div>
          <div class="ln i2">ui&nbsp;&nbsp; = self.<span class="f">build</span>(data)</div>
          <div class="ln i2"><span class="k">return</span> self.<span class="f">debug</span>(ui)<span class="cur"></span></div>
        </div>
      </div>
    </section>
    """)


def footer() -> None:
    render(f'<footer class="foot">Designed and built by {PROFILE["name"]} with Python and Streamlit.</footer>')
