import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from langchain_openai import ChatOpenAI
import os

st.set_page_config(page_title="AI Data Analyst", layout="wide")


OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
st.title("📊 AI Data Analyst")

# Sidebar
with st.sidebar:
    st.header("Upload Dataset")
    file = st.file_uploader("Upload CSV", type=["csv"])

# Initialize chat memory
if "messages" not in st.session_state:
    st.session_state.messages = []

# Load dataset
if file is not None:

    df = pd.read_csv(file, encoding="latin-1")

    # Sidebar dataset preview
    with st.sidebar:
        st.subheader("Dataset Preview")
        st.dataframe(df.head())

        st.subheader("Dataset Info")
        st.write("Rows:", df.shape[0])
        st.write("Columns:", df.shape[1])

    # Summary cards
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Rows", df.shape[0])

    with col2:
        st.metric("Columns", df.shape[1])

    with col3:
        st.metric("Missing Values", df.isna().sum().sum())

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):

            if isinstance(message["content"], pd.DataFrame):
                st.dataframe(message["content"])

            elif isinstance(message["content"], pd.Series):
                st.dataframe(message["content"])

            else:
                st.markdown(message["content"])
    user_question = st.chat_input("Ask a question about your dataset")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0,
        openai_api_key=OPENAI_API_KEY
    )

    if user_question:

        st.session_state.messages.append(
            {"role": "user", "content": user_question}
        )

        with st.chat_message("user"):
            st.markdown(user_question)

        with st.chat_message("assistant"):

            with st.spinner("Analyzing dataset..."):

                prompt = f"""
You are a Python data analyst using pandas.

Dataframe name: df

Columns:
{df.columns.tolist()}

Sample data:
{df.head().to_string()}

Rules:
- Use only pandas
- Store the final answer in variable result
- If a chart is needed, store the figure in variable fig
- Return only executable python code

Question:
{user_question}
"""

                response = llm.invoke(prompt)

                code = response.content.strip()
                code = code.replace("```python", "").replace("```", "")

                local_vars = {"df": df, "plt": plt, "sns": sns}

                try:
                    exec(code, {}, local_vars)

                    if "result" in local_vars:
                        st.write(local_vars["result"])
                        st.session_state.messages.append(
                            {"role": "assistant", "content": local_vars["result"], "type": "data"}
                        )

                    if "fig" in local_vars:
                        st.pyplot(local_vars["fig"])

                except Exception as e:
                    st.write("Error executing generated code.")
                    st.code(code)
                    st.write(e)