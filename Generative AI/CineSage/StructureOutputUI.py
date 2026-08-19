import streamlit as st
from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from typing import List, Optional
from pydantic import BaseModel
from langchain_core.output_parsers import PydanticOutputParser

# ---------------------------------------------------------
# Configuration
# ---------------------------------------------------------

load_dotenv()

st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------------
# Custom Styling
# ---------------------------------------------------------

st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #0f0f17 0%, #171725 50%, #0f0f17 100%);
        color: #ffffff;
    }

    .main {
        max-width: 1100px;
        margin: auto;
    }

    .hero {
        text-align: center;
        padding: 35px 20px 25px 20px;
    }

    .hero h1 {
        font-size: 3rem;
        font-weight: 800;
        margin-bottom: 8px;
        background: linear-gradient(90deg, #ff4b4b, #ff8a4b);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    .hero p {
        font-size: 1.1rem;
        color: #a9a9b8;
        margin-top: 0;
    }

    .section-title {
        font-size: 1.25rem;
        font-weight: 700;
        margin: 20px 0 10px 0;
        color: #ffffff;
    }

    .movie-card {
        background: rgba(30, 30, 45, 0.9);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 18px;
        padding: 25px;
        margin-top: 20px;
        box-shadow: 0 10px 35px rgba(0,0,0,0.25);
    }

    .movie-title {
        font-size: 2rem;
        font-weight: 800;
        color: #ffffff;
        margin-bottom: 5px;
    }

    .movie-meta {
        color: #a9a9b8;
        font-size: 1rem;
        margin-bottom: 20px;
    }

    .info-box {
        background: rgba(255,255,255,0.04);
        border-radius: 12px;
        padding: 15px;
        margin-bottom: 12px;
    }

    .info-label {
        color: #8f8fa3;
        font-size: 0.8rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 5px;
    }

    .info-value {
        color: #ffffff;
        font-size: 1rem;
        font-weight: 500;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 48px;
        font-weight: 700;
        font-size: 1rem;
        border: none;
        background: linear-gradient(90deg, #ff4b4b, #ff7043);
        color: white;
    }

    div.stButton > button:hover {
        background: linear-gradient(90deg, #ff3838, #ff5722);
        color: white;
    }

    textarea {
        border-radius: 14px !important;
    }

    footer {
        visibility: hidden;
    }
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Model
# ---------------------------------------------------------

model = ChatMistralAI(
    model="mistral-small-2506"
)

# ---------------------------------------------------------
# Pydantic Model
# ---------------------------------------------------------

class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(
    pydantic_object=Movie
)

# ---------------------------------------------------------
# Prompt
# ---------------------------------------------------------

prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
        Extract movie information from paragraph.

        {format_instructions}
        """
    ),
    (
        "human",
        "{paragraph}"
    )
])

# ---------------------------------------------------------
# UI
# ---------------------------------------------------------

st.markdown("""
<div class="hero">
    <h1>🎬 Movie Information Extractor</h1>
    <p>Extract structured movie information from any paragraph</p>
</div>
""", unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">Movie Paragraph</div>',
    unsafe_allow_html=True
)

para = st.text_area(
    label="Movie paragraph",
    placeholder=(
        "Paste a paragraph containing information about a movie..."
    ),
    height=220,
    label_visibility="collapsed"
)

st.write("")

extract = st.button("🎬 Extract Movie Information")

# ---------------------------------------------------------
# Extraction
# ---------------------------------------------------------

if extract:

    if not para.strip():
        st.warning("Please enter a movie paragraph first.")

    else:

        with st.spinner("Extracting movie information..."):

            try:

                final_prompt = prompt.invoke(
                    {
                        "paragraph": para,
                        "format_instructions":
                            parser.get_format_instructions()
                    }
                )

                response = model.invoke(final_prompt)

                movie = parser.parse(response.content)

                # -------------------------------------------------
                # Movie Result Card
                # -------------------------------------------------

                st.markdown(
                    '<div class="movie-card">',
                    unsafe_allow_html=True
                )

                st.markdown(
                    f'<div class="movie-title">🎬 {movie.title}</div>',
                    unsafe_allow_html=True
                )

                meta = []

                if movie.release_year:
                    meta.append(str(movie.release_year))

                if movie.rating is not None:
                    meta.append(f"⭐ {movie.rating}")

                if movie.genre:
                    meta.append(" • ".join(movie.genre))

                st.markdown(
                    f'<div class="movie-meta">{"  |  ".join(meta)}</div>',
                    unsafe_allow_html=True
                )

                col1, col2 = st.columns(2)

                with col1:

                    st.markdown(
                        f"""
                        <div class="info-box">
                            <div class="info-label">Director</div>
                            <div class="info-value">
                                {movie.director or "Not available"}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class="info-box">
                            <div class="info-label">Genres</div>
                            <div class="info-value">
                                {", ".join(movie.genre) if movie.genre else "Not available"}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="info-box">
                            <div class="info-label">Cast</div>
                            <div class="info-value">
                                {", ".join(movie.cast) if movie.cast else "Not available"}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                    st.markdown(
                        f"""
                        <div class="info-box">
                            <div class="info-label">Release Year</div>
                            <div class="info-value">
                                {movie.release_year or "Not available"}
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"""
                    <div class="info-box">
                        <div class="info-label">Summary</div>
                        <div class="info-value">
                            {movie.summary}
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("</div>", unsafe_allow_html=True)

            except Exception as e:

                st.error(
                    f"Unable to extract movie information: {e}"
                )