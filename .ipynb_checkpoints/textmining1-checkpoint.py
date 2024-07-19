#!/usr/bin/env python
# coding: utf-8

# In[5]: libraries

import numpy as np
import pandas as pd
from scipy import stats
import re
import itertools
import nltk
#nltk.download('all')


# In[11]:

df1 = pd.read_excel(r"savedrecs.xls")
df2 = pd.read_excel(r"savedrecs2.xls")
df3 = pd.read_excel(r"savedrecs3.xls")
df4 = pd.read_excel(r"savedrecs4.xls")
df5 = pd.read_excel(r"savedrecs5.xls")

df = pd.concat([df1, df2, df3,df4,df5])
del(df1,df2,df3,df4,df5)

colnames = list(df)
df = df.drop_duplicates(["Article Title", "DOI"])
df2 = pd.concat([df["Author Keywords"], df["Article Title"]], axis = 1) #select only relevant rows for keyword analysis
df2 = df2.dropna(subset= "Author Keywords")

# In[ ]:
#save keyword column into a list for easier processing

keywords = list(df2["Author Keywords"])
keyw = [kw.split("; ") for kw in keywords]

import itertools
keywords2 = (list(itertools.chain.from_iterable(keyw)))

keywords = [kw.lower() for kw in keywords2]
# In[ ]: dictionaries

#summarize synonyms of selected terms
syn_radical = ["extremism", "extremist", "extreme", "radical", "radicalisation", "radicalism","radicalization",
               "violence", "violent", "terror", "terrorism", "violent-activism",
               "activist", "political", "political-violence", "violent-extremism", "community-violence", "radical-behaviorism"]

syn_adol = ["youth", "adolescent", "adolescence", "student", "students", "juvenile", "teen",
            "teenager", "young-people", "young-person", "child", "young", "children"]

terror_mangmnt = ["terror-management", "fear-of-death", "terror-management-theory", "death-anxiety", "mortality-salience"]


#countries
from country_list import countries_for_language
# countries_for_language returns a list of tuples now, might be changed to an OrderedDict
countries_dict = dict(countries_for_language('en'))
countries_raw = list(countries_dict.values())
countries = [term.lower() for term in countries_raw]

dict_constructs ={"radicalism": syn_radical,
                  "adolescence": syn_adol,
                  "terror-management": terror_mangmnt,
                  "PTSD": ["ptsd", "posttraumatic-stress-disorder", "post-traumatic-stress-disorder"],
                  "religion": ["religion", "religiosity", "religious"],
                  "conflict":["conflict", "armed-conflict", "war"],
                  "islam": ["muslim", "islam"],
                  "education": ["higher-education", "education"],
                  "country": countries}


exclude_terms_raw = ["study", "university", "school", "and", "result", "year", "association", "sample", "level", "analysis",
                  "effect", "group", "control", "method", "treatment", "conclusion", "finding",
                  "intervention", "scale", "relation", "model", "research", "score", "attitude", 
                  "frequency", "indicator", "literature", "number", "odd", "pathway", "size", "time",
                  "outcome", "participant", "questionnaire", "difference", "measure", "variable", "datum",
                  "report", "skill", "trait", "rate", "total", "influence", "rating", "variance", "component",
                  "course", "hour", "index", "medium", "prevalence", "theory", "objective", "self-report", "change",
                  "lifetime", "american", "^BEHAVIOR$", "INDIVIDUAL-DIFFERENCES", "ASSOCIATIONS", "RESPONSES",
                  "FIT INDEXES", "MEDIATING ROLE", "SCALE", "EXPERIENCE", "INTERVENTION", "INVENTORY", "OUTCOMES",
                  "RELIABILITY", "SENSITIVITY", "UNITED-STATES", "CONSEQUENCES", "INITIAL VALIDATION", "LIFETIME PREVALENCE",
                  "TRAJECTORIES", "CONTEXT", "EXPERIENCES", "FOLLOW-UP", "IMPACT", "MISSING DATA",
                  "STUDENTS", "RANDOMIZED CONTROLLED-TRIAL", "PSYCHOMETRIC PROPERTIES", "VALIDATION", "MODEL",
                  "RISK-FACTORS", "RISK", "DIFFICULTIES", "ASSOCIATION", "METAANALYSIS", "VALIDITY", "PREDICTORS",
                  "QUESTIONNAIRE", "BEHAVIORS", "COGNITIVE-BEHAVIORAL THERAPY", "MIDDLE CHILDHOOD", "SELF-REPORT",
                  "SCHOOL", "DIFFICULTIES QUESTIONNAIRE",
                  "COMMUNITY SAMPLE", "EXPOSURE", "clinic", "disaster",
                  "dissociation", "distress", "involvement", "recognition", "therapy", "LIFE", "problem", "behavior",
                  "age", "exposure", "role", "development", "background", "patient", "childhood", "dimension",
                  "predictor", "regression", "assessment", "process", "response", "severity", "functioning", "pattern",
                  "data", "experience", "mechanism", "evidence", "program", "status", "checklist", "mediation", "onset",
                  "order", "perspective", "subject", "design", "domain", "equation", "goal", "grade", "point", "need",
                  "task", "trial", "interview", "mediator", "purpose", "approach", "body", "period", "practice",
                  "quality ", "activity", "inventory", "deficit", "perception", "prevention", "form", "aim",
                  "behaviour", "interaction", "type", "importance", "individual", "baseline", "month", "range", 
                  "syndrome", "ability", "awareness", "follow-up", "impairment", "modeling", "person", "condition",
                  "population", "elsevier", "feature", "profile", "right", "style", "all", "improvement", "function",
                  "ltd.", "history", "impact", "subscale", "test", "context", "service", "system", "value", "version",
                  "addition", "implication", "adult", "teacher", "care", "correlation", "diagnosis", "der", "sensitivity", 
                  "competence", "increase", "disturbance"]
exclude_terms = [term.lower() for term in exclude_terms_raw]


# In[] processing keywords per document for cooc matrix

kw_per_doc = list(df2["Author Keywords"])
kw_per_doc2 = [kw.lower() for kw in kw_per_doc]
kw_per_doc = [kw.split("; ") for kw in kw_per_doc2]
kw_per_doc2 = kw_per_doc


#connect keywords with multiple terms by "-"
kw_per_doc = []
for el in kw_per_doc2:
    kwords=[]
    for k in el:
        kwords.append(re.sub(" ", "-", k))
    kw_per_doc.append(kwords)
kw_per_doc2 = kw_per_doc


#get rid of all non-letter types (especially number keywords?!), keep "-"
kw_per_doc = []
for el in kw_per_doc2:
    kwords=[]
    for k in el:
        kwords.append(re.sub(r'[^a-zA-Z-]', '', k))
    kw_per_doc.append(kwords)
kw_per_doc2 = kw_per_doc


#lemmatize - but try other lemmatizer: "stanford corenlp lemmatizer"-google it
lemma = nltk.stem.WordNetLemmatizer()

kw_per_doc = []
for el in kw_per_doc2:
    kwords=[]
    for k in el:
        kwords.append(lemma.lemmatize(k))
    kw_per_doc.append(kwords)
kw_per_doc2 = kw_per_doc


#excluding stop words/exclusion words
kw_per_doc = []
for el in kw_per_doc2:
    kwords=[]
    for k in el:
        if not k in exclude_terms:
            kwords.append(k)
    kw_per_doc.append(kwords)
kw_per_doc2 = kw_per_doc


#change dict values
for el in kw_per_doc2:
    for idx, k in enumerate(el):
        for e in range(len(dict_constructs)):
            if k in list(dict_constructs.values())[e]:
                el[idx] = list(dict_constructs.keys())[e]
                
                
#calculate average number of kw per doc
average_kw = np.mean([len(kw) for kw in kw_per_doc2]) #5.42
###

#finish processing, turn lists within lists into strings for countVectorizer
kw_per_doc = [" ".join(k) for k in kw_per_doc2]

#cleaning
del(k,kwords,kw_per_doc2,lemma,idx,exclude_terms_raw,e,el)

# In[] from keywords per document, extract keywords in general for freq analysis
keyw = [kw.split(" ") for kw in kw_per_doc]
keywords = (list(itertools.chain.from_iterable(keyw)))

len(keywords)
len(set(keywords))

#what countries occur?
countries_in_kw = [kw for kw in keywords if kw in countries]
freq = nltk.FreqDist(countries_in_kw)
freq_countries = freq.most_common()

# In[ ] #attempt for neg binomial for frequency
freq = nltk.FreqDist(keywords)
most_com_kw = freq.most_common(146)

# In[ ]cooc to dataframe

from sklearn.feature_extraction.text import CountVectorizer
# Convert a collection of text documents to a matrix of token counts
cv = CountVectorizer(min_df=1, token_pattern = r'(?u)\b\S\S+\b') #pattern modified to keep "-"-terms
# matrix of token counts
X = cv.fit_transform(kw_per_doc)
X.getnnz()
names = cv.get_feature_names_out() # This are the entity names (i.e. keywords)
df_dtm = pd.DataFrame(data = X.toarray(), columns = names)
df_dtm.to_csv("dtm.csv", index=False)

cooc = (X.T * X) # matrix manipulation
cooc.setdiag(0) # set the diagonals to be zeroes as it's pointless to be 1

df_cooc = pd.DataFrame(data = cooc.toarray(), columns = names, index = names)
df_cooc.to_csv("cooc.csv", index = False)

