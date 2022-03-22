import getpass as gp

try:
 	p = gp.getpass('Password dao:')
except Exception as error:
	print('ERROR', error)

else:
	print('Password entered:', p)

