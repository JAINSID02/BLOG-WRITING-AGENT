import streamlit as st
import sys, io, re
from pathlib import Path

st.set_page_config(
    page_title="BlogForge",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=DM+Serif+Display&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], .main, .block-container {
    background: #0a0a0a !important;
    color: #f0f0f0 !important;
    font-family: 'Inter', sans-serif !important;
}

[data-testid="stSidebar"],
[data-testid="stToolbar"],
[data-testid="stDecoration"],
footer, #MainMenu { display: none !important; visibility: hidden !important; }

.block-container {
    max-width: 900px !important;
    padding: 3rem 2rem 6rem !important;
    margin: 0 auto !important;
}

/* ── HEADER ──────────────────────────────────────────────── */
.bf-header {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    padding-bottom: 2rem;
    border-bottom: 1px solid #1e1e1e;
    margin-bottom: 3rem;
}
.bf-wordmark {
    display: flex;
    align-items: center;
    gap: 10px;
}
.bf-logo {
    width: 32px; height: 32px;
    background: #f0f0f0;
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 16px; color: #0a0a0a; font-weight: 700;
    font-family: 'DM Serif Display', serif;
    flex-shrink: 0;
}
.bf-brand {
    font-family: 'DM Serif Display', serif;
    font-size: 1.25rem;
    color: #f0f0f0;
    letter-spacing: -0.3px;
}
.bf-tagline {
    font-size: 0.7rem;
    color: #555;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    font-weight: 500;
}

/* ── HERO ────────────────────────────────────────────────── */
.bf-hero {
    margin-bottom: 2.5rem;
}
.bf-hero-eyebrow {
    font-size: 0.7rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.14em;
    color: #555;
    margin-bottom: 0.75rem;
}
.bf-hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2rem, 5vw, 3rem);
    line-height: 1.1;
    color: #f0f0f0;
    letter-spacing: -1px;
    margin-bottom: 0.75rem;
}
.bf-hero-sub {
    font-size: 0.9rem;
    color: #666;
    line-height: 1.6;
    max-width: 540px;
}

/* ── INPUT SECTION ───────────────────────────────────────── */
.bf-input-label {
    font-size: 0.7rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #555;
    margin-bottom: 0.6rem;
}

.stTextInput > div > div > input {
    background: #111111 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 10px !important;
    color: #f0f0f0 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.95rem !important;
    padding: 0.85rem 1.1rem !important;
    transition: border-color 0.15s !important;
    box-shadow: none !important;
    height: auto !important;
}
.stTextInput > div > div > input:focus {
    border-color: #f0f0f0 !important;
    box-shadow: 0 0 0 3px rgba(240,240,240,0.06) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: #444 !important; }
div[data-testid="stWidgetLabel"] > label,
div[data-testid="stWidgetLabel"] p { display: none !important; }

/* ── GENERATE BUTTON ─────────────────────────────────────── */
div[data-testid="stButton"] > button {
    background: #f0f0f0 !important;
    color: #0a0a0a !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    padding: 0.75rem 2rem !important;
    width: 100% !important;
    cursor: pointer !important;
    transition: opacity 0.15s, transform 0.1s !important;
}
div[data-testid="stButton"] > button:hover {
    opacity: 0.85 !important;
    transform: translateY(-1px) !important;
}
div[data-testid="stButton"] > button:active {
    transform: translateY(0) !important;
}

/* ── METRIC CARDS ────────────────────────────────────────── */
[data-testid="stMetric"] {
    background: #111111 !important;
    border: 1px solid #1e1e1e !important;
    border-radius: 12px !important;
    padding: 1rem 1.25rem !important;
}
[data-testid="stMetricLabel"] > div {
    font-size: 0.68rem !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    color: #555 !important;
    font-weight: 500 !important;
}
[data-testid="stMetricValue"] > div {
    font-size: 1.5rem !important;
    font-weight: 600 !important;
    color: #f0f0f0 !important;
    font-family: 'Inter', sans-serif !important;
}
[data-testid="stMetricDelta"] { display: none !important; }

/* ── STATUS / SPINNER ────────────────────────────────────── */
.bf-status {
    display: flex;
    align-items: center;
    gap: 10px;
    background: #111;
    border: 1px solid #1e1e1e;
    border-radius: 10px;
    padding: 0.9rem 1.2rem;
    font-size: 0.82rem;
    color: #888;
    font-family: 'Inter', monospace;
    margin: 1rem 0;
}
.bf-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #f0f0f0;
    animation: pulse 1.2s ease-in-out infinite;
    flex-shrink: 0;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
}
.bf-done-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #4caf50;
    flex-shrink: 0;
}

/* ── OUTPUT AREA ─────────────────────────────────────────── */
.bf-output-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 1.25rem 0 0.75rem;
    border-top: 1px solid #1e1e1e;
    margin-top: 2rem;
}
.bf-output-label {
    font-size: 0.7rem;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    color: #555;
}

/* ── TABS ────────────────────────────────────────────────── */
[data-testid="stTabs"] [role="tablist"] {
    background: #111 !important;
    border: 1px solid #1e1e1e !important;
    border-radius: 10px !important;
    padding: 4px !important;
    gap: 2px !important;
}
[data-testid="stTabs"] button[role="tab"] {
    background: transparent !important;
    border: none !important;
    border-radius: 7px !important;
    color: #555 !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    padding: 0.45rem 1.2rem !important;
    transition: all 0.15s !important;
}
[data-testid="stTabs"] button[role="tab"][aria-selected="true"] {
    background: #1e1e1e !important;
    color: #f0f0f0 !important;
}
[data-testid="stTabs"] [data-testid="stTabContent"] {
    background: #111 !important;
    border: 1px solid #1e1e1e !important;
    border-radius: 0 0 12px 12px !important;
    border-top: none !important;
    padding: 1.5rem 1.75rem !important;
    margin-top: -1px !important;
}

/* ── MARKDOWN CONTENT ────────────────────────────────────── */
[data-testid="stTabContent"] .stMarkdown h1 {
    font-family: 'DM Serif Display', serif !important;
    font-size: 1.8rem !important;
    font-weight: 400 !important;
    color: #f0f0f0 !important;
    letter-spacing: -0.5px !important;
    margin-bottom: 1.5rem !important;
    padding-bottom: 1rem !important;
    border-bottom: 1px solid #1e1e1e !important;
}
[data-testid="stTabContent"] .stMarkdown h2 {
    font-size: 1.1rem !important;
    font-weight: 600 !important;
    color: #f0f0f0 !important;
    margin-top: 2rem !important;
    margin-bottom: 0.75rem !important;
}
[data-testid="stTabContent"] .stMarkdown h3 {
    font-size: 0.95rem !important;
    font-weight: 600 !important;
    color: #ccc !important;
}
[data-testid="stTabContent"] .stMarkdown p {
    line-height: 1.75 !important;
    color: #bbb !important;
    font-size: 0.9rem !important;
    margin-bottom: 0.9rem !important;
}
[data-testid="stTabContent"] .stMarkdown ul,
[data-testid="stTabContent"] .stMarkdown ol {
    padding-left: 1.5rem !important;
}
[data-testid="stTabContent"] .stMarkdown li {
    color: #bbb !important;
    font-size: 0.9rem !important;
    line-height: 1.7 !important;
    margin-bottom: 0.3rem !important;
}
[data-testid="stTabContent"] .stMarkdown code {
    background: #1a1a1a !important;
    color: #e0e0e0 !important;
    font-size: 0.82rem !important;
    padding: 0.15em 0.4em !important;
    border-radius: 4px !important;
    font-family: 'SF Mono', 'Fira Code', monospace !important;
}
[data-testid="stTabContent"] .stMarkdown pre {
    background: #0f0f0f !important;
    border: 1px solid #1e1e1e !important;
    border-left: 3px solid #f0f0f0 !important;
    border-radius: 10px !important;
    padding: 1.25rem 1.5rem !important;
    overflow-x: auto !important;
    margin: 1rem 0 !important;
}
[data-testid="stTabContent"] .stMarkdown pre code {
    background: transparent !important;
    padding: 0 !important;
    font-size: 0.82rem !important;
    color: #ccc !important;
}
[data-testid="stTabContent"] .stMarkdown blockquote {
    border-left: 3px solid #2a2a2a !important;
    padding-left: 1rem !important;
    color: #666 !important;
    font-style: italic !important;
}
[data-testid="stTabContent"] .stMarkdown a {
    color: #f0f0f0 !important;
    text-decoration: underline !important;
    text-underline-offset: 2px !important;
}

/* ── CODE BLOCK (raw tab) ─────────────────────────────────── */
[data-testid="stTabContent"] [data-testid="stCode"] {
    background: #0f0f0f !important;
    border: 1px solid #1e1e1e !important;
    border-radius: 10px !important;
}
[data-testid="stTabContent"] [data-testid="stCode"] pre {
    background: transparent !important;
    border: none !important;
    border-radius: 0 !important;
    font-size: 0.8rem !important;
    color: #999 !important;
}

/* ── DOWNLOAD BUTTON ─────────────────────────────────────── */
[data-testid="stDownloadButton"] > button {
    background: transparent !important;
    color: #f0f0f0 !important;
    border: 1px solid #2a2a2a !important;
    border-radius: 10px !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.78rem !important;
    font-weight: 500 !important;
    text-transform: uppercase !important;
    letter-spacing: 0.1em !important;
    padding: 0.65rem 1.5rem !important;
    transition: background 0.15s, border-color 0.15s !important;
}
[data-testid="stDownloadButton"] > button:hover {
    background: #1a1a1a !important;
    border-color: #555 !important;
}

/* ── DIVIDER ─────────────────────────────────────────────── */
hr { border: none !important; border-top: 1px solid #1e1e1e !important; margin: 2rem 0 !important; }

/* ── ERROR ───────────────────────────────────────────────── */
[data-testid="stAlert"] {
    background: #150e0e !important;
    border: 1px solid #3a1a1a !important;
    border-radius: 10px !important;
    color: #e0a0a0 !important;
    font-size: 0.85rem !important;
}

/* ── SCROLLBAR ───────────────────────────────────────────── */
::-webkit-scrollbar { width: 4px; height: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: #2a2a2a; border-radius: 4px; }
</style>
""", unsafe_allow_html=True)


# ── HEADER ────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="bf-header">
    <div class="bf-wordmark">
        <div class="bf-logo">B</div>
        <span class="bf-brand">BlogForge</span>
    </div>
    <span class="bf-tagline">LangGraph · Mistral · Tavily</span>
</div>
""", unsafe_allow_html=True)


# ── HERO ──────────────────────────────────────────────────────────────────────

st.markdown("""
<div class="bf-hero">
    <p class="bf-hero-eyebrow">AI-powered technical writing</p>
    <h1 class="bf-hero-title">From idea to<br>full blog post.</h1>
    <p class="bf-hero-sub">Enter a topic. The pipeline researches, plans, and writes
    a complete, structured technical blog — section by section, in parallel.</p>
</div>
""", unsafe_allow_html=True)


# ── INPUT ─────────────────────────────────────────────────────────────────────

st.markdown('<div class="bf-input-label">Topic</div>', unsafe_allow_html=True)

col_input, col_btn = st.columns([4, 1.4], gap="medium")

with col_input:
    topic = st.text_input(
        "Topic",
        placeholder="e.g. State of Multimodal LLMs in 2026",
        label_visibility="collapsed",
    )

with col_btn:
    generate = st.button("Generate →")


# ── PIPELINE ──────────────────────────────────────────────────────────────────

if generate:
    if not topic.strip():
        st.error("Enter a topic to continue.")
    else:
        try:
            from main import run
        except ImportError as exc:
            st.error(f"Could not import main.py — {exc}")
            st.stop()

        status_ph = st.empty()
        status_ph.markdown(
            '<div class="bf-status"><div class="bf-dot"></div>'
            'Routing request — deciding research mode…</div>',
            unsafe_allow_html=True,
        )

        old_stdout, captured = sys.stdout, io.StringIO()
        sys.stdout = captured
        result, error = None, None

        try:
            status_ph.markdown(
                '<div class="bf-status"><div class="bf-dot"></div>'
                'Planning, researching, writing sections in parallel…</div>',
                unsafe_allow_html=True,
            )
            result = run(topic.strip())
        except Exception as exc:
            error = exc
        finally:
            sys.stdout = old_stdout

        if error:
            status_ph.empty()
            st.error(f"Pipeline error: {error}")
            st.stop()

        status_ph.markdown(
            '<div class="bf-status"><div class="bf-done-dot"></div>'
            'Done — blog generated.</div>',
            unsafe_allow_html=True,
        )

        plan     = result.get("plan")
        final_md = result.get("final", "")
        mode     = result.get("mode", "—").replace("_", " ").title()
        n_src    = len(result.get("evidence", []))
        n_sec    = len(plan.tasks) if plan else "—"

        # ── METRICS ───────────────────────────────────────────────────────────
        st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
        m1, m2, m3, m4 = st.columns(4, gap="small")
        m1.metric("Sections", n_sec)
        m2.metric("Mode", mode)
        m3.metric("Sources", n_src)
        wc = len(final_md.split())
        m4.metric("Words", f"~{round(wc / 100) * 100:,}")

        # ── OUTPUT ────────────────────────────────────────────────────────────
        st.markdown("""
        <div class="bf-output-header">
            <span class="bf-output-label">Generated post</span>
        </div>""", unsafe_allow_html=True)

        tab_render, tab_raw = st.tabs(["Rendered", "Markdown"])

        with tab_render:
            st.markdown(final_md)

        with tab_raw:
            st.code(final_md, language="markdown")

        # ── DOWNLOAD ──────────────────────────────────────────────────────────
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        slug = re.sub(r'[^a-z0-9_]', '',
               (plan.blog_title if plan else topic).lower().replace(" ", "_"))
        filename = f"{slug}.md"

        st.download_button(
            label="↓  Download .md",
            data=final_md.encode("utf-8"),
            file_name=filename,
            mime="text/markdown",
        )