from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate


# -----------------------------
# Model
# -----------------------------
model = ChatMistralAI(
    model="mistral-small-2506"
)


# -----------------------------
# Prompt
# -----------------------------
prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        """
You are a movie information extraction assistant.

Your task is to analyze a paragraph containing information about one or more movies
and extract the most useful and relevant information from it.

Extract the following information whenever available:

- Movie title
- Release year/date
- Genre
- Language
- Country
- Director
- Writers
- Producers
- Main cast and the characters they play
- Runtime
- Plot/story
- Rating and rating source
- Budget
- Box office
- Production company
- Awards and nominations
- Franchise/sequel information
- Major themes
- Important keywords
- Any other notable movie-related information

Rules:
1. Extract only information that is present in the given paragraph.
2. Never hallucinate or use outside knowledge.
3. If information is not available, write "Not provided".
4. Clearly distinguish actors from the characters they play.
5. If multiple movies are mentioned, extract information for each movie separately.
6. Keep the extracted information concise and useful.
7. Avoid unnecessary or irrelevant details.

After extracting the information, provide a short summary of the paragraph
in 2-4 sentences.

The summary should focus on the movie's main story, important characters,
genre, and other significant information.

Return the answer in a clear and well-organized format using headings and bullet points.
"""
    ),
    (
        "human",
        """
Here is the movie paragraph:

{para}

Extract the useful information and provide the summary.
"""
    )
])


# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(
    page_title="Movie Information Extractor",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 Movie Information Extractor")
st.write("Extract useful information and generate a quick summary from a movie paragraph.")

para = st.text_area(
    "Enter Movie Paragraph",
    height=250,
    placeholder="Paste your movie paragraph here..."
)

if st.button("Extract Information", type="primary"):
    if not para.strip():
        st.warning("Please enter a movie paragraph.")
    else:
        with st.spinner("Extracting movie information..."):
            final_prompt = prompt.invoke({
                "para": para
            })

            response = model.invoke(final_prompt)

        st.subheader("📋 Extracted Information")
        st.markdown(response.content)