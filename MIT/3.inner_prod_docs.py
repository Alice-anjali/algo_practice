import string

file1 = open("doc1.txt", "r")
doc1 = file1.read()
print(doc1)
file2 = open("doc2.txt", "r")
doc2 = file2.read()
print(doc2)

def remove_punctuations(doc):
    table = str.maketrans({key: None for key in string.punctuation})
    return doc.translate(table).lower().rstrip("\n").replace('\n', ' ')

def convert_to_list(doc):
    return list(doc.split(" "))

def word_frequency(doc):
    dic = {}
    for x in doc:
        if not x in dic:
            dic[x] = doc.count(x)
    return dic

def inner_product(dict1,dict2):
    innProd = 0
    for x in dict1:
        if x in dict2:
            innProd += dict1[x]*dict2[x]
    return innProd

cleaned_doc1 = remove_punctuations(doc1)
cleaned_doc2 = remove_punctuations(doc2)

docToList1 = convert_to_list(cleaned_doc1)
docToList2 = convert_to_list(cleaned_doc2)

listToDict1 = word_frequency(docToList1)
listToDict2 = word_frequency(docToList2)

innProd = inner_product(listToDict1,listToDict2)

print(listToDict1)
print(listToDict2)
print("Inner Product of 2 docs= "+str(innProd))
