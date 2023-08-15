import streamlit as st
from langchain.llms import OpenAI

st.title('Curious about Election Candidates. ASK ME.')
st.write("Disclaimer : This is Experimental USER need to verify the information.")
st.write("ASK ME is not responsible for wrong answers or incorrect infomation.")
st.write("Use at your own risk.")

#openai_api_key = st.sidebar.text_input('Enter OPEN API key')

openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
    query = f"""what is important issue in   Nassau County regarding upcoming election.
   categorize them from most important to least important.
   Summarize why they are important. 
   what are election candidates saying about these show candidate name and Reponses on above issues?
    """
    text = st.text_area('Enter text:', query)
    submitted = st.form_submit_button('Submit')
    if not openai_api_key.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)