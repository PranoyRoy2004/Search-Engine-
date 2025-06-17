import streamlit as st
from exa_py import Exa

# Initialize Exa with your API key
exa = Exa('Your Exa API key')

# UI Layout
st.title("🔍 Custom Exa Search Engine")
query = st.text_input("Enter your search query")

if st.button("Search") and query:
    with st.spinner("Searching..."):
        try:
            response = exa.search(
                query,
                num_results=5,
                type='keyword',
                include_domains=['https://www.google.com'],
            )

            if not response.results:
                st.warning("No results found.")
            else:
                for result in response.results:
                    st.subheader(result.title)
                    st.markdown(f"[Visit Link]({result.url})")

        except Exception as e:
            st.error(f"Error: {e}")
