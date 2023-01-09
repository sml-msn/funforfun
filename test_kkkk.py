import kkkk as m
import pytest
import pandas as pd
from Levenshtein import distance, ratio

def test_translit_acc_tg_fa():
	sample = pd.read_csv('test180k.csv', sep=',').sample(1)
	for k, row in sample.iterrows():
		target = row.Pers
		prediction = m.translit(row.Taj, max_length = 1024)
		print('input:', row.Taj)
		print('target:', target)
		print('prediction:', prediction)
		print('lev. ratio:', ratio(target, prediction))
	assert ratio(target, prediction) > 0.8
    
def test_translit_acc_fa_tg():
	sample = pd.read_csv('test180k.csv', sep=',').sample(1)
	for k, row in sample.iterrows():
		target = row.Taj
		prediction = m.translit(row.Pers, max_length = 1024)
		print('input:', row.Pers)
		print('target:', target)
		print('prediction:', prediction)
		print('lev. ratio:', ratio(target, prediction))
	assert ratio(target, prediction) > 0.8

def test_check_length_too_long():
	txt = '''
		Бунёдгузори адабиёти форсу тоҷик Абӯабдуллоҳ Рӯдакӣ соли 858 дар деҳаи Панҷрӯд аз тавобеъи Самарқанд (бинобар ин дар баъзе сарчашмаҳо Рӯдакии Самарқандӣ низ меноманд), 
		ки акнун рустое аз ноҳияи Панҷакент дар вилояти Суғд аст, ба дунё омадааст. 
		Таърихи ҳазору сад солаи адабиёти тоҷик бо номи бунёдгузори он устод Рӯдакӣ сахт вобаста аст. 
		Рӯдакиро муосиронаш ва суханварони баъдина бо унвонҳои ифтихорӣ: 
		Одамушуаро форсӣ: آدم الشعرا‎ Қофиласорои назми форсӣ, Соҳибқирони шоирон, Султони шоирон, Мақаддумушуаро ва ҳамсони инҳо ёд мекунанд. 
		Асосгузор ва сардафтари адабиёт аслан маънои онро надорад ки пеш аз дигарон асар эҷод карда бошад.
		'''
	assert m.check_length(txt) == False
	
def test_check_length_blank():
	txt = ''
	assert m.check_length(txt) == False

def test_check_length_ok():
	txt = '''
		Бунёдгузори адабиёти форсу тоҷик Абӯабдуллоҳ Рӯдакӣ соли 858 дар деҳаи Панҷрӯд аз тавобеъи Самарқанд (бинобар ин дар баъзе сарчашмаҳо Рӯдакии Самарқандӣ низ меноманд), 
		ки акнун рустое аз ноҳияи Панҷакент дар вилояти Суғд аст, ба дунё омадааст. 
		'''
	assert m.check_length(txt) == True
		
def test_split_n_translit_dots_only():
	txt = '......'
	assert m.split_n_translit(txt) == False

def test_split_n_translit_ok():
	txt = '''
		Таърихи ҳазору сад солаи адабиёти тоҷик бо номи бунёдгузори он устод Рӯдакӣ сахт вобаста аст. 
		Рӯдакиро муосиронаш ва суханварони баъдина бо унвонҳои ифтихорӣ: 
		Одамушуаро форсӣ: آدم الشعرا‎ Қофиласорои назми форсӣ, Соҳибқирони шоирон, Султони шоирон, Мақаддумушуаро ва ҳамсони инҳо ёд мекунанд. 
		Асосгузор ва сардафтари адабиёт аслан маънои онро надорад ки пеш аз дигарон асар эҷод карда бошад.
		'''
	assert m.split_n_translit(txt) == True
