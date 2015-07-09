# continue statement jumps back to the start of the loop and re-evaluates
# the condition.

num = 0
while True:
	print "Now counting: %s"%num
	if num == 1000:
		print "Reached the limit: %s"%num
		break
	if num >=100:
		num += 100
		continue
	else:
		num += 10

