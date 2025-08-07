import os
import streamlit as st
from app.prompt import get_prompt
from app.llm import get_llm
from app.retriever import get_retriever
from app.rag_chain import build_chain

st.set_page_config(page_title="Advanced RAG Chatbot")

st.title(" Advanced RAG Chatbot")

provider = st.selectbox("Choose LLM Provider", ["Groq", "HuggingFace"])
answer_type = st.selectbox("Select Answer Type", ["Short", "Detailed"])

prompt_input = st.chat_input("Ask your question...")

if 'messages' not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg['role']).markdown(msg['content'])

if prompt_input:
    st.chat_message("user").markdown(prompt_input)
    st.session_state.messages.append({'role': 'user', 'content': prompt_input})

    try:
        prompt_template = get_prompt(answer_type)
        retriever = get_retriever()
        llm = get_llm(provider)

        qa_chain = build_chain(llm, retriever, prompt_template)
        response = qa_chain.invoke({'query': prompt_input})

        result = response['result']
        sources = response["source_documents"]

        if answer_type == "Detailed":
            sources_text = "\n".join(
                f"- Page {doc.metadata.get('page', '?')} from `{os.path.basename(doc.metadata.get('source', ''))}`"
                for doc in sources
            )
            result += f"\n\n**Sources:**\n{sources_text}"

        st.chat_message("assistant").markdown(result)
        st.session_state.messages.append({'role': 'assistant', 'content': result})
    except Exception as e:
        st.error(f"Error: {str(e)}")
