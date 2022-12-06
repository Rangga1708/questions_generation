import streamlit as st
import random as rand

def math01(n):
  questions = set()
  for number in range(1,n+1):
    num1 = rand.randint(1,9)
    num2 = rand.randint(1,9)
    eq = (rf'''$\displaystyle \lim_{{x \to \infty}} \frac{{x+{num1}}}{{x+{num2}}}$''')
    questions.add(f'''Nilai dari {eq} adalah ....''')
  questions = list(questions)
  rand.shuffle(questions)
  return questions