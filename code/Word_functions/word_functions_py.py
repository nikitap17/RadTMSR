import re
import pandas as pd
import spacy
nlp = spacy.load('en_core_web_sm')
from collections import Counter
import numpy as np


### Functions for data cleaning

def strip_characters(string):
    '''
    Intended use with pd.DataFrame.apply() function.
    '''
    string = re.sub(r"[^a-zA-Z '-]|\b[nN]\b| -", "", string)
    string = re.sub("-", " ", string)
    string = re.sub("\b[a-zA-Z]\b|s'|'s|'", "", string)
    string = re.sub(" {2,}", " ", string)
    return string

def POS_tagging(string, extract_pos = ["NOUN","ADJ"]):
    '''
    Intended use with pd.DataFrame.apply() function.
    '''
    doc = nlp(string)
    doc2 = " ".join([token.text for token in doc if token.pos_ in extract_pos])
    #doc2 = re.sub(" - ", " ", doc2)
    return doc2

def lemmatisation(string):
    '''
    Intended use with pd.DataFrame.apply() function.
    '''
    doc = nlp(string)
    
    lem_spacy = []
    for token in doc: 
        lem_spacy.append(token.lemma_)
    doc2 = " ".join(lem_spacy)
    #doc2 = re.sub(" - ", "-", doc2)
    return doc2



### Functions for N-gram extraction --------------------------------------------------------------------------

def ngram_extractor(doc_list):
    '''
    Building list(1) of lists(2) of strings. Each list(2) includes all possible combinations of three words, that is,
    one 3-gram, two 2-grams, and 3 1-grams.
    '''

    doc = []
    for idx in range(len(doc_list)-2):
        
        combo_list = [" ".join(doc_list[idx:idx+3])] + [" ".join(doc_list[idx:idx+2])]# + [doc_list[idx]] + [doc_list[idx+1]] + [doc_list[idx+2]]
        # + [" ".join(doc_list[idx+1:idx+3])]
        doc.append(combo_list)
        if idx == len(doc_list)-3:
            combo_list = [np.NaN] + [" ".join(doc_list[idx+1:idx+3])]# + [np.NaN] + [np.NaN] + [np.NaN]
            doc.append(combo_list)
    
    return doc


def trigram_to_nounbydoc(df):
    data = df.copy(deep=True)
    data["trigrams"] = data.ngram.apply(lambda x: Counter([element[0] for element in x]))
    
    ids = list(data.record_id)
    tri_count = [len(trigram) for trigram in data.trigrams]
    trigrams_list = sum(data.trigrams.apply(lambda x: list(x.keys())),[])
    freq_list = sum(data.trigrams.apply(lambda x: list(x.values())),[])

    new_ids = []
    for idx,count in enumerate(tri_count):
        new_ids += [ids[idx]] * count

    nounbydoc = pd.DataFrame({"doc_id" : new_ids,
                              "term" : trigrams_list,
                              "freq" : freq_list})
    nounbydoc.dropna(inplace = True)

    return nounbydoc


def bigram_to_nounbydoc(df):
    
    data = df.copy(deep=True)
    data["bigrams"] = data.residual_ngrams.apply(lambda x: Counter([item for item in x if not pd.isna(item)]))
    
    ids = list(data.record_id)
    bi_count = [len(bigram) for bigram in data.bigrams]
    bigrams_list = sum(data.bigrams.apply(lambda x: list(x.keys())),[])
    freq_list = sum(data.bigrams.apply(lambda x: list(x.values())),[])

    new_ids = []
    for idx,count in enumerate(bi_count):
        new_ids += [ids[idx]] * count

    nounbydoc = pd.DataFrame({"doc_id" : new_ids,
                              "term" : bigrams_list,
                              "freq" : freq_list})
    return nounbydoc


def relevant_trigrams(data_ngrams, meaningful_trigrams):
    trigrams = set()
    resid_ngrams = []

    # Make a deep copy of data_ngrams to avoid modifying the original input
    data_ngrams_copy = [list(element) for element in data_ngrams]

    for idx, element in enumerate(data_ngrams_copy):
        if element[0] in meaningful_trigrams:
            trigrams.add(element[0])
            
            if idx < len(data_ngrams_copy) - 1:
                data_ngrams_copy[idx+1][1] = np.NaN

        else:
            resid_ngrams.append(element[1])
    
    return list(trigrams), resid_ngrams


def select_unigrams(data_frame):
    df = data_frame
    df["resid_onegrams"] = df.abstract.apply(lambda x: x.copy())

    for idx in df.index:
        
        # Process trigrams
        for idx_b in range(len(df.loc[idx,"resid_onegrams"]) - 2):
            trigram = " ".join(df.loc[idx,"resid_onegrams"][idx_b:idx_b + 3])
            if trigram in df.loc[idx,"trigrams"]:
                df.loc[idx,"resid_onegrams"][idx_b:idx_b + 3] = ["-"] * 3

        # Process bigrams
        for idx_b in range(len(df.loc[idx,"resid_onegrams"]) - 1):
            bigram = " ".join(df.loc[idx,"resid_onegrams"][idx_b:idx_b + 2])
            if bigram in df.loc[idx,"bigrams"]:
                df.loc[idx,"resid_onegrams"][idx_b:idx_b + 2] = ["-"] * 2

        # Remove placeholders
        resid_onegrams = df.loc[idx, 'resid_onegrams']
        resid_onegrams = [token for token in resid_onegrams if token != "-"]

        # Assign back to the DataFrame
        df.at[idx, 'resid_onegrams'] = resid_onegrams
        
    df.resid_onegrams = df.resid_onegrams.apply(lambda x: list(set(x)))
                
    return

### Functions for CLassification and Replacements -------------------------------------

def classification(list_of_words, word_dict):
    '''
    Counts frequency of words falling into categories as pre-defined by a
    regex dictionary.

    Parameters
    ----------
    list_of_words : list
        The list should consist of strings, representing (key)words.
    word_dict : dict
        The dictionary classifies different regex patterns. The dict().values() should
        be a list of strings (regex patterns)

    Returns
    -------
    count_dict : dict
        A dictionary including the category names as values and their frequency counts
        as values.
    uniques_list : list
        A list of strings.
    terms_in_cat_dict : dict
        A dictionary including the category names as keys and a list of categorized
        tokens from the corpus as values.
    '''
    # Precompile all regex patterns in the dictionary
    compiled_word_dict = {term: [re.compile(pattern) for pattern in patterns] for term, patterns in word_dict.items()}
    
    count_dict = {key: 0 for key in word_dict}
    terms_in_cat_dict = {key: list() for key in word_dict}
    uniques_list = []

    for token in list_of_words:
        not_detected = True
        for term, patterns in compiled_word_dict.items():
            for pattern in patterns:
                if pattern.search(token):
                    count_dict[term] += 1
                    terms_in_cat_dict[term].append(token)
                    not_detected = False
                    break  # Break after the first match to avoid unnecessary checks

        if not_detected:
            uniques_list.append(token)

    # Convert sets in terms_in_cat_dict to lists
    terms_in_cat_dict = {key: Counter(list(value)) for key, value in terms_in_cat_dict.items()}
    
    return count_dict, uniques_list, terms_in_cat_dict



def extend_keywords(data_kw, word_dict):
    """
    Categorizes keywords according to a regex dictionary and replaces original
    (key)words with overarching categories. Importantly, one keyword can naturally
    belong to multiple categories and will be assigned to multiple categories.
    Intended use with the pd.DataFrame.apply() function.

    Parameters
    ----------
    data_kw : list
        List of strings.
    word_dict : dict
        The dictionary classifies different regex patterns. The values should
        be a list of strings (regex patterns).

    Returns
    -------
    list
        List of strings. Strings that have been matched with a dictionary class are replaced
        by the key term, respectively.
    """
    # Precompile all regex patterns in the dictionary
    compiled_word_dict = {term: [re.compile(pattern) for pattern in patterns] for term, patterns in word_dict.items()}
    
    new_kw_set = set()
    
    for token in data_kw:
        not_detected = True
        
        for term, patterns in compiled_word_dict.items():
            for pattern in patterns:
                if pattern.search(token):
                    new_kw_set.add(term)
                    not_detected = False
                    break  # Break after the first match to avoid unnecessary checks
                    
        if not_detected:
            new_kw_set.add(token)
                
    return list(new_kw_set)


def to_nounbydoc(data, column):
    '''
    Transforms a document-strring pd.DataFrame() from a "wide" to a "long" format.
    The columns "record_id" and "cat_keywords" should be defined in the data frame.

    Parameters
    ----------
    data : pd.DataFrame()
    column : str
        Name of the column that is subject to the transfomation.

    Returns
    -------
    nounbydoc : pd.DataFrame()
    '''
    ids = list(data.record_id)
    kw_count = [len(kw_list) for kw_list in data[column]]
    kw = sum(data[column], [])

    new_ids = []
    for idx,count in enumerate(kw_count):
        new_ids += [ids[idx]] * count

    nounbydoc = pd.DataFrame({"doc_id" : new_ids,
                              "term" : kw,
                              "freq" : 1})
    
    return nounbydoc

