# from pathlib import Path
# import bisect

# size = [1, 2**10, 2**20, 2**30]
# unit = ['B', 'Kb', 'Mb', 'Gb']
# fpath = input('Enter file name: ')
# fsize = Path(fpath).stat().st_size

# def convert(byts):
# 	if byts != 0:
# 		index = bisect.bisect(size, byts) -1
# 		return f'{byts/size[index]:.1f}{unit[index]}'
# 	else:
# 		return '0B'
# print(f'{convert(fsize)} {fpath}')

# sentence = "One of Triumph's best-loved motorcycles, the Tiger 800 family takes this celebrated range to a whole new level by incorporating around 200 upgrades per model over the previous generation.This is now a Tiger 800 range that has the highest ever level of technology, more capability, enhanced ergonomics, and a lower ratio 1st gear and more responsive power delivery."
# for word in sentence.split(' ')[::-1]:
# 	print(word)

# import sys

# def Hello(name):
# 	name = 'Your name is ' + name + ' !!!!!!!!!'
# 	print("Hello", name)

# def main():
# 	Hello(sys.argv[-1])

# if __name__ == '__main__':
# 	main()





