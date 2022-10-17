#!/bin/python

# Currency Converter

# version 0.1 

import requests

URL = 'https://api.exchangerate-api.com/v4/latest/THB?'
BASE_CURRENCY = 'THB'

def retrieve_data(url):
	response_API = requests.get(url)
	data = response_API.json()
	rates = data["rates"]
	return rates

def get_currencies_lst(rates):
	""" get countries list from the keys
	"""
	currencies_list = list(rates.keys())
	return currencies_list

def get_currency_rate(currency, rates):
	""" get specific country rate
	"""
	currency_rate = rates[currency]
	return currency_rate

# Convertion Part

def converter(from_currency:str, to_currency:str, amount:float):
	""" convert amount of money from from_currency to to_currency using 
	conversion_factor retrieving real time using the API.
	Usuage:

	>>> converter('THB', 'CAD', 0.0362, 100)
	3.62
	"""
	rate = get_currency_rate(from_currency, retrieve_data(URL))
	initial_amount = amount

	if from_currency != BASE_CURRENCY:
		# convert other currency to thb which is our base
		# default output is to_currency == 'THB'
		amount_in_base_currency = initial_amount / rate
		# limiting the precision to 4 decimal places
		amount_in_base_currency = round(amount_in_base_currency, 4)
		return amount_in_base_currency

	# Check TO DO
	#else: #from_currency == 'THB' and to_currency != 'THB' :
	#	amount_to_thb = initial_amount / rate
	#	thb_2_others =  amount_to_thb * rate
		# limiting the precision to 4 decimal places
	#	thb_2_others = round(thb_2_others, 4)
	#	return thb_2_others

# CLI UI Ver 2
fromCurrency = input("Enter from_currency: ")
toCurrency = input("Enter to_currency: ")
initialAmount = float(input("Enter amount: "))

description = f'From Currency: {fromCurrency} \n To Currency: {toCurrency} \n Initial Amount: {initialAmount} \n Converting Result:'
print(description, converter(fromCurrency, toCurrency, initialAmount))



"""
Later

from tkinter import *
from tkinter import ttk

# GUI
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Convert to and from THB").grid(column=0, row=0)
ttk.Button(frm, text="Convert", command=root.keys()).grid(column=1, row=1)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)
root.mainloop() 
"""