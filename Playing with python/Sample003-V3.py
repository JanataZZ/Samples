def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car in casino", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    list_of_indexes = []
    for i, doc in enumerate(doc_list):
       print(i, doc)
       tokens = doc.split()
       print(i, tokens)
       normalised = [token.lower().strip('.,') for token in tokens]
       print(i, normalised)
       if keyword.lower() in normalised:
            list_of_indexes.append(i)
    return list_of_indexes

doc_list = ["The Learn, Casinoo Python, casino, Challenge Casino.", "They bought a car, bike and boat in casino", "Casino ville"]
word_search = word_search(doc_list, 'casino')
print(word_search)

str = " The Learn. Python, Challenge Casinova. "

spl = str.split()
low = str.lower()
strip = str.strip(' ').strip('.').strip('T').strip('o')
ind = str.index('t')
normalised = [s.lower().rstrip('.,') for s in spl]
if 'casino' in normalised:
    print(1)
else:
    print(2)    
#print(enumerate(doc_list))
print(normalised)
