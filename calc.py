import streamlit as st

#1 usage
class buttons:
    def __init__(self,button_name):
        if st.button(f"Button Number is{button_name}"):
            self.calc(button_name*button_name)

    def calc(self,num):
        if num % 2 == 0:
            st.balloons()
        else:
            st.snow()

for i in range(10):
    buttons(i)
