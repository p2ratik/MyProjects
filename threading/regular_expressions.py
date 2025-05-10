import re
pattern=r"[a-z]+lly" #Searches for (a to z every charater + lly)
pattern2=r"\_+ros"
text='''
Technology is the application of conceptual knowledge to achieve practical goals, especially in a reproducible way.[1] The word technology can also mean the products resulting from such efforts,[2][3] including both tangible tools such as utensils or machines, and intangible ones such as software. Technology plays a critical role in science, engineering, and everyday life asplly zsplly asop_ros

Technological advancements have led to significant changes in society. The earliest known technology is the stone tool, used during prehistory, followed by the control of fire—which in turn contributed to the growth of the human brain and the development of language during the Ice Age, according to the cooking hypothesis. The invention of the wheel in the Bronze Age allowed greater travel and the creation of more complex machines. More recent technological inventions, including the printing press, telephone, and the Internet, have lowered barriers to communication and ushered in the knowledge economy.
'''
match_1=re.search(pattern2,text) #Returns only the first pattern found
match=re.findall(pattern,text) #Returns the list of all patterns occcuring in the text
match3=re.findall(pattern2,text)
print(match3)

for z in match:
    i=text.index(z)
    print(i)
    
