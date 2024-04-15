import openslide as opslide

#读取病理图
slide = opslide.open_slide('G:\\E----Cancaer\\1444\\MMRd\\CD3\\2013-3442-3\\1.tif')

# 获取图像基本信息
print(slide.dimensions)     # 图像宽度和高度
print(slide.level_count)    # 图像金字塔级别数
print(slide.level_dimensions)   # 每个金字塔级别的宽度和高度
print(slide.level_downsamples)  # 每个金字塔级别的下采样因子

# 获取图像缩略图
thumbnail = slide.get_thumbnail((256, 256))
thumbnail.save('thumbnail.png')