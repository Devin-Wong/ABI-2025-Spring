# Data Instruction

## 1. Hitters

A data frame with 322 observations of major league players on the following 20 variables.

- `AtBat`

  Number of times at bat in 1986

- `Hits`

  Number of hits in 1986

- `HmRun`

  Number of home runs in 1986

- `Runs`

  Number of runs in 1986

- `RBI`

  Number of runs batted in in 1986

- `Walks`

  Number of walks in 1986

- `Years`

  Number of years in the major leagues

- `CAtBat`

  Number of times at bat during his career

- `CHits`

  Number of hits during his career

- `CHmRun`

  Number of home runs during his career

- `CRuns`

  Number of runs during his career

- `CRBI`

  Number of runs batted in during his career

- `CWalks`

  Number of walks during his career

- `League`

  A factor with levels `A` and `N` indicating player's league at the end of 1986

- `Division`

  A factor with levels `E` and `W` indicating player's division at the end of 1986

- `PutOuts`

  Number of put outs in 1986

- `Assists`

  Number of assists in 1986

- `Errors`

  Number of errors in 1986

- `Salary`

  **1987 annual salary on opening day in thousands of dollars**

- `NewLeague`

  A factor with levels `A` and `N` indicating player's league at the beginning of 1987

## 2. Caravan

**Description**

- The data contains 5822 real customer records. Each record consists of 86 variables, containing sociodemographic data (variables 1-43) and product ownership (variables 44-86). The sociodemographic data is derived from zip codes. All customers living in areas with the same zip code have the same sociodemographic attributes. Variable 86 (`Purchase`) indicates whether the customer purchased a caravan insurance policy. Further information on the individual variables can be obtained at http://www.liacs.nl/~putten/library/cc2000/data.html



**Format**

- A data frame with 5822 observations on 86 variables.

**Source**

- The data was originally supplied by Sentient Machine Research and was used in the CoIL Challenge 2000.



**References**

- P. van der Putten and M. van Someren (eds) . CoIL Challenge 2000: The Insurance Company Case. Published by Sentient Machine Research, Amsterdam. Also a Leiden Institute of Advanced Computer Science Technical Report 2000-09. June 22, 2000. See http://www.liacs.nl/~putten/library/cc2000/
- P. van der Putten and M. van Someren. A Bias-Variance Analysis of a Real World Learning Problem: The CoIL Challenge 2000. Machine Learning, October 2004, vol. 57, iss. 1-2, pp. 177-195, Kluwer Academic Publishers
- James, G., Witten, D., Hastie, T., and Tibshirani, R. (2013) *An Introduction to Statistical Learning with applications in R*, [www.StatLearning.com](http://127.0.0.1:9597/help/library/ISLR/html/www.StatLearning.com), Springer-Verlag, New York



## 3. Gene Data

**Description**

- The data consists of a number of tissue samples corresponding to **four distinct types of small** round blue cell tumors. For each tissue sample, 2308 gene expression measurements are available.

**Format**

- The format is a list containing four components: `xtrain`, `xtest`, `ytrain`, and `ytest`. `xtrain` contains the 2308 gene expression values for 63 subjects and `ytrain` records the corresponding tumor type. `ytrain` and `ytest` contain the corresponding testing sample information for a further 20 subjects.

