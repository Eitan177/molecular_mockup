from select import select
import streamlit as st
from streamlit_tags import st_tags, st_tags_sidebar
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
st.set_page_config(layout="wide")
st.title('Molecular Results and Their Histology Correlates')



keyword0 = st_tags_sidebar(label='# Immunoqueryesque setup: Enter something molecular:',
                          text='Press enter to add more',
                          value=[ 't(8;14)','t(14;18)'],
                          suggestions=['t(8;14)','t(14;18)','t(11;14)','t(2;8)'],
                          
                          maxtags=3,
                          key="afrfae")

st.sidebar.write("### Results:")
st.sidebar.write((keyword0))


keyword1 = st_tags_sidebar(label='# Get a near match to an individual case:',
                          text='Press enter to add more',
                          value=[ 'ROS1','MYC','EGFR','RET','NOTCH1','TP53','KRAS'],
                          suggestions=['MYCL','MSH6','JAK3','APC','GNAS','MET','ERK','ARID1A'],
                          
                          maxtags=20,
                          key="xfase")

st.sidebar.write("### profile")
st.sidebar.write((keyword1))

transl=np.array(('t(8;14)','t(14;18)','t(11;14)','t(2;8)'))
lymphs =np.array(('Burkitts','Follicular','Mantle Cell','Burkitts'))
descr = np.array(('starry sky','giant follicle','giant mantle zone','starry sky'))
descr2 = np.array(('CD10','CD10,CD6','Cyclin D1','CD10'))
descr3 = np.array(('cleared out Macrophages','medium Lymphocytes','small lymhocutes','Cleared out macrophages'))
inputs=pd.DataFrame({'translocations': keyword0})
ii=pd.DataFrame({'lymphoma':lymphs, 'translocations':transl,'Description':descr,'more Description':descr2,'Yet more':descr3 })
show=pd.merge(inputs,ii)
st.write('## Input and histology correlates')
st.write(show)

if 't(8;14)' in keyword0 or 't(2;8)':

    with st.expander('Burkitts Lymphoma: Click on this bar to see'):

        components.iframe('https://digital.pathology.johnshopkins.edu/imageSets/451?folder=12752',height=1000)

if 't(11;14)' in keyword0:

    with st.expander('Mantle Cell Lymphoma: Click on this bar to see'):

        components.iframe('https://digital.pathology.johnshopkins.edu/imageSets/5236?slide=191711',height=1000)

if 't(14;18)' in keyword0:
    with st.expander('Follicular Lymphoma: Click on this bar to see'):

        components.iframe('https://digital.pathology.johnshopkins.edu/imageSets/1451?slide=44388',height=1000)


with st.expander('Histology from cases that somewhat match an entire report or subset of a report: Click on this bar to see'):
    st.write( 'Most similar')
    components.iframe('https://digital.pathology.johnshopkins.edu/imageSets/451?slide=78418',height=1000)
    cola, colb, colc, cold, cole =st.columns(5)
    cola.write('EGFR mutated')
    colb.write('KRAS mutated')
    colc.write('ERK mutated')
    cold.write('ROS1 mutated')
    cole.write('APC mutated')
    st.write( '2nd Most similar')
    components.iframe('https://digital.pathology.johnshopkins.edu/imageSets/451?slide=83063',height=1000)
    cola, colb, colc =st.columns(3)
    colb.write('KRAS mutated')
    colc.write('ERK mutated')
    cole.write('APC mutated')

with st.expander('Test yourself: Click on this bar to see'):
    st.write('1) Stem...')
    st.selectbox('1) Answer', ('A) something','B) wrong answer','C) not a bad choice'))
    st.write('2) Stem...')
    st.selectbox('2) Answer', ('A) something','B) wrong answer','C) not a bad choice'))
    st.write('3) Stem...')
    st.selectbox('3) Answer', ('A) something','B) wrong answer','C) not a bad choice'))
    st.write('4) Stem...')
    st.selectbox('4) Answer', ('A) something','B) wrong answer','C) not a bad choice'))
    st.write('5) Stem...')
    st.selectbox('5) Answer', ('A) something','B) wrong answer','C) not a bad choice'))
