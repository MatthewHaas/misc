# Load required packages
library(tidyverse)
library(dplyr)
library(data.table)

# Set working direcory
setwd("~/Documents/coursera_case_study_bikes")

# Read in data
data <- fread("combined_bike_trip_data.csv")

# Remove duplicates
data_dedup <- data[!duplicated(data$ride_id),]

# Make new columns for start date and start time
data_dedup[, c("start_date", "start_time") := tstrsplit(started_at, " ", fixed = TRUE)]

# Make new columns for end date and end time
data_dedup[, c("end_date", "end_time") := tstrsplit(ended_at, " ", fixed = TRUE)]

# Now that we have new columns for start and end dates and time, remove original columns--no longer needed
data_dedup[, started_at := NULL]
data_dedup[, ended_at := NULL]

# Save data
fwrite(data_dedup, file = "clean_bike_trip_data.csv", col.names = TRUE, row.names = FALSE)
