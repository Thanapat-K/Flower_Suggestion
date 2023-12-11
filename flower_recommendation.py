
import streamlit as st
import openai
import json
import pandas as pd

# Get the API key from the sidebar called OpenAI API key
user_api_key = st.sidebar.text_input("OpenAI API key", type="password")

client = openai.OpenAI(api_key=user_api_key)
prompt = """Act as an florist. You will receive a description and you should give suggestions of flowers in English that match those description.
            List the suggestions in a JSON array, one example per line.
            Each example should have 2 fields:
            - "Name" - the flower suggested
            - "Meaning" - the meaning of that flower
            - "Explaination" - what people use that flower for
            Don't say anything at first. Wait for the user to say something."""  


st.title(':sunflower: :green[Flower] Suggestion :blossom:')
st.markdown('Write a describtion or meaning of a flower you want. \n\
            The AI will give you some suggestions.')

user_input = st.text_area("Enter your description:", "Your text here")


# submit button after text input
if st.button('Submit'):
    messages_so_far = [
        {"role": "system", "content": prompt},
        {'role': 'user', 'content': user_input},
    ]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages_so_far
    )
    # Show the response from the AI in a box
    st.markdown('**AI response:**')
    suggestion_dictionary = response.choices[0].message.content


    sd = json.loads(suggestion_dictionary)

    print (sd)
    suggestion_df = pd.DataFrame.from_dict(sd)
    print(suggestion_df)
    st.table(suggestion_df)

