from pathlib import Path
import pickle

import numpy as np
import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


APP_DIR = Path(__file__).resolve().parent
TOKENIZER_PATH = APP_DIR / "tokenizer.pkl"
MAX_LEN_PATH = APP_DIR / "max_len.pkl"
MODEL_CANDIDATES = ("model.h5", "lstm_model.h5")


@st.cache_resource(show_spinner="Loading LSTM model and tokenizer...")
def load_artifacts():
    if not TOKENIZER_PATH.exists():
        raise FileNotFoundError(f"Tokenizer file not found: {TOKENIZER_PATH}")
    if not MAX_LEN_PATH.exists():
        raise FileNotFoundError(f"max_len file not found: {MAX_LEN_PATH}")

    model_path = next((APP_DIR / name for name in MODEL_CANDIDATES if (APP_DIR / name).exists()), None)
    if model_path is None:
        expected = ", ".join(MODEL_CANDIDATES)
        raise FileNotFoundError(f"Model file not found. Expected one of: {expected}")

    with TOKENIZER_PATH.open("rb") as tokenizer_file:
        tokenizer = pickle.load(tokenizer_file)

    with MAX_LEN_PATH.open("rb") as max_len_file:
        max_len = pickle.load(max_len_file)

    model = load_model(model_path)
    input_len = model.input_shape[1] if isinstance(model.input_shape, tuple) else None

    return tokenizer, int(max_len), model, input_len


def predict_next_word(text: str, tokenizer, model, sequence_len: int) -> str:
    sequence = tokenizer.texts_to_sequences([text])[0]
    padded = pad_sequences([sequence], maxlen=sequence_len, padding="pre")
    probs = model.predict(padded, verbose=0)[0]
    predicted_index = int(np.argmax(probs))
    return tokenizer.index_word.get(predicted_index, "")


def generate_text(seed_text: str, words_to_generate: int, tokenizer, model, sequence_len: int) -> str:
    generated_text = seed_text.strip()
    for _ in range(words_to_generate):
        next_word = predict_next_word(generated_text, tokenizer, model, sequence_len)
        if not next_word:
            break
        generated_text = f"{generated_text} {next_word}"
    return generated_text


def main():
    st.set_page_config(page_title="Next Word Predictor", page_icon="🧠", layout="centered")

    if "is_predicting" not in st.session_state:
        st.session_state.is_predicting = False
    if "generated_text" not in st.session_state:
        st.session_state.generated_text = ""
    if "pending_seed_text" not in st.session_state:
        st.session_state.pending_seed_text = ""
    if "pending_word_count" not in st.session_state:
        st.session_state.pending_word_count = 3

    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(180deg, #f8fbff 0%, #eef4ff 100%);
            }
            .app-title {
                text-align: center;
                font-size: 2.1rem;
                font-weight: 700;
                color: #1f2a44;
                margin-bottom: 0.25rem;
            }
            .app-subtitle {
                text-align: center;
                color: #4b587c;
                margin-bottom: 1.2rem;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown('<p class="app-title">🧠 LSTM Next Word Prediction</p>', unsafe_allow_html=True)
    st.markdown(
        '<p class="app-subtitle">Enter a phrase and let the model predict upcoming words.</p>',
        unsafe_allow_html=True,
    )

    try:
        tokenizer, max_len, model, model_input_len = load_artifacts()
    except FileNotFoundError as file_error:
        st.error(str(file_error))
        st.stop()
    except (pickle.UnpicklingError, OSError, ValueError) as load_error:
        st.error(f"Could not load model artifacts: {load_error}")
        st.stop()

    sequence_len = int(model_input_len) if model_input_len else max_len - 1
    if sequence_len <= 0:
        st.error("Invalid sequence length derived from model/max_len.")
        st.stop()

    seed_text = st.text_input("Seed text", placeholder="Type a phrase...")
    words_to_generate = st.slider("Words to generate", min_value=1, max_value=20, value=3)

    predict_clicked = st.button(
        "Predicting..." if st.session_state.is_predicting else "Predict",
        type="primary",
        use_container_width=True,
        disabled=st.session_state.is_predicting,
    )

    if predict_clicked:
        cleaned_seed = seed_text.strip()
        if not cleaned_seed:
            st.warning("Please enter seed text first.")
        else:
            st.session_state.pending_seed_text = cleaned_seed
            st.session_state.pending_word_count = words_to_generate
            st.session_state.is_predicting = True
            st.rerun()

    if st.session_state.is_predicting:
        with st.spinner("Predicting..."):
            st.session_state.generated_text = generate_text(
                seed_text=st.session_state.pending_seed_text,
                words_to_generate=st.session_state.pending_word_count,
                tokenizer=tokenizer,
                model=model,
                sequence_len=sequence_len,
            )
        st.session_state.is_predicting = False
        st.rerun()

    if st.session_state.generated_text:
        st.subheader("Generated text")
        st.success(st.session_state.generated_text)


if __name__ == "__main__":
    main()