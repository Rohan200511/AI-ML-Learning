import streamlit as st
import time
import re
from Agents import (
    build_reader_agent,
    build_seacrh_agent,
    writer_chain,
    critic_chain,
)


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DeepTrace — Multi-Agent AI Research",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# GLOBAL STYLE
# =========================================================

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }

    :root {
        --dt-primary: #6366f1;
        --dt-primary-dark: #4338ca;
        --dt-accent: #22d3ee;
        --dt-bg-soft: #0f172a;
        --dt-card-border: rgba(148, 163, 184, 0.18);
    }

    /* Hide default streamlit chrome */
    #MainMenu, footer {visibility: hidden;}
    header[data-testid="stHeader"] {background: transparent;}

    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Hero header */
    .dt-hero {
        background: linear-gradient(135deg, #4338ca 0%, #6366f1 45%, #22d3ee 100%);
        border-radius: 20px;
        padding: 2.2rem 2.4rem;
        margin-bottom: 1.8rem;
        box-shadow: 0 12px 32px rgba(67, 56, 202, 0.25);
        position: relative;
        overflow: hidden;
    }

    .dt-hero::after {
        content: "";
        position: absolute;
        top: -60px;
        right: -60px;
        width: 220px;
        height: 220px;
        background: rgba(255,255,255,0.08);
        border-radius: 50%;
    }

    .dt-hero-badge {
        display: inline-block;
        font-size: 0.72rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color: #e0e7ff;
        background: rgba(255,255,255,0.14);
        padding: 0.28rem 0.7rem;
        border-radius: 999px;
        margin-bottom: 0.7rem;
    }

    .dt-hero-title {
        font-size: 2.6rem;
        font-weight: 800;
        color: white;
        margin: 0 0 0.35rem 0;
        letter-spacing: -0.02em;
    }

    .dt-hero-sub {
        color: rgba(255,255,255,0.88);
        font-size: 1.02rem;
        max-width: 640px;
        line-height: 1.5;
        margin: 0;
    }

    /* Section card */
    .dt-card {
        background: rgba(148, 163, 184, 0.05);
        border: 1px solid var(--dt-card-border);
        border-radius: 16px;
        padding: 1.4rem 1.5rem;
        margin-bottom: 1rem;
    }

    .dt-section-label {
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.06em;
        color: var(--dt-primary);
        text-transform: uppercase;
        margin-bottom: 0.3rem;
    }

    /* Pipeline stage rows */
    .dt-stage {
        display: flex;
        align-items: center;
        gap: 0.9rem;
        padding: 0.7rem 0.85rem;
        border-radius: 12px;
        border: 1px solid var(--dt-card-border);
        background: rgba(148, 163, 184, 0.04);
        margin-bottom: 0.55rem;
        transition: all 0.2s ease;
    }

    .dt-stage.done {
        border-color: rgba(34, 197, 94, 0.4);
        background: rgba(34, 197, 94, 0.06);
    }

    .dt-stage-num {
        display: flex;
        align-items: center;
        justify-content: center;
        min-width: 30px;
        height: 30px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--dt-primary), var(--dt-accent));
        color: white;
        font-weight: 700;
        font-size: 0.85rem;
    }

    .dt-stage.done .dt-stage-num {
        background: #22c55e;
    }

    .dt-stage-icon {
        font-size: 1.3rem;
    }

    .dt-stage-name {
        font-weight: 650;
        font-size: 0.95rem;
        margin-bottom: 0.05rem;
    }

    .dt-stage-desc {
        font-size: 0.78rem;
        color: #94a3b8;
    }

    /* Score badge */
    .dt-score-ring {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background: linear-gradient(135deg, var(--dt-primary), var(--dt-accent));
        border-radius: 18px;
        padding: 1.4rem 1rem;
        color: white;
        text-align: center;
    }

    .dt-score-value {
        font-size: 2.4rem;
        font-weight: 800;
        line-height: 1;
    }

    .dt-score-label {
        font-size: 0.72rem;
        letter-spacing: 0.06em;
        text-transform: uppercase;
        opacity: 0.85;
        margin-top: 0.3rem;
    }

    div.stButton > button, div.stDownloadButton > button {
        border-radius: 10px;
        font-weight: 650;
        border: none;
    }

    div.stButton > button[kind="primary"] {
        background: linear-gradient(135deg, var(--dt-primary), var(--dt-accent));
        box-shadow: 0 6px 16px rgba(99, 102, 241, 0.35);
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# SESSION STATE
# =========================================================

if "results" not in st.session_state:
    st.session_state.results = {}

if "running" not in st.session_state:
    st.session_state.running = False

if "done" not in st.session_state:
    st.session_state.done = False

if "topic_input" not in st.session_state:
    st.session_state.topic_input = ""


# =========================================================
# HEADER
# =========================================================

st.markdown(
    """
    <div class="dt-hero">
        <div class="dt-hero-badge">🔬 MULTI-AGENT AI RESEARCH SYSTEM</div>
        <div class="dt-hero-title">DeepTrace</div>
        <p class="dt-hero-sub">
            Search deeper. Understand better. Four specialized AI agents
            search, read, write, and critique — so you get a vetted
            research report, not just a list of links.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# =========================================================
# MAIN WORKSPACE
# =========================================================

left, right = st.columns([1.15, 0.85], gap="large")


# =========================================================
# RESEARCH INPUT
# =========================================================

with left:

    st.markdown('<div class="dt-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="dt-section-label">Step 1 · Ask a question</div>',
        unsafe_allow_html=True,
    )
    st.markdown("#### 🎯 What do you want to research?")

    topic = st.text_input(
        "Research topic",
        placeholder="e.g. Quantum computing breakthroughs in 2026",
        key="topic_input",
        label_visibility="collapsed",
    )

    run_btn = st.button(
        "⚡  Start Deep Research",
        use_container_width=True,
        type="primary",
    )
    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# PIPELINE PREVIEW
# =========================================================

with right:

    st.markdown('<div class="dt-card">', unsafe_allow_html=True)
    st.markdown(
        '<div class="dt-section-label">How it works</div>',
        unsafe_allow_html=True,
    )
    st.markdown("#### 🧠 Research Pipeline")

    stages = [
        ("🔎", "Search Agent", "Find relevant sources"),
        ("📖", "Reader Agent", "Investigate the best sources"),
        ("✍️", "Writer Chain", "Synthesize the findings"),
        ("🧐", "Critic Chain", "Review the final report"),
    ]

    is_complete = bool(st.session_state.results)

    stage_html = ""
    for number, (icon, name, description) in enumerate(stages, start=1):
        cls = "dt-stage done" if is_complete else "dt-stage"
        badge = "✓" if is_complete else str(number)
        stage_html += f"""
        <div class="{cls}">
            <div class="dt-stage-num">{badge}</div>
            <div class="dt-stage-icon">{icon}</div>
            <div>
                <div class="dt-stage-name">{name}</div>
                <div class="dt-stage-desc">{description}</div>
            </div>
        </div>
        """

    st.markdown(stage_html, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# =========================================================
# RUN
# =========================================================

if run_btn:

    if not topic.strip():
        st.warning("Please enter a research topic first.")

    else:
        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False
        st.rerun()


# =========================================================
# PIPELINE EXECUTION
# =========================================================

if st.session_state.running and not st.session_state.done:

    results = {}
    topic_val = st.session_state.topic_input

    st.divider()

    st.markdown(
        '<span id="researching-section" class="researching-anchor"></span>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="dt-card" style="border-color: rgba(99,102,241,0.4);">
            <div class="dt-section-label">Live run</div>
            <h4 style="margin:0;">🔬 Researching: {topic_val}</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <script>
        (() => {
            const scrollToResearch = () => {
                const target = window.parent.document.getElementById(
                    "researching-section"
                );
                if (target) {
                    target.scrollIntoView({ behavior: "smooth", block: "start" });
                    return true;
                }
                return false;
            };
            if (!scrollToResearch()) {
                setTimeout(scrollToResearch, 150);
                setTimeout(scrollToResearch, 500);
                setTimeout(scrollToResearch, 1000);
            }
        })();
        </script>
        """,
        unsafe_allow_html=True,
    )

    # -----------------------------------------------------
    # SEARCH
    # -----------------------------------------------------

    with st.status("🔎 Search Agent · discovering sources", expanded=True) as status:

        search_agent = build_seacrh_agent()

        sr = search_agent.invoke(
            {
                "messages": [
                    (
                        "user",
                        f"Find recent, reliable and detailed information about: {topic_val}",
                    )
                ]
            }
        )

        results["search"] = sr["messages"][-1].content

        status.update(label="✓ Search Agent complete", state="complete", expanded=False)

    st.session_state.results = dict(results)

    # -----------------------------------------------------
    # READER
    # -----------------------------------------------------

    with st.status("📖 Reader Agent · investigating sources", expanded=True) as status:

        reader_agent = build_reader_agent()

        rr = reader_agent.invoke(
            {
                "messages": [
                    (
                        "user",
                        (
                            f"Based on the following search results about "
                            f"'{topic_val}', pick the most relevant URL and "
                            "scrape it for deeper content.\n\n"
                            f"Search Results:\n{results['search'][:800]}"
                        ),
                    )
                ]
            }
        )

        results["reader"] = rr["messages"][-1].content

        status.update(label="✓ Reader Agent complete", state="complete", expanded=False)

    st.session_state.results = dict(results)

    # -----------------------------------------------------
    # WRITER
    # -----------------------------------------------------

    with st.status("✍️ Writer · synthesizing the research", expanded=True) as status:

        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )

        results["writer"] = writer_chain.invoke(
            {"topic": topic_val, "research": research_combined}
        )

        status.update(label="✓ Research report drafted", state="complete", expanded=False)

    st.session_state.results = dict(results)

    # -----------------------------------------------------
    # CRITIC
    # -----------------------------------------------------

    with st.status("🧐 Critic · reviewing research quality", expanded=True) as status:

        results["critic"] = critic_chain.invoke({"report": results["writer"]})

        status.update(label="✓ Critic review complete", state="complete", expanded=False)

    st.session_state.results = dict(results)

    st.session_state.running = False
    st.session_state.done = True

    st.rerun()


# =========================================================
# RESULTS
# =========================================================

results = st.session_state.results


if results:

    st.divider()

    # -----------------------------------------------------
    # REPORT
    # -----------------------------------------------------

    report_col, action_col = st.columns([3.2, 1])

    with report_col:
        st.header("📑 Research Report")

    with action_col:
        st.write("")
        st.download_button(
            "⬇️  Download",
            data=results.get("writer", ""),
            file_name=f"deeptrace_report_{int(time.time())}.md",
            mime="text/markdown",
            use_container_width=True,
        )

    st.markdown('<div class="dt-card">', unsafe_allow_html=True)
    st.markdown(results.get("writer", "No report generated."))
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("↻  New Research", use_container_width=False):
        st.session_state.results = {}
        st.session_state.done = False
        st.session_state.topic_input = ""
        st.rerun()

    # -----------------------------------------------------
    # QUALITY
    # -----------------------------------------------------

    st.divider()
    st.header("⭐ Research Quality")

    critic_text = results.get("critic", "")

    score_match = re.search(r"Score:\s*([\d.]+)\s*/\s*10", critic_text)
    score = score_match.group(1) if score_match else "—"

    q1, q2 = st.columns([1, 2.6])

    with q1:
        st.markdown(
            f"""
            <div class="dt-score-ring">
                <div class="dt-score-value">{score}</div>
                <div class="dt-score-label">out of 10</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with q2:
        st.markdown('<div class="dt-card" style="height:100%;">', unsafe_allow_html=True)
        st.markdown(
            '<div class="dt-section-label">Critic verdict</div>',
            unsafe_allow_html=True,
        )
        st.markdown(critic_text)
        st.markdown("</div>", unsafe_allow_html=True)

    # -----------------------------------------------------
    # RESEARCH TRAIL
    # -----------------------------------------------------

    st.divider()
    st.header("🔬 Research Trail")
    st.caption("See the evidence gathered by the research agents.")

    search_tab, reader_tab = st.tabs(["🔎 Sources", "📖 Investigation"])

    with search_tab:
        st.markdown('<div class="dt-card">', unsafe_allow_html=True)
        st.text(results.get("search", "No search output available."))
        st.markdown("</div>", unsafe_allow_html=True)

    with reader_tab:
        st.markdown('<div class="dt-card">', unsafe_allow_html=True)
        st.text(results.get("reader", "No reader output available."))
        st.markdown("</div>", unsafe_allow_html=True)

else:

    st.info(
        "💡 Enter a topic above and DeepTrace will "
        "search, investigate, synthesize, and critique it."
    )