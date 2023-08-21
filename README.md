# B+-Programming-Language

B+ is a Programming language made for starters to get into programming very easily by terminating different prefixes etc. No need to put = or +, -, *, /. The Transpiler will
translate it automatically.

Given variables:
	MATH.PI = Pi
	MATH.random = a random number from 0 to 255 which generates each time the programm starts and cant be changed while program is running.
	MATH.dice = a random number from 1 to 6

out:
	The out command replaces the print command as its mostly known of. It outputs text to the Terminal. An example command would be: out Hello World! <<.
	the <<, >> prefixes determines wether it is a variable or string. if you put a >> at the end it will search for a variable named Hello and output its value.

var, str:
	Programming would be empty without any variables. The use is: var a 1 or str a 1. As the name suggests var stands for variable and str for string. The reason
	why i didn't put int instead of var is because it can var can also take float.

take:
	Take gets an input of a user in the shell and puts it in a variable which you give it. Example: take number What is your preffered number?

rand:
	Use: rand generated_number 0 255, generates a number between 0 and 255 with the given variable of generated_number.

if and ifn:
	The if statement is a common statement amognst all programming languages and is one of the most important one. With it you can make multiple possibilities how a programm would work for example if a is 1 then... The ifn statement is the negative of the if statement and checks if the statement is NOT true. with this you can make multiple possible ways a program will work.

add, sub, mul, div:
	add = addition, sub = subtraction, mul = multiplication, div = division, with these basic statements you can make simple mathematical calculations of numbers and variables.

func:
	With "func" you can create functions which are lines of codes which can be recalled at any time.