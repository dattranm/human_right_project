install.packages("readxl")
library("readxl")
source("http://www.sthda.com/upload/rquery_cormat.r")
require("corrplot")
# Dataset 1
a <- read_excel("D:/Task_2_Dat_Tran/ds1.xlsx")
rquery.cormat(a)
a$hr.violation.rim[which(a$hr.violation.rim == "666")] <- "2"
a$hr.violation.rim[which(a$hr.violation.rim == "999")] <- "3"
a$hr.violation.af[which(a$hr.violation.af == "666")] <- "2"
a$hr.violation.af[which(a$hr.violation.af == "999")] <- "3"
a$hr.violation.vg[which(a$hr.violation.vg == "666")] <- "2"
a$hr.violation.vg[which(a$hr.violation.vg == "999")] <- "3"
a$hr.violation.cb[which(a$hr.violation.cb == "666")] <- "2"
a$hr.violation.cb[which(a$hr.violation.cb == "999")] <- "3"
a$hr.violation.rim <- as.numeric(a$hr.violation.rim)
a$hr.violation.af <- as.numeric(a$hr.violation.af)
a$hr.violation.vg <- as.numeric(a$hr.violation.vg)
a$hr.violation.cb <- as.numeric(a$hr.violation.cb)
a_1 <- subset(a, select = -sentence.id)
rquery.cormat(a_1)
# Chosse RIM and AF. Reason: High Corr Stat(0.38), CB's work is very different compared to others, and VG used too much "666" and "999" compared to others.

#Dataset 2
b <- read_excel("D:/Task_2_Dat_Tran/ds2.xlsx")
rquery.cormat(b)
b$hr.violation.AD[which(b$hr.violation.AD == "666")] <- "2"
b$hr.violation.AD[which(b$hr.violation.AD == "999")] <- "3"
b$hr.violation.CA[which(b$hr.violation.CA == "666")] <- "2"
b$hr.violation.CA[which(b$hr.violation.CA == "999")] <- "3"
b$hr.violation.KH[which(b$hr.violation.KH == "666")] <- "2"
b$hr.violation.KH[which(b$hr.violation.KH == "999")] <- "3"
b$hr.violation.AD <- as.numeric(b$hr.violation.AD)
b$hr.violation.CA <- as.numeric(b$hr.violation.CA)
b$hr.violation.KH <- as.numeric(b$hr.violation.KH)
b_1 <- subset(b, select = -sentence.id)
rquery.cormat(b_1)
# Choose AD and KH. Reason: High Corr Stat(0.53), CA got too many "666" and "999" compared with AD and KH, and with unreliable format as well. CA did sloppy work in general.

