my_str = 'this is a test'
string_elements = my_str.split()
print('This is string element: ',string_elements)

reversed_elements = []
for element in string_elements:
	reversed_elements.append(element[::-1])
	
print('This is reversed element: ',reversed_elements)
new_str = ''.join(reversed_elements)
print('This is new reverse join element: ',new_str)
	
