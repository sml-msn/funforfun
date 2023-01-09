import kkkk as m
import pandas as pd
from Levenshtein import distance, ratio
import streamlit as st

def start():
	sample = pd.read_csv('test180k.csv', sep=',').sample(1)
	
	# tg-fa
	for k, row in sample.iterrows():
		target = row.Pers
		prediction = m.translit(row.Taj, max_length = 1024)
		st.write('input:', row.Taj)
		st.write('target:', target)
		st.write('prediction:', prediction)
		st.write('lev. distance:', distance(target, prediction))
		st.write('lev. ratio:', ratio(target, prediction))
	
	st.write()
	st.write('--------------------------------------------')
	st.write()	
	
	# fa-tg
	for k, row in sample.iterrows():
		target = row.Taj
		prediction = m.translit(row.Pers, max_length = 1024)
		st.write('input:', row.Pers)
		st.write('target:', target)
		st.write('prediction:', prediction)
		st.write('lev. distance:', distance(target, prediction))
		st.write('lev. ratio:', ratio(target, prediction))

