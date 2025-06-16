def toRome(number):
    num = [1, 4, 5, 9, 10, 40, 50, 90,
        100, 400, 500, 900, 1000]
    sym = ["I", "IV", "V", "IX", "X", "XL",
        "L", "XC", "C", "CD", "D", "CM", "M"]
    i = 12
    res = ""
    
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            # print(sym[i], end = "")
            res += sym[i]
            div -= 1
        i -= 1
    return res


val = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

# Returns decimal value of roman numeral
def romanToDecimal(s):
	res = 0
	i = 0
	while i < len(s):
        
		# Get value of current symbol
		s1 = val[s[i]]

		# Compare with the next symbol if it exists
		if i + 1 < len(s):
			s2 = val[s[i + 1]]

			# If current value is greater or equal, 
			# add it to result
			if s1 >= s2:
				res += s1
			else:
				# Else, add the difference and 
				# skip next symbol
				res += (s2 - s1)
				i += 1
		else:
			res += s1
		i += 1

	return res

f = open("in.txt")

ans = 0
for line in f:
    line = line.strip()
    num = romanToDecimal(line)
    ans += (len(line) - len(toRome(num))) 

        
print(ans)

