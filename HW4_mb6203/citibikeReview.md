# Ideaun
unclear: did you mean "Subscribers tend to choose biking for commuting _more likely than_ than customer."

# Null hypothesis
"The proportion of customers biking on a daily basis is the same or higher than the proportion of subscribers biking on a daily basis."
_commuting_ generally means going to and from work. I think your idea was that there is a higher number of customers than subscribers. 

what is proportion? i think you mean the number, or the rate, not the proportion

or you would have to say the proportion compared to what?

I cannot say if the NH is appropriate because your idea is not clear. Please rething this. Commuting is fine in the idea, but here you have to define who is commuting and who is not based on info int he data:
for example the hour of the day, or the day of the week. So it would be the fraction of costumer biking on days of the week [or certain hours of the day] to costumer bikeng at other times is higher/lower... etc



# Formula
Missing!! please add a formula to go with the NH

# Data
This is basically my cells of code copied and pasted. Which is ok, but you are missing an opportunity to learn something for yourself. 
Because the question is unclear I cannot tell you exactly how the data should be processed, but this data is not processed fully to answer the question.

If you want to talk about commuting, typically you would select only rush hours: e.g. 8-10 AM and 4-7 PM. 

Or perhaps you are using weekday as workday == communting and weekend == not communting so that is how you split the data? but then you have not grouped it by those two group.

I think you have to rethink your question, forulate the hypothesis, and rething your data processing then.

# Test

If in the end you want a test of proportions (since you ahd proportion in the NH) a chi sq test would be appropriate and better than a Z test, since the Z test assumes gaussianity while the chi sq test is non-parametric

https://www.r-bloggers.com/comparison-of-two-proportions-parametric-z-test-and-non-parametric-chi-squared-methods/

