import streamlit as st
import streamlit.components.v1 as components

def about_streamlit():
  st.markdown("# A Little Bit About Streamlit...")
  st.markdown("SLR would like to thank the very kind and brilliant people at [streamlit](https://streamlit.io/) for their amazing python package and app hosting as well as the additional resources provided for the course, **FREE OF CHARGE!**")
  st.text("")
  text = "While us geologists are not trained programmers, we often find ourselves producing custom workflows in one or another programming language. "
  text += "We produce novel solutions to difficult problems that commercial software packages cannot cater for. "
  text += "We provide reproducible scripts to peers and clients in difficult to use and outdated interfaces embedded in the commercial packages, "
  text += "often coded in difficult, syntax sensitive non-readable languages. "
  text += "Streamlit provides us with an easy to use solution that takes seconds to get yourself up and running. "
  text += "All the basic widgets you will need along with all the fun stuff that python has to offer. "
  st.markdown(text)
  st.text("")
  st.markdown("See the video below for an example of using Python and [Streamlit](https://streamlit.io/) in [Datamine](https://www.dataminesoftware.com/). Skip to minute 10 for the [streamlit](https://streamlit.io/) demonstration.")
  
  st.video('https://youtu.be/wL8niCeXwPI')
  components.html(
    '''
    <iframe src="https://publicscenes.seequent.com/f8f2fc71-713c-4b48-b708-4073b150d511" width=800 height=650 allowfullscreen></iframe>
    ''', height=600)
 
