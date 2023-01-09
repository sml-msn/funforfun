import streamlit as st
import torch
from transformers import T5ForConditionalGeneration, T5Tokenizer
import demo

model_name = "sml-msn/pst5-tg-fa-bidirectional"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def translit(x, **kwargs):
    inputs = tokenizer(x, return_tensors='pt').to(model.device)     
    with torch.no_grad():    
        hypotheses = model.generate(**inputs, **kwargs)        
    return tokenizer.decode(hypotheses[0], skip_special_tokens=True)

def check_length(txt):
	if len(txt) > 500:
		st.write('Output: ')
		st.write('Sorry, your text is too long.')
		return False
	elif txt == '':
		st.write('Output: ')
		st.write('You must enter something.')
		return False
	else:
		return True
		
def split_n_translit(txt):
	lst = txt.split('.')
	blanks = lst.count('')
	if blanks > 0:
		for i in range(blanks):
			lst.remove('')
	text = []
	if lst == []:
		st.write('There is something wrong with your text.')
		return False
	else:
		for sentence in lst:
			text.append(translit(sentence, max_length = 1024)+'.')
		st.write(' '.join(text))
		return True

st.title('Tg-Fa transliterator')

txt = st.text_area('Enter your text:', placeholder = 'Your text must have less than 500 symbols.')

if st.button('Transliterate'):
	if check_length(txt) == True:
		st.write('Output: ')
		if txt.count('.') > 0:
			split_n_translit(txt)
		else:
			st.write(translit(txt, max_length = 1024))	

if st.button('Run demo'):
	st.write('Output: ')
	demo.start()	

#st.write(str(lst))
