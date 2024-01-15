x = 2
y = x + 5
print(y)

print(type(3.14)) #float
print(type(3.14) == float) #true

print(isinstance(3.14,float))
print(isinstance("inha",float)) #false p.69

artists = ['bts', 'newjeans','ses','hot','blackpink']
group = artists
print(artists, group)
artists[2] = 'seventeen'
print(artists, group) #same address