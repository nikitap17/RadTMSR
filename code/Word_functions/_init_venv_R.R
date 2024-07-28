if(!require("renv", quietly = T)){
  install.packages("renv")
}

renv::init()

library(tidyverse)
library(fitdistrplus)
library(udpipe)
library(Matrix)
library(RaschSampler)
library(abind)

renv::snapshot()