def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    
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
                print("success")


doc_list = ["The Learn Python Challenge Casino.", "They bought a car, bike and boat", "Casinoville"]
word_search(doc_list, 'casino')


str = " The Learn Python Challenge Casino. "

spl = str.split('t')
low = str.lower()
strip = str.strip(' ').strip('.').strip('T').strip('o')
#print(str)
#print(low)
