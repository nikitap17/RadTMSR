
if(!require("renv", quietly = T)){
    options(repos = c(CRAN = "https://cloud.r-project.org"))
    install.packages("renv")
}

renv::restore()

library(tidyverse)
library(fitdistrplus)
library(udpipe)
library(Matrix)
library(RaschSampler)
library(abind)

source("word_functions.R")



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
