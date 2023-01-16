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
    for doc in doc_list:
        print(doc)
        low = doc.lower() 
        print(low)
        split = low.split(' ')
        print(split)
        for word in split:
            strip = word.strip('.').strip(',')
            print(strip)
            if strip == keyword:
                list_of_indexes.append(doc_list.index(doc)) 
                print(list_of_indexes)
                break
    return(list_of_indexes)            


doc_list = ["The Learn Casinoo Python casino Challenge Casino.", "They bought a car, bike and boat in casino", "Casinoville"]
word_search = word_search(doc_list, 'casino')
print(word_search)

str = " The Learn Python Challenge Casino. "

spl = str.split('t')
low = str.lower()
strip = str.strip(' ').strip('.').strip('T').strip('o')
ind = str.index('t')
#print(ind)
#print(low)
