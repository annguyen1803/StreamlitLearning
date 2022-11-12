import streamlit as st

st.set_page_config(
    page_title="An App",
    page_icon=":shark:"
)

st.header('Page 1 header')
st.subheader('Subheader page 1')
st.markdown('Hello **world**!')
st.latex('\int a x^2 \,dx')
st.metric('My metric', 55,-5)
tab1, tab2, tab3 = st.tabs(["Tab 1","Tab 2","TAB 3"])

tab1 = tab1.container()
tab1.multiselect('buy',[1,2,3])
tab1.write('tab 1 content eeeeee')

with tab2.container():
    st.write('tab 2 content here')
    st.color_picker("pick color")

with tab3.container():
    with st.form(key='tap3_form'):
        userN = st.text_input('Username: ')
        passW = st.text_input('Password: ')
        st.form_submit_button('Loginnnn')