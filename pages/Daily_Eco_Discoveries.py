import streamlit as st 
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain_community.utilities import WikipediaAPIWrapper

st.markdown("<h2 style='color: green; font-style: italic; font-family: Comic Sans MS; ' >EcoKids Hub Daily 🌿🎨Discoveries</h2> <h3 style='color: #ADFF2F; font-style: italic; font-family: Comic Sans MS; font-size:2rem'>🌍🌱 Exploring the EcoVerse: Your Daily Thought 💭 and Activity 🎨 for a Greener Tomorrow! 🌿🌈</h3>", unsafe_allow_html=True)


thought_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Give a {topic} for kids related to sustainable environment and how they can protect the nature.'
)

activity_template = PromptTemplate(
    input_variables = ['topic'], 
    template='Suggest one {topic} to do for kids related to sustainable environment and how they can protect the nature.'
)

# Llms
llm = OpenAI(temperature=0.9) 


thought_chain = LLMChain(llm=llm, prompt=thought_template, verbose=True, output_key='thought')
activity_chain = LLMChain(llm=llm, prompt=activity_template, verbose=True, output_key='activity')

# Show stuff to the screen if there's a prompt
st.markdown("<p style='color: #4FC978; font-style: italic; font-family: Comic Sans MS; ' >'Click 👇 to get the Thought for the day' </p>", unsafe_allow_html=True)
if st.button("Thought for the day"): 
    prompt = "thought for the day"
    thought = thought_chain.run(prompt)
    st.write(thought) 

st.markdown("<p style='color: #4FC978; font-style: italic; font-family: Comic Sans MS; ' >'Click 👇 to get the daily activity' </p>", unsafe_allow_html=True)
if st.button("Daily Activity"): 
    prompt = "activity"
    activity = activity_chain.run(prompt)
    st.write(activity) 
