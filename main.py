import streamlit as st
import random as rand
import generate

n = 10
questions = generate.math01(n)
for number in range(1, n+1):
  st.markdown(f'# Nomor {number}')
  st.markdown(questions[number-1])