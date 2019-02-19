from fann2 import libfann

eng_ref = "etaoinsrhldcumfpgwybvkxjqz"
fr_ref = "esaitnrulodcmpévqfbghjàxèy"

alpha = "abcdefghijklmnopqrstuvwxyzéàè"

f = open('eng.txt', 'r')
content = f.read()
fr_count = 0
eng_count = 0


letter_occ = {}


for i in alpha:
	letter_occ[str(i)] = content.count(str(i))

sorted_by_value = sorted(letter_occ.items(), key=lambda kv: kv[1], reverse = True)

tmp = ""
for key, value in sorted_by_value:
	tmp = tmp + str(key[0])


for i in range(len(eng_ref)):
	if(eng_ref[i] == tmp[i]):
		eng_count += 1
	if(fr_ref[i] == tmp[i]):
		fr_count += 1


if(fr_count > eng_count):
	print("Français")
elif(fr_count == eng_count):
	print("dunno")
	print(fr_count)
	print(eng_count)
else:
	print("Anglais")
