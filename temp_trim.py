import streamlit as st

def main():
    st.title("News Article Display")
    html_code = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Bible Verses</title>
        <style>
            .verse {
                font-size: 18px;
                font-weight: bold;
                margin-bottom: 10px;
            }
            
            .reference {
                font-size: 14px;
                color: gray;
                margin-bottom: 20px;
            }
            
            .text {
                font-size: 16px;
                margin-bottom: 20px;
            }
        </style>
    </head>
    <body>
        <div class="verse">
            <div class="reference">John 3:16</div>
            <div class="text">For God so loved the world that he gave his one and only Son, that whoever believes in him shall not perish but have eternal life.</div>
        </div>
        
        <div class="verse">
            <div class="reference">Romans 8:28</div>
            <div class="text">And we know that in all things God works for the good of those who love him, who have been called according to his purpose.</div>
        </div>
        
        <div class="verse">
            <div class="reference">Philippians 4:13</div>
            <div class="text">I can do all this through him who gives me strength.</div>
        </div>
    </body>
    </html>
    """
    st.markdown(html_code, unsafe_allow_html=True)

if __name__ == "__main__":
    main()