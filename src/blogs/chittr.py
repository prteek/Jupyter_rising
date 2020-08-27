import streamlit as st
def run():
    st.title("Chittr")    
    st.markdown("""##""")
    
    #5
    st.markdown("""**N** is never enough because if it were *enough* you'd already be on to the next problem for which you need more data.  
    - Andre Gelman, on sample size. 
    
---
""")
    
    #4
    st.markdown("""The tougher the question the easier it is dismissed. When we be facing an easy dismissal, it be worth asking “was the problem even well understood?”
    
---
""")
    
    #3
    html_string = """<blockquote class="twitter-tweet"><p lang="en" dir="ltr">So I guess <a href="https://twitter.com/hashtag/data?src=hash&amp;ref_src=twsrc%5Etfw">#data</a> is knowledge but <a href="https://twitter.com/hashtag/code?src=hash&amp;ref_src=twsrc%5Etfw">#code</a> is wisdom 🤔 <a href="https://t.co/bzYppH6bQo">https://t.co/bzYppH6bQo</a></p>&mdash; Prateek (@prateekpatel_in) <a href="https://twitter.com/prateekpatel_in/status/1284201607488569348?ref_src=twsrc%5Etfw">July 17, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    
---
"""
    st.markdown(html_string, unsafe_allow_html=True)
    
    #2
    html_string = """<blockquote class="twitter-tweet"><p lang="en" dir="ltr">Is it cannibalism to quit Task manager from Task manager ? 🤔</p>&mdash; Prateek (@prateekpatel_in) <a href="https://twitter.com/prateekpatel_in/status/1283337696669294592?ref_src=twsrc%5Etfw">July 15, 2020</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>
    
---
"""
    st.markdown(html_string, unsafe_allow_html=True)
    
    #1
    st.markdown("""Is it just me or the [#AvengersEndgame](https://twitter.com/search?q=%23avengersendgame&src=typed_query) storyline is like a typical [@github](https://twitter.com/github) project evolution ?🤷🏻
 """)
    
