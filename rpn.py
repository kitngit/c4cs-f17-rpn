#!/usr/bin/env python
import operator
import readline
import colorama
ops = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv
}


def calculate(myarg):
	stack = list()
	for token in myarg.split():
		try:
			stack.append(int(token))
		except ValueError:
			arg2 = stack.pop()
			arg1 = stack.pop()
			function = ops[token]
			function(arg1, arg2)
			result = function(arg1, arg2)
			stack.append(result)
	print(colorama.Fore.YELLOW)
	print(result)
	print(colorama.Fore.WHITE)
	
	return stack.pop()

def main():
	while True:
		calculate(raw_input(colorama.Fore.GREEN + "rpn calc> "+colorama.Fore.WHITE))

if __name__ == '__main__':
	main()
