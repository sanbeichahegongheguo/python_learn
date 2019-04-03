import re
import jieba

add1 = '四川省成都市都江堰市天马镇34号'
add2 = '北京市北京市东城区前门大街1号'
add3 = '新疆维吾尔自治区乌鲁木齐市天山区中山路479号'
add4 = '四川省成都市双流县幸福社区23号'
add5 = '香港特别行政区中西区尖沙嘴路'

# pattern = re.compile(r'\d+')   # 查找数字
pattern = re.compile(r'(省)')

result1 = pattern.findall(add1)
result2 = pattern.findall(add2)

print(result1)
print(result2)
