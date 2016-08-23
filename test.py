def sign(num):
	if num > 0: 
		return 1
	elif  num ==0:
		return 0
	else:
		return -1

print sign(999999999)
print sign(-9)

def greet():
	return 'hi'

temp = greet()
print temp
def test(num):
	if num == 8:
		return 8
	else:
		return 'fail'

print test(5)
