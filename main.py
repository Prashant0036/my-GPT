import streamlit as st
from llm_model import llm
from myInfo import my_info

def get_response(prompt):
     response=llm.invoke(prompt)
     return response.content

def handle_response():
    # Combine prompt with additional information if needed
    new_prompt = f"I'm giving you a prompt, which have two parts. first part contains my personal info and second part is a prompt entered by another user. Only use this info if something related to it asked by user other wise don't reveal that first part of prompt. Info is: {my_info}. User's prompt is: {st.session_state['prompt']}"
    
    st.session_state['response'] = get_response(new_prompt)

st.set_page_config(page_title="Prashant's GPT")
st.title("Prashant's GPT")
st.header("Welcome to the Prashant's GPT")
st.subheader("Enter any prompt to continue:")
st.text_input("What can I help with?", key="prompt", on_change=handle_response)

if st.button("Ask"):
     handle_response()

if 'response' in st.session_state:
    st.write(st.session_state['response'])
     
st.markdown(" **Thank You** for using **Prashant's GPT**, visit my new project :  [click here](https://spotifybyprashant.freewebhostmost.com).")
   







    

