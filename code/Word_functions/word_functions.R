## Negative Binomial function
select_words <- function(dtm, q = .95){
  d <- colSums(dtm)
  fit <- fitdist(d, "nbinom")
  thres <- qnbinom(q, size=fit$estimate["size"], mu=fit$estimate["mu"])
  return(d > thres)
}

select_cooc <- function(cooc, q = .95){
  mat.summ   <- summary(cooc)
  mat.summ <- mat.summ[!mat.summ$i == mat.summ$j, ]
  lower.summ <- subset(mat.summ, i >= j)
  fit <- fitdist(lower.summ$x, "nbinom")
  thres <- qnbinom(q, size=fit$estimate["size"], mu=fit$estimate["mu"])
  lower.summ <- lower.summ[!lower.summ$x < thres, ]
  out <- sparseMatrix(i = lower.summ$i,
               j = lower.summ$j,
               x = lower.summ$x,
               dims = dim(cooc), symmetric = TRUE)
  rownames(out) <- rownames(cooc)
  colnames(out) <- colnames(cooc)
  is_zero <- rowSums(out) == 0
  out <- out[!is_zero, !is_zero]
  attr(out, "thres") <- thres
  return(out)
}

create_cooc <- function(dtm){
  dtm_binary <- dtm > 0
  Matrix::t(dtm_binary) %*% dtm
}

unmatched <- function(words, dict){
  dict_matches <- lapply(unlist(dict), function(this_reg){
    grep(this_reg, words)
  })
  sort(table(words[c(1:length(words))[-unique(unlist(dict_matches))]]), decreasing = TRUE)
}