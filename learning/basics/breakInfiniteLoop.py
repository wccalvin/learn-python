# break statement breaks out of the while loop clause early

number = 0
while True:
	number += 1
	if number == 100:
		print "Counted to %s!"%number
		break