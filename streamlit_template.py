# app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Matt Foster AI Demo App - Generated with ChatGPT 4.0", layout="wide")

# -------------------------
# 1. TITLE & DESCRIPTION
# -------------------------
st.title("🚀 AI + Data Demo App")
st.markdown("This app shows **Streamlit essentials**: text, charts, widgets, file upload, caching, and a model stub.")

# -------------------------
# 2. BASIC DISPLAY
# -------------------------
st.subheader("📊 Example Data")
df = pd.DataFrame({"x": [1, 2, 3, 4, 5], "y": [10, 20, 30, 25, 15]})
st.write(df)
st.line_chart(df)

# -------------------------
# 3. WIDGETS
# -------------------------
st.subheader("🎛️ User Input")
name = st.text_input("Enter your name", "Data Scientist")
age = st.slider("Pick your age", 0, 100, 30)
st.write(f"Hello **{name}**, you are {age} years old!")

# -------------------------
# 4. PLOTLY CHART
# -------------------------
st.subheader("📈 Interactive Plotly Chart")
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length", color="species", title="Iris Dataset")
st.plotly_chart(fig, use_container_width=True)

# -------------------------
# 5. FILE UPLOAD / DOWNLOAD
# -------------------------
st.subheader("📂 File Upload & Download")
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")
if uploaded_file:
    user_df = pd.read_csv(uploaded_file)
    st.write(user_df.head())

    # Download same file back
    st.download_button("Download as CSV",
                       user_df.to_csv(index=False).encode("utf-8"),
                       file_name="processed.csv")

# -------------------------
# 6. CACHING
# -------------------------
@st.cache_data
def load_big_dataset():
    # Pretend this is expensive
    return pd.DataFrame({"a": range(1000), "b": range(1000, 2000)})

if st.checkbox("Load big dataset"):
    big_df = load_big_dataset()
    st.write(big_df.head())

# -------------------------
# 7. AI MODEL INTEGRATION (Stub)
# -------------------------
st.subheader("🤖 AI Model Demo (Stub)")
prompt = st.text_area("Ask the AI something:", "What is Streamlit?")
if st.button("Generate"):
    # Replace with your real model (OpenAI, Hugging Face, custom ML model, etc.)
    fake_answer = f"🔮 Pretend AI Answer to: '{prompt}'"
    st.write(fake_answer)