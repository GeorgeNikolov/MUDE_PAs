# Project 2: Modelling Road Deformation using Non-Linear Least-Squares

*[CEGM1000 MUDE](http://mude.citg.tudelft.nl/): Weeks 3 & 4, Friday Sep 22 & Friday Sep 29, 2023.*

In this assignment you will model the deformation of a newly built highway in the <a href="https://www.groenehart.nl/the-green-heart-of-holland" target="_blank"> Green Heart</a> in the Netherlands using non-linear least-squares. You will also apply a hypothesis test to test whether the model you chose was correct. 

New packages that you might have to add to the `mude` environment are `datetime` and `pandas`. For those of you that are not yet familiar with `pandas`, don't be concerned: this week we only use it to import and convert the data to a numpy array. We will learn how to use it more thoroughly later, as it is a very useful package for working with time series.

## Objectives

In this assignment you will:
- Set up the system of equations for a linear system
- Find the best linear unbiased estimates for a linear estimation problem
- Present the estimated parameters and their quality and use confidence intervals
- Linearize a non-linear estimation problem
- Use an iterative scheme for the non-linear least squares estimation
- Apply a hypothesis test to decide whether one of the models can be accepted
- Assess the quality and reflect on the estimation and testing results

Note that the last 4 items are part of Week 4, and will be shared with you during that week.

## Report Requirements

A project report is required, `Report.ipynb`, which should be a self-contained document describing your analysis and interpretation, as well as any decision-making with regards to programming (e.g., setting up extra functions or using extra packages). For Project 2, the Report structure is provided to you in the form of **Tasks**, so you only need to fill in code and Markdown cells as directed (later in the semester you will have more freedom in writing the report contents). In your answers you should explain in your report how you obtained your results (even if you are just following the procedure as described in the Tasks). For example, if you refer to a Python function, explain how and why you used it. In addition, the analysis and interpretation of your results are at least as important as the results themselves (numerical solutions and plots). You should refer to the results of your analyses specifically and quantitatively in your answers. When creating plots, don’t forget to include axis labels with units. See Assessment section below for additional information.

You will submit the report via the GitLab repository for your group. Only one person makes the commit to submit the report on behalf of the entire group.

You are welcome to use Deepnote for collaborating with your group, but keep in mind that you are responsible for exporting the document correctly, checking the formatting and making sure that the analysis runs as-submitted from your GitLab directory. See the [website](https://mude.citg.tudelft.nl/software/deepnote/) for more information.

## Timeline and Deadlines

We will work on this project during the Friday sessions on Sep 22 and Sep 29. You are required to submit the current draft of your notebook at the end of each session (12:30) via GitLab. This is a strict deadline; note, however, that the report submitted during the first Friday will not be graded as this is for you to practice submitting a notebook via GitLab, as well as for us to evaluate group progress.

We will review the project reports during the week following their submission and will try to return feedback by the end of Wednesday, along with the solution.

While these deadlines are strict, they are meant to keep you on on track with the module, and to ensure that you get timely feedback. Even if your assignment is incomplete, we will adapt the grading as-needed if it appears the assignment was too long. In addition, if there are programming related deficiencies with your notebook (i.e., filesize too large, or errors in the code), we will notify you of the problem and request that you resubmit. Although the deadline of the projects is the end of Q1; note that if you opt to submit the project report after Wednesday, you will be given an alternative assignment.

## Supplementary Material

Supplementary materials have been provided in a GitLab repository for your group. They include:

- this `README.md` with instrucions.
- `Report.ipynb`: the primary notebook where you are expected to make your calculations and report your results and answers.
- `data/`: a sub-directory containing 3 `*.csv` files, explained in the notebook.

## Project Assessment Categories

General information about the project assessment can be found on the course website. In particular for this project, the assessment will focus on:

* **Documentation:** Readable, well-structured and well-formatted answers in Markdown cells. Plots have been formatted with axes, titles, units, etc.
* **Application:** Correctly apply concepts from Chapter 2 and 3 of the textbook.
* **Programming:** implement and use the functions as asked. The notebook should not exceed 3 MB and should run without error from your GitLab repository within a maximum time of 3 minutes. 
* **Interpretation:** Findings reported based on good evidence and sound reasoning. Refers to results quantitatively, as well as qualitatively (figures).

The weight for each category is 25%.

**End of file.**

<span style="font-size: 75%">
&copy; Copyright 2023 <a rel="MUDE Team" href="https://studiegids.tudelft.nl/a101_displayCourse.do?course_id=65595">MUDE Teaching Team</a>, TU Delft. This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-nc-sa/4.0/">CC BY-NC-SA 4.0 License</a>.