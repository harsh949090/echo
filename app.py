import streamlit as st
import torch
import scipy.io.wavfile
import numpy as np
from transformers import pipeline, AutoProcessor, BarkModel

# --- AI Model Functions ---
# Use Streamlit's cache to load the text rewriting model only once
@st.cache_resource
def get_rewriting_pipeline():
    # This is a pre-trained model for text-to-text generation
    return pipeline("text2text-generation", model="google/flan-t5-base")

def rewrite_text(text, tone):
    llm_pipeline = get_rewriting_pipeline()
    # This is the prompt that instructs the AI on how to rewrite the text
    prompt = f"""
Rewrite the following text in a {tone} tone. The rewritten text should retain the original meaning but reflect the new sentiment.

Original Text:
{text}

Rewritten Text:
    """
    rewritten_output = llm_pipeline(prompt, max_length=len(text.split()) + 50, num_return_sequences=1)
    return rewritten_output[0]['generated_text'].strip()

# Use Streamlit's cache to load the Bark TTS model only once
@st.cache_resource
def get_tts_model_bark():
    processor = AutoProcessor.from_pretrained("suno/bark")
    model = BarkModel.from_pretrained("suno/bark")
    return processor, model

def generate_audio_bark(text):
    processor, model = get_tts_model_bark()
    inputs = processor(text)
    waveform = model.generate(**inputs)
    waveform_np = waveform.cpu().numpy().squeeze()
    sampling_rate = model.generation_config.sample_rate
    return waveform_np, sampling_rate

# --- User Interface Layout ---
st.set_page_config(page_title="EchoVerse", layout="wide")

st.title("EchoVerse - An AI Audiobook Creation Tool")
st.markdown("""
_EchoVerse transforms your text into expressive, downloadable audio content. 
It's designed for accessibility and content reusability, empowering you to create 
natural-sounding narrations with a customizable tone and voice._
""")

st.header("1. Input Your Content")
original_text = st.text_area("Enter your text here:", height=200)

col1, col2 = st.columns(2)
with col1:
    tone = st.selectbox("Select Narration Tone:", ["Neutral", "Suspenseful", "Inspiring"])
with col2:
    voice = st.selectbox("Select Voice:", ["Voice 1 (Male)", "Voice 2 (Female)"])

# --- Main Logic for Generation ---
if st.button("Generate Audiobook"):
    if original_text:
        with st.spinner("Rewriting and generating audio..."):
            # Step 4: Rewrite Text
            rewritten_text = rewrite_text(original_text, tone)
            
            # Step 5: Generate Audio using the Bark model
            waveform, sampling_rate = generate_audio_bark(rewritten_text)
            
            # Save audio to a temporary file
            scipy.io.wavfile.write("audiobook.wav", sampling_rate, waveform)
        
        st.success("Audiobook generated successfully! 🎉")

        st.header("2. Side-by-Side Comparison")
        col_orig, col_new = st.columns(2)
        with col_orig:
            st.subheader("Original Text")
            st.write(original_text)
        with col_new:
            st.subheader(f"Rewritten ({tone})")
            st.write(rewritten_text)

        st.header("3. Play and Download Your Audiobook")
        st.audio("audiobook.wav", format="audio/wav")
        
        with open("audiobook.wav", "rb") as file:
            st.download_button(
                label="Download as WAV",
                data=file,
                file_name="audiobook.wav",
                mime="audio/wav"
            )
    else:
        st.warning("Please enter some text to begin.")