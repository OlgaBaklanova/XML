import xml.etree.ElementTree as ET

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

news_list = root.findall("channel/item")

word_value = {}
full_set = set()
descript = ''
for news in news_list:
	descript += news.find("description").text

for news in news_list:
    full_set.add(descript)

full_set = ', '.join(full_set)
full_set = full_set.split(" ")

for elements in full_set:
    if len(elements) > 6:
        if elements in word_value:
            word_value[elements] += 1
        else:
            word_value[elements] = 1

sorted_words = sorted(word_value.items(), key=lambda x: x[1], reverse=True)

print(f'Топ-10 самых часто встречающихся в новостях слов: {sorted_words[:10]}')
