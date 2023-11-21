import streamlit as st
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

def read_tsv(file_path):
    return pd.read_csv(file_path, sep='\t')
df_bible = read_tsv('data.tsv')


def keyword_filter_dataframe(dataframe, filter_col, keyword):
    filtered_df = dataframe[dataframe[filter_col].str.contains(keyword, flags=re.IGNORECASE, regex=True)]
    return filtered_df

def df_read_bible(df): # for read_bible_page. requirement 1.1.1
    return df[['Book Name', 'Chapter', 'Verse', 'Text_NET']]

def generate_wordcloud(data):
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(data)
    st.image(wordcloud.to_image())


def main():
    st.set_page_config(page_title="Voyager", layout="wide")

    # @st.cache

    def read_bible_page():
        st.title("Read.")
        st.write(df_read_bible(df_bible))
    

    def search_bible():
        st.title("Ask.")
        
        keyword = st.text_input("Search:", key=1)

        if keyword:
            filtered_df = keyword_filter_dataframe(df_bible, "Text_NET", keyword)
            st.write(len(filtered_df))
            st.dataframe(df_read_bible(filtered_df))

            # Add a button to generate the WordCloud
            if st.button('Generate WordCloud'):
                # Call the generate_wordcloud function with the desired data
                generate_wordcloud(' '.join(filtered_df['Text_NET'].dropna().astype(str)))
            
            keyword = st.text_input("Search:", key=2)

            if keyword:
                filtered_df = keyword_filter_dataframe(df_bible, "Text_NET", keyword)
                st.write(len(filtered_df))
                st.dataframe(df_read_bible(filtered_df))

                # Add a button to generate the WordCloud
                if st.button('Generate WordCloud'):
                    # Call the generate_wordcloud function with the desired data
                    generate_wordcloud(' '.join(filtered_df['Text_NET'].dropna().astype(str)))
                
                # WIP: identical issue
                # keyword = st.text_input("Search:", key=3)
                # if keyword:
                #     filtered_df = keyword_filter_dataframe(df_bible, "Text_NET", keyword)
                #     st.write(len(filtered_df))
                #     st.dataframe(df_read_bible(filtered_df))

                #     # Add a button to generate the WordCloud
                #     if st.button('Generate WordCloud'):
                #         # Call the generate_wordcloud function with the desired data
                #         generate_wordcloud(' '.join(filtered_df['Text_NET'].dropna().astype(str)))

    pages = {
        "Read Bible": read_bible_page,
        "Search Bible": search_bible,
    }

    st.sidebar.title("Bible Searcher")
    page = st.sidebar.radio("Select a page", tuple(pages.keys()))

    pages[page]()

if __name__ == "__main__":
    main()