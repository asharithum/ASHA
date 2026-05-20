import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MASTER_PROMPT = """
You are a professional International Marketing AI Strategist.

Product Name: {product_name}

Generate:
1. Global Product Title
2. Marketing Slogan
3. Three advertising descriptions:
   - Emotional Branding Expert
   - Luxury Brand Strategist
   - Digital Marketing Expert

Ensure:
- Global audience compatibility
- Persuasive marketing
- Emotional engagement
- Professional tone
"""

st.set_page_config(page_title="International Marketing AI", layout="centered")

st.title("🌍 International Business Marketing Prompt Application")

product_name = st.text_input("Enter Product Name")

if st.button("Generate Marketing Content"):

    if product_name:

        prompt = MASTER_PROMPT.format(product_name=product_name)

        with st.spinner("Generating..."):

            response = client.chat.completions.create(
                model="gpt-4.1-mini",
                messages=[
                    {"role": "system", "content": "You are an international marketing expert."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.9,
                max_tokens=1000
            )

            result = response.choices[0].message.content

            st.success("Marketing Content Generated!")

            st.write(result)

    else:
        st.warning("Please enter a product name.")
