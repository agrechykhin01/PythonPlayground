text = "X-DSPAM-Confidence:    0.8475"
pos = text.find('0.8475')
str_number = text[pos:]
number = float(str_number)
print(number)
