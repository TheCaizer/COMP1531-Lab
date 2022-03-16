import sys

def roman(input):
	rom_num = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
	value = 0
	for i in range(len(input)):
		if i > 0 and rom_num[input[i]] > rom_num[input[i - 1]]:
			value += rom_num[input[i]] - 2*rom_num[input[i - 1]]
		else:
			value += rom_num[input[i]]
	return value

def test_roman_normal():
	assert roman('I') == 1
	assert roman('II') == 2
	assert roman('IX') == 9
	assert roman('XIX') == 19
	assert roman('XX') == 20
	assert roman('IV') == 4
	assert roman('XIV') == 14
	assert roman('MDCCLXXVI') == 1776
	assert roman('MMXIX') == 2019

def test_roman_empty():

	assert roman('') == 0