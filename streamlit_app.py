import pandas as pd
import streamlit as st


# Page setup
st.set_page_config(page_title="CACI Intern Search Engine", page_icon="🐍", layout="wide")
st.title("CACI Intern Search Engine")

# Connect to the Google Sheet
sheet_id = "1VIFY0PfqeePEeKtzsyFuwpGpNvyKaylsaCea8aXUajE"
sheet_name = "caci"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
df = pd.read_csv(url, dtype=str).apply(lambda x: x.astype(str).str.lower())



# Use a text_input to get the keywords to filter the dataframe
text_search = st.text_input("Search information by keywords", value="")

# Filter the dataframe using masks
m1 = df["Topic"].str.contains(text_search)
m2 = df["Information"].str.contains(text_search)
df_search = df[m1 | m2]

# Another way to show the filtered results
# Show the cards
N_cards_per_row = 3
if text_search:
    for n_row, row in df_search.reset_index().iterrows():
        i = n_row%N_cards_per_row
        if i==0:
            st.write("---")
            cols = st.columns(N_cards_per_row, gap="large")
        # draw the card
        with cols[n_row%N_cards_per_row]:
            st.caption(f"{row['Topic'].strip()} - {row['Date Updated'].strip()}")
            st.markdown(f"**{row['Topic'].strip()}**")
            st.markdown(f"*{row['Information'].strip()}*")
            st.markdown(f"**{row['Links']}**")


