#Create raster object for throw tracking
library(raster)
field <- raster(nrow=40, ncol=120, xmn=-60, xmx=60, ymn=-20, ymx=20)
#Display "end zones" on raster object
n <- c(rep(1,25),rep(0,70),rep(1,25))
n <- c(rep(n,40))
values(field) <- n
par(mai = c(.5,.5,.5,.5))
plot(field)
#Enter clicks on field, click "Finish" on top right to stop
throws <- click(field, n = Inf, id = TRUE, xy = TRUE, cell = FALSE, show = TRUE)
#Display data
View(throws)