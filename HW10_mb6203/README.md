# PUI2018 HW 10.
## Team Collaboration:

This is mainly for the second hw, which I worked in a pretty large group throughout the duration of the assignment. Team members were Kate Cauley, Alia Kasem, Manrique Vargas, Max Humphreys, and Shivam Pathak. Shivam really helped me with the plotting at the end and the chi squared.

## ASSIGNMENTS:

### Assignment 1. 
LR Test Lab


### Assignment 2.
MapPLUTO Data and relationship between buildings and energy



### Useful Notes from Professor

Take home points from lecture:

- A model is a simplification of a phenomenon that can be conveyed with a mathematical formula

- Models are useful at predicting and explaining observations.

- Every mathematical formula describes a family of models. For example a line model describes an twice-infinite (infinite**2) set of lines each corresponding to a slope-intercept pair. Methods to chose the _best fitting_ set of parameters (a process which we call _model fitting_) include
  	- minimization of residual squared (e.g. OLS)
	- minimization of chi squared
	- maximization of likelihood (via minimization of negative log-likelihood)
	

- Important questions about your model are:

 	- Is my model "close enough" to my observations (e.g. does the line go close enough to the points) - this can be answered by R^2 and chi^2. The first is used in absence of measurement uncertainties, the latter is used when you can quantify the uncertainty in your measurements. R^2 is the fraction of variance in the data explained by the model, for a perfect model it is R^2=1. ~0.5 is generally acceptable in social sciences, >0.8 in physical sciences. Chi^2 follows a chi square distribution with a _k_ parameter equal to the number of degrees of freedom of data (Ndof = number of observations - number of parameters in the model). Chi^2/Ndof should be close to 1.

 	- As the complexity of a model increases (number of parameters increases) the model becomes more "flexible" and it is bound to fit the data better. Accordingly, R^2 and chi^2 must improve. This **does not** mean that a more complex model is better than a less complex model. Often the opposite is true.
 
 	- Is my model "overfitting" the data? Have I added too much complexity (in violation of Occam's razor and thus losing predictive power)? This question can be answered by the Reduced chi^2 (the chi^2 divided by the number of degrees of freedom _of the data_ which has expectation value 1) or by the Adjusted R^2. Both incorporate a measure of how close the model prediction is to the observations weighted against the complexity of the model. However neither gives a formal, quantitative answer.
The likelihood ratio test gives a formal answer to which model is preferable (in terms of NHST) as long as the models are nested (the complex model contains the simpler one, for example a*x^2 + b*x + c (quadratic model) contains a*x + b (line model), a*z + b*x + c  (linear bi-variate model) also contains a*x + b (line model). The LR statistics, LR = -1 log_e(maxLikelihoodSimplerModel / maxLikelihoodComplexModel), follows a chi square distribution with number of degrees of freedom equal to the difference in the number of parameters in the two models (1 in both examples above), and thus it can be compared to a chi square table to reject the Null hypothesis which is that _"the simpler model is preferable"_.

 	- Is my model missing something that could be modelled? The residuals of a model that captures all deterministic factors in the data generation (without modelling the stocastic changes) should be randomly distributed, because what is left after everything that could be modeled should only the uncertainties in the data. Visual inspection of the residuals is often revealing when the dataset is not too large, and the distribution of the residuals can be compared to a random (Gaussian in general) distribution.

- the technical skills required to do all this (in PUI) are: 

	- data munging
	
	- model fitting with, e.g., statsmodels
	
	- knowing how to interpret statistical tests (NHST)
