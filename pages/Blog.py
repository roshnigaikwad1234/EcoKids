# import streamlit as st
# import pandas as pd

# def create_blog_card(title, content):
#     """
#     Function to create a card with the blog title and content.
#     """
#     st.write(f"## {title}")
#     st.write(content)

# def main():
#     st.set_page_config(page_title="Blogs Page", page_icon="✍️")

#     st.title("Welcome to the Blogs Page!")

#     # Initialize an empty list to store the blogs
#     blog_data = []

#     # Input widgets to get the blog title and content from the user
#     blog_title = st.text_input("Enter Blog Title:")
#     blog_content = st.text_area("Write your Blog:")

#     # Submit button to add the blog to the list
#     if st.button("Submit Blog"):
#         blog_data.append({"Title": blog_title, "Content": blog_content})
#         st.success("Blog Submitted Successfully!")

#     # Display the blogs in card format
#     st.subheader("Blogs:")
#     for blog in blog_data:
#         create_blog_card(blog["Title"], blog["Content"])

# if __name__ == "__main__":
#     main()



import streamlit as st
import pandas as pd

def create_blog_card(title, content):
    """
    Function to create a card with the blog title and content.
    """
    st.write(f"## {title}")
    st.write(content)

def main():
    st.set_page_config(page_title="Blogs Page", page_icon="✍️")
    
    st.markdown("<h2 style='color: green; font-style: italic; font-family: Comic Sans MS; ' >EcoKids Hub Blogs Page! ✍️</h2>", unsafe_allow_html=True)

    # Initialize an empty list to store the blogs
    blog_data = []

    # Input widgets to get the blog title and content from the user
    blog_title = st.text_input("## _:green[Enter Blog Title]_ ✏️:")
    blog_content = st.text_area("## _:green[Write your Blog]_ 📜:")

    # Submit button to add the blog to the list
    if st.button("Submit Blog"):
        blog_data.append({"Title": blog_title, "Content": blog_content})
        st.success("Blog Submitted Successfully!")

    # Display the blogs in card format
    st.markdown("<h2 style='color: green; font-style: italic; font-family: Comic Sans MS; ' >Your Blogs 📚 </h2>", unsafe_allow_html=True)

    for blog in blog_data:
        create_blog_card(blog["Title"], blog["Content"])

if __name__ == "__main__":
    main()

