# -*- coding: utf-8 -*-
# 描述: 创建gif图片
# 作者: youlanhai
# 主页: https://github.com/youlanhai/makegif
# 参考: https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#saving
#
from os import path, listdir
from argparse import ArgumentParser

def main():
	parser = ArgumentParser(description = "创建gif图片")
	parser.add_argument("-d", "--duration", type = float, default = 200, help = "时间间隔。默认200ms")
	parser.add_argument("-o", "--output", help = "输出路径")
	parser.add_argument("-f", "--filters", default = "png,jpg,bmp", help = "用于在文件夹中搜索指定的后缀文件。默认: png,jpg,bmp")
	parser.add_argument("-s", "--size", help = "输出图片大小。格式: 640x480; 或者640x，仅限定宽度为640，高度等比缩放; 或者x480，仅限定高度为480，宽度等比缩放")
	parser.add_argument("inputs", nargs = "+", help = "输入文件路径，或文件夹。支持混合输入")

	option = parser.parse_args()

	try:
		from PIL import Image
	except:
		raise RuntimeError("先安装Pillow插件: pip install Pillow")

	if not option.inputs:
		raise RuntimeError("没有输入文件")

	filters = option.filters.split(",")

	# 搜索文件
	input_paths = []
	for input_path in option.inputs:
		if path.isdir(input_path):
			files = listdir(input_path)
			files.sort()
			for fname in files:
				ext = path.splitext(fname)[1]
				if ext and ext[1:] in filters:
					input_paths.append(path.join(input_path, fname))

		elif path.isfile(input_path):
			input_paths.append(input_path)

		else:
			print("文件不存在:", input_path)

	if len(input_paths) == 0:
		raise RuntimeError("没有匹配到图片文件")

	# 加载图片
	images = []
	for file_path in input_paths:
		image = Image.open(file_path)
		images.append(image)

	# 执行缩放
	size = parse_size(option.size, images[0].size)
	for i, image in enumerate(images):
		if image.size != size:
			image = image.resize(size, Image.ANTIALIAS)
		images[i] = image

	# 输出
	output_path = option.output
	if not output_path:
		output_path = path.dirname(input_paths[0]) + ".gif"

	print("save gif to:", output_path)
	images[0].save(output_path, save_all = True, duration = option.duration, append_images = images[1:])

def parse_size(size_str, size):
	if not size_str:
		return size

	strs = size_str.split("x")
	# 限定宽度，保留宽高比
	if len(strs) == 1 or strs[1] == "":
		width = int(strs[0])
		height = width * size[1] // size[0]
		return width, height

	# 限定高度
	if strs[0] == "":
		height = int(strs[1])
		width = height * size[0] // size[1]
		return width, height

	# 限定宽和高
	return int(strs[0]), int(strs[1])


if __name__ == "__main__":
	main()
