# Load required packages
library(tidyverse)
library(dplyr)
library(data.table)

# Set working direcory
setwd("~/Documents/coursera_case_study_bikes")

# Load data
files <- list.files(pattern = "*divvy-tripdata.csv")
concat_files <- rbindlist(lapply(files, fread, header = TRUE))

# Save concatenated file into a combined CSV
fwrite(concat_files, file = "combined_bike_trip_data.csv", col.names = TRUE, row.names = FALSE)
