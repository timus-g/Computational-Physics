sums <- read.csv("dist_sum_random_walk.csv", header=FALSE, stringsAsFactors = TRUE)
summary(sums)
pdf("dist_sum_random_walk_test.pdf") # create a pdf file to save the plot

hist(sums)

dev.off() # close the pdf file
