import streamlit as st
import os
import datetime

def main():
    st.set_page_config(page_title="Udaysinh's Blog Site", layout="wide", initial_sidebar_state="auto", page_icon="📝")
    st.title("Uday's Blogs !")
    
    # Initialize session state for filter visibility
    if 'show_filters' not in st.session_state:
        st.session_state.show_filters = False
    
    # Button to toggle filters
    if st.button("🔍 Filters"):
        st.session_state.show_filters = not st.session_state.show_filters
    
    # Default filter values
    search_query = ""
    filter_author = "All"
    filter_date = datetime.date.today()
    filter_category = "All"
    filter_tags = []
    
    # Filter section
    if st.session_state.show_filters:
        st.markdown("### Filters")
        search_query = st.text_input("Search blog posts")
        filter_author = st.selectbox("Filter by author", ["All", "Udaysinh"])
        filter_date = st.date_input("Filter by date", datetime.date.today())
        filter_category = st.selectbox("Filter by category", ["All", "Technology", "Education", "Lifestyle"])
        filter_tags = st.multiselect("Filter by tags", ["AI", "Python", "Streamlit", "Data Science"])
    
    # Custom CSS for card styling
    st.markdown(
        """
        <style>
        .card {
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            color: #333; /* Default text color */
        }
        .card-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .card-meta {
            font-size: 14px;
            color: #888;
            margin-bottom: 10px;
        }
        .card-preview {
            font-size: 16px;
            margin-bottom: 10px;
        }
        .card-button {
            background-color: #ff6347;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .card-button:hover {
            background-color: #ff4500;
        }
        /* Dark mode adjustments */
        @media (prefers-color-scheme: dark) {
            .card {
                background-color: #333;
                color: #f9f9f9; /* Light text color for dark mode */
            }
            .card-meta {
                color: #bbb;
            }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Display blog posts as cards
    st.subheader("Blog Posts")
    markdown_folder = 'markdown'
    markdown_files = [f for f in os.listdir(markdown_folder) if f.endswith('.md')]
    
    for md_file in markdown_files:
        with open(os.path.join(markdown_folder, md_file), 'r', encoding='utf-8') as file:
            content = file.read()
            lines = content.split('\n')
            title = lines[0].replace('# ', '') if lines[0].startswith('# ') else 'Untitled'
            preview = '\n'.join(lines[1:6])  # Show first 5 lines as preview
            date = datetime.datetime.now().strftime("%Y-%m-%d")  # Example date, you can customize this
            author = "Udaysinh"  # Example author, you can customize this
            category = "Technology"  # Example category, you can customize this
            tags = ["AI", "Python"]  # Example tags, you can customize this
            
            # Apply search and filter
            if (search_query.lower() in title.lower() and 
                (filter_author == "All" or filter_author == author) and 
                filter_date <= datetime.datetime.now().date() and 
                (filter_category == "All" or filter_category == category) and 
                (not filter_tags or any(tag in tags for tag in filter_tags))):
                
                with st.container():
                    st.markdown(f"""
                    <div class="card">
                        <div class="card-title">{title}</div>
                        <div class="card-meta">Date: {date} | Author: {author} | Category: {category} | Tags: {', '.join(tags)}</div>
                        <div class="card-preview">{preview}...</div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Read more button
                    if st.button(f"Read more about {title}", key=md_file):
                        st.query_params.post = md_file
                        st.rerun()
                    
                    st.markdown("---")  # Separator between posts

def detail_page(md_file):
    st.set_page_config(page_title="Blog Post", layout="wide", initial_sidebar_state="auto", page_icon="📝")
    st.markdown('<a name="section-1"></a>', unsafe_allow_html=True)
    st.title("Blog Post")
    
    # Back arrow button
    if st.button("⬅️ Back to Blog Posts"):
        st.query_params.clear()
        st.rerun()
    
    markdown_folder = 'markdown'
    with open(os.path.join(markdown_folder, md_file), 'r', encoding='utf-8') as file:
        content = file.read()
        st.markdown(content)
    
    # Back to Top button
    st.markdown('''
        <a target="_self" href="#section-1">
            <button>⬆️ Back to Top</button>
        </a>
        ''', unsafe_allow_html=True)

if __name__ == '__main__':
    query_params = st.query_params
    if 'post' in query_params:
        detail_page(query_params['post'])
    else:
        main()