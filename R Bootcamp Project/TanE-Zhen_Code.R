View(mtcars)

pairs(mtcars)

model.full=lm(disp ~ .,data=mtcars)
(summary.full=summary(model.full))

model.red = lm(disp~hp+wt+carb,data=mtcars)
(summary.red=summary(model.red))
