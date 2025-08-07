from langchain_core.prompts import PromptTemplate

SHORT_PROMPT = """
Answer the question based only on the context. Avoid unnecessary info.

Context: {context}
Question: {question}
"""

DETAILED_PROMPT = """
Answer based only on the provided context. Explain thoroughly.

Context: {context}
Question: {question}
"""

def get_prompt(answer_type="Short"):
    template = SHORT_PROMPT if answer_type == "Short" else DETAILED_PROMPT
    return PromptTemplate(template=template, input_variables=["context", "question"])
