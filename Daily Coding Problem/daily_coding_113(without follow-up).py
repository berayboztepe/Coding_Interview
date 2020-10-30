#This problem was asked by Google.
#Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
#Follow-up: given a mutable string representation, can you perform this operation in-place?

#this is without follow-up version!

st = "hello word here"
list1 = []

def get_words():
    for i in range(len(st.split())):
        list1.append(st.split()[i])

    return list1[::-1]

def string_return(strn):
    strn1 = ""

    for i in strn:
        strn1 += i
        strn1 += " "

    return strn1

print(string_return(get_words()))