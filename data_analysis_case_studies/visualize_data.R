# Load required packages
library(tidyverse)
library(dplyr)
library(data.table)

# Set working direcory
setwd("~/Documents/coursera_case_study_bikes")

# Read in data
data <- fread("clean_bike_trip_data.csv")

data_by_month <- data[, .(.N), by="start_month"]

months <- c("Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Feb", "Mar", "Apr", "May", "Jun")
ticks <- c(0.7, 1.9, 3.1, 4.3, 5.5, 6.7, 7.9, 9.1, 10.3, 11.5, 12.7)

pdf("monthly_ride_count.pdf", height = 5, width = 10)
par(mar = c(5,10,5,5))
data_by_month[, barplot(N, xlim=c(0,13), ylim = c(0, max(N)), yaxt = 'n', main = paste0("Number of bike trips per month", "\n", "(2020-2021)"), xlab = "Month")]
data_by_month[, text(ticks, par("usr")[3] - 0.2, labels = months, pos = 1, xpd = TRUE)]
mtext("Number of rides", side = 2, line = 5)
axis(2, at = c(200000, 400000, 600000, 800000, 1000000, 1200000), labels = c("200,000", "400,000", "600,000", "800,000", "1,000,000", "1,200,000"), las = 1)
dev.off()
