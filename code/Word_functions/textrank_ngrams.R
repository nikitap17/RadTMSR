library(textrank)
library(readr)


data <- read_csv("../RTMR_Output/tr_nounbydoc.csv",show_col_types = FALSE)

kw_tr <- textrank_keywords(x = data$"0", 
                           ngram_max = 3, p = 0.025, sep = " ")

write_csv(subset(kw_tr$keywords, ngram > 1), "../RTMR_Output/textrank_keywords.csv")


#nn_d <- subset(kw_tr$keywords, kw_tr$keywords$ngram == 1)

#kw_tr$keywords
