from langchain_core.prompts import PromptTemplate

# Prompt Template
template = PromptTemplate(
    template="""
You are an AI research assistant.

Summarize the research paper titled "{paper_input}" with the following constraints:

Explanation Style: {style_input}
Explanation Length: {length_input}

Requirements:
- Include mathematical details only if they are central to the paper
- Explain math concepts with intuitive explanations or simple pseudocode
- Use analogies where helpful
- Do NOT hallucinate details
- If required information is unavailable, say: "Insufficient information available"

Produce a clear, accurate, and well-structured summary.
""",
    input_variables=["paper_input", "style_input", "length_input"],
    validate_template=True
)

template.save("template.json")