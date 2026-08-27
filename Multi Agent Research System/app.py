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

st.write("")

top_left, top_right = st.columns([5, 1])

with top_left:
    st.caption("🔬  MULTI-AGENT AI RESEARCH SYSTEM")
    st.title("DeepTrace")
    st.markdown(
        "Search deeper. Understand better. "
        "Let four specialized AI agents investigate your question."
    )

with top_right:
    st.write("")
    st.metric("Agents", "4")
    st.caption("Search · Read · Write · Critique")

st.divider()


# =========================================================
# MAIN WORKSPACE
# =========================================================

left, right = st.columns(
    [1.15, 0.85],
    gap="large",
)


# =========================================================
# RESEARCH INPUT
# =========================================================

with left:

    st.subheader("🎯 What do you want to research?")

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



# =========================================================
# PIPELINE PREVIEW
# =========================================================

with right:

    st.subheader("🧠 Research Pipeline")

    stages = [
        ("🔎", "Search Agent", "Find relevant sources"),
        ("📖", "Reader Agent", "Investigate the best sources"),
        ("✍️", "Writer Chain", "Synthesize the findings"),
        ("🧐", "Critic Chain", "Review the final report"),
    ]

    for number, (icon, name, description) in enumerate(
        stages,
        start=1,
    ):

        if st.session_state.results:
            status = "✓"
        else:
            status = str(number)

        with st.container(border=True):

            c1, c2 = st.columns([0.55, 3.5])

            with c1:
                st.markdown(f"**{status}**")

            with c2:
                st.markdown(f"**{icon} {name}**")
                st.caption(description)


# =========================================================
# RUN
# =========================================================

if run_btn:

    if not topic.strip():

        st.warning(
            "Please enter a research topic first."
        )

    else:

        st.session_state.results = {}
        st.session_state.running = True
        st.session_state.done = False

        st.rerun()


# =========================================================
# PIPELINE EXECUTION
# =========================================================

if (
    st.session_state.running
    and not st.session_state.done
):

    results = {}
    topic_val = st.session_state.topic_input

    st.divider()

    # Browser anchor used to automatically bring the user to the
    # active research section after the rerun starts.
    st.markdown(
        '<span id="researching-section" class="researching-anchor"></span>',
        unsafe_allow_html=True,
    )

    st.subheader(
        f"🔬 Researching: {topic_val}"
    )

    # Auto-scroll once the research run begins.
    st.markdown(
        """
        <script>
        (() => {
            const scrollToResearch = () => {
                const target = window.parent.document.getElementById(
                    "researching-section"
                );

                if (target) {
                    target.scrollIntoView({
                        behavior: "smooth",
                        block: "start"
                    });
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

    with st.status(
        "🔎 Search Agent · discovering sources",
        expanded=True,
    ) as status:

        search_agent = build_seacrh_agent()

        sr = search_agent.invoke(
            {
                "messages": [
                    (
                        "user",
                        (
                            "Find recent, reliable and detailed "
                            f"information about: {topic_val}"
                        ),
                    )
                ]
            }
        )

        results["search"] = (
            sr["messages"][-1].content
        )

        status.update(
            label="✓ Search Agent complete",
            state="complete",
            expanded=False,
        )

    st.session_state.results = dict(results)


    # -----------------------------------------------------
    # READER
    # -----------------------------------------------------

    with st.status(
        "📖 Reader Agent · investigating sources",
        expanded=True,
    ) as status:

        reader_agent = build_reader_agent()

        rr = reader_agent.invoke(
            {
                "messages": [
                    (
                        "user",
                        (
                            f"Based on the following search results "
                            f"about '{topic_val}', pick the most "
                            "relevant URL and scrape it for deeper "
                            "content.\n\n"
                            f"Search Results:\n"
                            f"{results['search'][:800]}"
                        ),
                    )
                ]
            }
        )

        results["reader"] = (
            rr["messages"][-1].content
        )

        status.update(
            label="✓ Reader Agent complete",
            state="complete",
            expanded=False,
        )

    st.session_state.results = dict(results)


    # -----------------------------------------------------
    # WRITER
    # -----------------------------------------------------

    with st.status(
        "✍️ Writer · synthesizing the research",
        expanded=True,
    ) as status:

        research_combined = (
            f"SEARCH RESULTS:\n{results['search']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{results['reader']}"
        )

        results["writer"] = writer_chain.invoke(
            {
                "topic": topic_val,
                "research": research_combined,
            }
        )

        status.update(
            label="✓ Research report drafted",
            state="complete",
            expanded=False,
        )

    st.session_state.results = dict(results)


    # -----------------------------------------------------
    # CRITIC
    # -----------------------------------------------------

    with st.status(
        "🧐 Critic · reviewing research quality",
        expanded=True,
    ) as status:

        results["critic"] = critic_chain.invoke(
            {
                "report": results["writer"],
            }
        )

        status.update(
            label="✓ Critic review complete",
            state="complete",
            expanded=False,
        )

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

    st.header("📑 Research Report")

    with st.container(border=True):

        st.markdown(
            results.get(
                "writer",
                "No report generated.",
            )
        )


    # -----------------------------------------------------
    # DOWNLOAD
    # -----------------------------------------------------

    st.write("")

    download_col, new_col = st.columns(2)

    with download_col:

        st.download_button(
            "⬇️  Download Report",
            data=results.get("writer", ""),
            file_name=(
                f"deeptrace_report_{int(time.time())}.md"
            ),
            mime="text/markdown",
            use_container_width=True,
        )

    with new_col:

        if st.button(
            "↻  New Research",
            use_container_width=True,
        ):

            st.session_state.results = {}
            st.session_state.done = False
            st.session_state.topic_input = ""

            st.rerun()


    # -----------------------------------------------------
    # QUALITY
    # -----------------------------------------------------

    st.divider()

    st.header("⭐ Research Quality")

    critic_text = results.get(
        "critic",
        "",
    )

    score_match = re.search(
        r"Score:\s*([\d.]+)\s*/\s*10",
        critic_text,
    )

    score = (
        score_match.group(1)
        if score_match
        else "—"
    )

    q1, q2 = st.columns([1, 2])

    with q1:

        st.metric(
            "Critic Score",
            f"{score}/10",
        )

    with q2:

        with st.container(border=True):

            st.caption("CRITIC VERDICT")

            st.markdown(
                critic_text
            )


    # -----------------------------------------------------
    # RESEARCH TRAIL
    # -----------------------------------------------------

    st.divider()

    st.header("🔬 Research Trail")

    st.caption(
        "See the evidence gathered by the research agents."
    )

    search_tab, reader_tab = st.tabs(
        [
            "🔎 Sources",
            "📖 Investigation",
        ]
    )

    with search_tab:

        with st.expander(
            "View Search Agent output",
            expanded=False,
        ):

            st.text(
                results.get(
                    "search",
                    "No search output available.",
                )
            )

    with reader_tab:

        with st.expander(
            "View Reader Agent output",
            expanded=False,
        ):

            st.text(
                results.get(
                    "reader",
                    "No reader output available.",
                )
            )


else:

    st.write("")

    st.info(
        "💡 Enter a topic above and DeepTrace will "
        "search, investigate, synthesize, and critique it."
    )