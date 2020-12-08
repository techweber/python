# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.findall("ai",txt)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.search("\s", txt)
# print("The first white space character is positioned at " , x.start())

# import re
# txt = "The rain in Spain"
# x = re.split("\s", txt, 2)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.sub("\s","9",txt, 2)
# print(x)

# import re
# txt = "The rain in Spain"
# x = re.search("ai", txt)
# print(x)

import re
txt = "The rain in Switzerland Spain"
x = re.search(r"\bS\w+", txt)
# print(x.span())
# print(x.string)
print(x.group())

