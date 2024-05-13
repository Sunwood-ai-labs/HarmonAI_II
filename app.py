import streamlit as st
from harmon_ai import HarmonAI
# from templates.header import show_header
# from templates.sidebar import show_sidebar
# from templates.footer import show_footer

def main():
    
    if st.button("Generate README"):
        pass
    #     readme_text = HarmonAI.generate_readme(repo_name, owner_name, package_name, icon_url, title, subtitle, important_message)
    #     st.markdown(readme_text)
    # show_footer()

if __name__ == "__main__":
    main()