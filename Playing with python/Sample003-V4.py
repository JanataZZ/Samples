def multi_word_search(doc_list, keywords):
    dict_of_ind = {}
    def word_search(doc_list, keyword):
        """
        Takes list of documents (each document is a string) and a list of keywords.  
        Returns a dictionary where each key is a keyword, and the value is a list of indices
        (from doc_list) of the documents containing that keyword

        >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
        >>> keywords = ['casino', 'they']
        >>> multi_word_search(doc_list, keywords)
        {'casino': [0, 1], 'they': [1]}
        """
        list_of_indexes = []
    
        for i, doc in enumerate(doc_list):
           tokens = doc.split()
           normalised = [token.lower().strip('.,') for token in tokens]
           if keyword.lower() in normalised:
               list_of_indexes.append(i)
        return list_of_indexes
    for keyword in keywords:
        dict_of_ind[keyword] = word_search(doc_list, keyword)
    return dict_of_ind


doc_list = ["They Learn, Casinoo Python, casino, Challenge Casino.", "They bought a car, bike and boat in casino", "Casino ville", "Casinoville"]
keywords = ['casino', 'they']
multi_word_search = multi_word_search(doc_list, keywords)
print(multi_word_search)


