

# Kristin Goselin

#######################################
# Instructions:
#
# The contact information below is not properly formatted.  Use regular expressions and Python code to reorganize the
# contact information into this format:
#
# Last name, First name, Middle Initial
# Location
# (xxx) xxx-xxxx
#
# Use regular expressions to decompose the data as much as possible and Python to reformat it.
#
# Print the reformatted information to show that it has been correctly reorganized.
#
# Extra Credit: Produce the reformatted contact info sorted programmatically by last name, ascending.
#
#######################################
import re
contacts = ["Kiayada D. Levy ,(570)7924192, Saint-Laureins-Berchem ",
            "Gretchen F. Manning ,(1-656)-285-0869, Spoleto ",
            "Ashton Richards ,(974)843-9297 , Annapolis-Royal ",
            "Demetrius J. Ferguson ,1-906-206-4323, Rea ",
            "Blair Nelson ,121-171-3665, Bertiolo ",
            "Cynthia J. Farley ,632-691-2180, Moen ",
            "Nayda M. Lloyd ,1-864-250-6977, Sarrev ",
            "Miranda E. Sexton ,1-597-689-8316, Shipshaw ",
            "Fulton Mays ,(725)789-9517, Pierrefonds ",
            "Shea Kim ,1-697-854-4139, Bihain ",
            "Emma-Mae Winters ,137-630-5601, Gulfport ",
            "Inez W. Depew ,1-833-470-5664, Johnstone ",
            "Darrel F. Key ,1-878-918-2161, Olympia ",
            "Tobias L. Stephens ,119-939-6704, Unnao ",
            "Elmo Pate ,1-869-333-7341, Griesheim "]
strContacts = ''.join(contacts)

PN = re.findall(r"\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b", strContacts)
MI = re.findall(r"\b[a-zA-Z]\w*\.", strContacts)
CL = re.split(r"\s", strContacts)
FN = (CL[0],CL[5], CL[10],CL[15],CL[20],CL[24],CL[29],CL[34],CL[39],CL[43],CL[47],CL[51],CL[56],CL[61],CL[66])
LN = (CL[2],CL[7],CL[11],CL[17],CL[21],CL[26],CL[31],CL[36],CL[40],CL[44],CL[48],CL[53],CL[58],CL[63],CL[67])
LC =(CL[4],CL[9],CL[14],CL[19],CL[23],CL[28],CL[33],CL[38],CL[42],CL[46],CL[50],CL[55],CL[60],CL[65],CL[69])
SP = "*************"
print(MI)
print(PN)
print(FN)
print(LN)
print(LC)
print('\n')



print(SP)
print('\n', LN[0], ', ', FN[0], ', ', MI[0], '\n', LC[0], '\n', PN[0],'\n')
print(SP)
print('\n', LN[1], ', ', FN[1], ', ', MI[1], '\n', LC[1], '\n', '(',PN[1])
print(SP)
print('\n', LN[2], ', ', FN[2], ', ', '\n', LC[2], '\n', PN[2])
print(SP)
print('\n', LN[3], ', ', FN[3], ', ', MI[2], '\n', LC[3], '\n', PN[3])
print(SP)
print('\n', LN[4], ', ', FN[4], ', ', '\n', LC[4], '\n', CL[22])
print(SP)
print('\n', LN[5], ', ', FN[5], ', ', MI[3], '\n', LC[5], '\n', PN[4])
print(SP)
print('\n', LN[6], ', ', FN[6], ', ', MI[4], '\n', LC[6], '\n', PN[5])
print(SP)
print('\n', LN[7], ', ', FN[7], ', ', MI[5], '\n', LC[7], '\n', PN[6])
print(SP)
print('\n', LN[8], ', ', FN[8], ', ', '\n', LC[8], '\n', PN[7])
print(SP)
print('\n', LN[9], ', ', FN[9], ', ', '\n', LC[9], '\n', PN[8])
print(SP)
print('\n', LN[10], ', ', FN[10], ', ', '\n', LC[10], '\n', CL[49])
print(SP)
print('\n', LN[11], ', ', FN[11], ', ', MI[6], '\n', LC[11], '\n', PN[9])
print(SP)
print('\n', LN[12], ', ', FN[12], ', ', MI[7], '\n', LC[12], '\n', PN[10])
print(SP)
print('\n', LN[13], ', ', FN[13], ', ', MI[8], '\n', LC[13], '\n', CL[64])
print(SP)
print('\n', LN[14], ', ', FN[14], ', ', '\n', LC[14], '\n', PN[11])
print(SP)









