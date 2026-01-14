from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import load_prompt

load_dotenv()

# Model
model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.3
)

# UI
st.header("Research Paper Summarizer")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis"
    ]
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner Friendly", "Technical", "Code-Oriented", "Mathematical", "Creative"]
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"]
)

# Prompt Template
template = load_prompt("template.json")
if st.button("Summarize"):
    with st.spinner("Generating summary..."):
        # prompt = template.invoke({
        #   "paper_input": paper_input,
        #   "style_input": style_input,
        #   "length_input": length_input
        # })
        # result = model.invoke(prompt)

        chain = template | model
        result = chain.invoke({
          "paper_input": paper_input,
          "style_input": style_input,
          "length_input": length_input
        })
        st.write(result.content)
