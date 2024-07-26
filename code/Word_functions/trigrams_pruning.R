library(fitdistrplus)
library(readr)
source("word_functions.R")
#source("circle2.R")
library(data.table)
#library(bibliometrix)
#library(yaml)
library(stringr)
#library(lattice)
#library(topicmodels)
library(udpipe)
library(igraph)
library(wordcloud)
library(Matrix)
library(ggplot2)
library(yaml)



## Trigram occurrences ------------------------------------------------------
## Import trigram_nounbydoc.csv file created with Python
nounbydoc <- read_csv("../RTMR_Output/Abstracts/trigram_nounbydoc.csv",show_col_types = FALSE)
#View(nounbydoc)

### Negative Binomial function
select_words <- function(dtm, q = .95){
  d <- colSums(dtm)
  fit <- fitdist(d, "nbinom")
  thres <- qnbinom(q, size=fit$estimate["size"], mu=fit$estimate["mu"])
  return(d > thres)
}


# Frequency of word by doc (doc term matrix)
dtm <- udpipe::document_term_matrix(document_term_frequencies(nounbydoc))


# Negative binomial
set.seed(5348)
dtm_top <- dtm[, select_words(dtm, .95)]
dtm_top <- dtm_top[rowSums(dtm_top) > 0, ]


## Word frequencies
topterms <- colSums(dtm_top)
word_freq <- data.frame(Word = names(topterms),row.names = NULL)
write.csv(word_freq, "../RTMR_Output/Abstracts/trigrams_pruned.csv", row.names = FALSE)
