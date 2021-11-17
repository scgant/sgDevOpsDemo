data = 50
try: 
	data = data/0
except (ZeroDivisionError): 
	print('Cannot divide by 0 ', end = '') 
else: 
	print('Division successful ', end = '') 
