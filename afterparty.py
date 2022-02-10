#Afterparty
# l = [1,2,3,4,4,5,6,7,8,9,0,1,3]
# for i in range(1,len(l)):
#     if l[i] == l[i-1]:
#         l[i] = ''
# while '' in l:
#     l.remove('')
# print(l)
# l = [1,2,3,4,4,5,6,7,8,9,0,1,3]
# a = 1
# length = len(l)
# while a < length:
#     if l[a] == l[a-1]:
#         l.pop(a)
#     a = a + 1
#     length = len(l)
# print(l)

# #Вариант работает при точном совпадении регистра
#
# text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.
#
# A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]
#
# Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
# word_list = ['Star','Wars','Force','slavery']
# for word in word_list:
# 	if word in text:
# 		text = text.replace(word,word.upper())
# print(text)
#
# #Не чувствителен к регистру, но обратите внимание, что воздействует только на "чистые слова", самое последнее слова, является один целым с точкой, потому его не меняет
# text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.
#
# A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]
#
# Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
# word_list = ['Star','Wars','Force','slavery']
# text_list = text.split(' ')
# for i in range(len(word_list)):
# 		for j in range(len(text_list)):
# 				if word_list[i].lower() == text_list[j].lower():
# 						text_list[j] = text_list[j].upper()
# upper_text = ''
# for text_word in text_list:
# 		upper_text = upper_text + ' ' + text_word
# print(upper_text)
# 2.0#Не чувствителен к регистру, но обратите внимание, что воздействует только на "чистые слова", самое последнее слова, является один целым с точкой, потому его не меняет
text = '''The Star Wars franchise depicts the adventures of characters "A long time ago in a galaxy far, far away",[5] in which humans and many species of aliens (often humanoid) co-exist with robots (typically referred to in the films as 'droids'), who may assist them in their daily routines; space travel between planets is common due to lightspeed hyperspace technology.[6][7][8] Spacecraft range from small starfighters, to huge capital ships such as the Star Destroyers, to space stations such as the moon-sized Death Stars. Telecommunication includes two-way audio and audiovisual screens, and holographic projections.

A mystical power known as the Force is described in the original film as "an energy field created by all living things ... [that] binds the galaxy together".[9] Through training and meditation, those whom "the Force is strong with" are able to perform various superpowers (such as telekinesis, precognition, telepathy, and manipulation of physical energy).[10] The Force is wielded by two major knightly orders at conflict with each other: the Jedi, peacekeepers of the Galactic Republic who act on the light side of the Force through non-attachment and arbitration, and the Sith, who use the dark side by manipulating fear and aggression. While Jedi Knights can be numerous, the Dark Lords of the Sith (or 'Darths') are intended to be limited to two: a master and their apprentice.[11]

Force-wielders are very limited in numbers in comparison to the population. The Jedi and Sith prefer the use of a weapon called a lightsaber, a blade of energy that can cut through virtually any surface and deflect energy bolts. The rest of the population, as well as renegades and soldiers, use laser-powered blaster firearms. In the outer reaches of the galaxy, crime syndicates such as the Hutt cartel are dominant. Bounty hunters are often employed by both gangsters and governments. Illicit activities include smuggling and slavery.'''
word_list = ['Star','Wars','Force','slavery']
text_list = text.split(' ')
for i in range(len(word_list)):
		for j in range(len(text_list)):
				if word_list[i].lower() in text_list[j].lower():
						text_list[j] = text_list[j].upper()
upper_text = ''
for text_word in text_list:
		upper_text = upper_text + ' ' + text_word
print(upper_text)

# 'slavery' == 'slavery.' 1.0 FALSE
# 'slavery' in 'slavery.' 2.0 TRUE
# 'slavery' in 'slavery' 2.0 TRUE
s1 = [4,1,2,3,4]
s2 = [3,10,2,5,7]
mini = s1[0]
maxi = s1[0]
s_minmax = []
for n in range(len(s1)):
    if mini > s1[n]:
        mini = s1[n]
        s_minmax.append(mini)
    if maxi < s1[n]:
        maxi = s1[n]
        s_minmax.append(maxi)
print(mini, maxi)
mini = s2[0]
maxi = s2[0]
for n in range(len(s2)):
    if mini > s2[n]:
        mini = s2[n]
        s_minmax.append(mini)
    if maxi < s2[n]:
        maxi = s2[n]
        s_minmax.append(maxi)
print(s_minmax)

'''# ■ Сформировать третий список, содержащий только уникальные элементы каждого из списков;
# ■ Сформировать третий список, содержащий только минимальное и максимальное значение каждого из списков.'''
s1 = [1,2,3,4]
s2 = [1,2,5,6,8]
s3 = s1[:]
for s in s2:
    if s not in s3:
        s3.append(s)

s1 = [1,2,3,4]
s2 = [1,2,5,6,8]
s3 = s1[:]
for s in s2:
    if s in s3:
        continue
    else:
        s3.append(s)


s1 = [1,2,3,4]
s2 = [1,2,5,6,8]
s_rr = s1[:]
for i in s2:
    if i not in s_rr:
        s_rr.append(i)
print(s_rr)