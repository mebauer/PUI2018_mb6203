### You will recieve an email tonight with the name, nyuID, and GitHub username of a classmate.
*check that at least one of these class-mates is not already in your group for HW4 and contact me promptly if they both are! By lunch time tomorrow I want to do the necessary reassignments so that each of you is paired with a classmate so I need to know ASAP.

*look in the classmate HW4_<netid> repo ASAP and identify their submission for the citibike project. If you cannot find it contact them immediately!

*Fork their repository and clone it (you did this in HW1, look at the instructions in the HW1 README if you need to refresh your memory) - only read up to the experimantal setup and verify the data to answer the question is available. Do not consider the way they answer the question if they already did!

*Read it carefully (but do not modify the notebook)! You have to:

### a. verify that their Null and alternative hypotheses are formulated correctly

*Null hypothesis: average trips per Sunday is less than average trips per Saturday in January.

*Alternative hypothesis: average trips per Sunday is more than or equal to than average trips per Saturday in January.

Hi Sam, great concept! I really like this hypothesis. I probably would have formulated the Null hypothesis as *average trips per Sunday is less than or **equal to** average trips per Saturday in January.* If they were indeed equal, than your hypothesis would be rejected. However, I would double-check this with someone with more insight, as I'm still improving my understanding of hypothesis testing. Perhaps Professor Bianco can provide more guidance.

### b. verify that the data supports the project: i.e. if the a data has the appropriate features (variables) to answer the question, and if the data was properly pre-processed to extract the needed values (there is some flexibility here since the test was not chosen yet)

The data seems to support the project. As you mentioned in your README, I am interested in why there was a week missing in January. Perhaps something to review. 

### c. chose an appropriate test to test H0 given the type of data, and the question asked. You can refer to the flowchart of statistical tests for this in the slides, or here, or Statistics in a Nutshell.

I would apply a *t* Test to the data to see if there is a significant difference between the two groups. If you do decide to perform the *t* Test, make sure to specify the level of probability (alpha level, level of significance, p) you are willing to accept (p < .05 for example).

I chose this test because I'm interested to see if there is a significant difference between the average trips on Sunday vs. Saturday. I also chose this test because the data is numeric, as we can add average daily ridership for each day. I received guidance when choosing an appropriate test from Professor Bianco's link: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3116565/


*Write your comments, suggestions, and suggested an appropriate statistical test, motivating your test choice, in a markdown named CitibikeReview_<netID>.md. Suggest variations on the question, if you think it may be made more interesting.

As you mentioned, I would be interested to see what would happen if the experiment included more data.

Also, great job of the cleaning and parsing of the data. Your comments were very easy to read and understand. 

Please keep me updated on this project!

- Mark Bauer

