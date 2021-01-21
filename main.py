######################
# Import libraries
######################

import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

######################
# Page Title
######################

print(pd.__version__)
print("panda")
print(st.__version__)
print("streamlit")
print(alt.__version__)
print("altair")


image = Image.open('header-logo.png')

st.image(image, use_column_width=True)

st.write("""
# DNA Base Counter 
Calculates composition of your DNA sequence and shows you how many of each bases you got!
***
""")


######################
# Input Text Box
######################

#st.sidebar.header('Enter DNA sequence')
st.header('Enter DNA sequence')

sequence_input = "Enter Sequence Here: \nTGCCGCGGGGTTGCCTTGCCTAGACGCAATGTCGGACGTATCGCTCTCGCCTCAACGGCTGCTGCTTCC\nGCTGCGACCCAAGACAGGCGGCGGTAGCCGCCTTTCGAAGGCGAGTCCTCCGCCTGTGACTAACTGTGCCAGATCGTCT\nCCAAACCCCCCATCCAGTTTAACTCACCAAACTATTGCGGTACAGACCCTAATCTCACGTCATATGACGCCAGTTGCCTCTGCCGAAATTCTGTCCTCAAGCGTTTTGGTCCG\nCCCCAGCGGTGCTGCCGATAAGGACCACCAAATCCGCATGTTACAGGACTTCTTATAAACTCTTTCTTCGTGGGG"

#sequence = st.sidebar.text_area("Sequence input", sequence_input, height=300)
sequence = st.text_area("Sequence input", sequence_input, height=300)
sequence = sequence.splitlines()
sequence = ''.join(sequence) # Concatenates list to string
st.write("here is a [random dna generator](https://faculty.ucr.edu/~mmaduro/random.htm)")


st.write("""
***
""")

## Prints the input DNA sequence
st.header('INPUT (DNA Query)')
sequence

## DNA nucleotide count
st.header('OUTPUT (DNA Nucleotide Base Count)')

### 1. Print dictionary
st.subheader('1. Print dictionary')
def DNA_base_count(seq):
  d = dict([
            ('A',seq.count('A')),
            ('T',seq.count('T')),
            ('G',seq.count('G')),
            ('C',seq.count('C'))
            ])
  return d
  
X = DNA_base_count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

### 2. Print text
st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'base'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('4. Display Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='base',
    y='count'
)
p = p.properties(
    width=alt.Step(80)  # controls width of bar.
)
st.write(p)