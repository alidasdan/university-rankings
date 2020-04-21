university-rankings
====================

This repository contains data and code for university or college
rankings as studied in [1].

## INFO ABOUT THE STUDY REPORTED IN [1]

The abstract of [1] explains it best what the study was about and what
this data was used for:

> University or college rankings have almost become an industry of
> their own, published by US News \& World Report (USNWR) and similar
> organizations. Most of the rankings use a similar scheme: Rank
> universities in decreasing score order, where each score is computed
> using a set of attributes and their weights; the attributes can be
> objective or subjective while the weights are always subjective. This
> scheme is general enough to be applied to ranking objects other than
> universities. As shown in the related work, these rankings have
> important implications and also many issues. In this paper, we take a
> fresh look at this ranking scheme using the public College dataset;
> we both formally and experimentally show in multiple ways that this
> ranking scheme is not reliable and cannot be trusted as authoritative
> because it is too sensitive to weight changes and can easily be
> gamed. For example, we show how to derive reasonable weights
> programmatically to move multiple universities in our dataset to the
> top rank; moreover, this task takes a few seconds for over 600
> universities on a personal laptop. Our mathematical formulation,
> methods, and results are applicable to ranking objects other than
> universities too. We conclude by making the case that all the data
> and methods used for rankings should be made open for validation and
> repeatability.

## INFO ABOUT THE REPOSITORY

There are three directories: data, doc, and src. The data directory
contains the data files, the doc directory contains a pdf copy of [1],
and the src directory contains a Python program to process some of the
data files.

The data directory contains

1. A copy of the public College dataset files: aaup.*, usnews.*, and
info.txt. The 'dat' files contain the data, and the 'documentation'
and 'txt' files are the documentation about the data files (e.g.,
their schema, the meaning of each field, etc.).

> The College dataset is part of the StatLib datasets archive, hosted
> at the Carnegie Mellon University; it contains data about many (1,329
> to be exact) but not all American higher education institutions. Its
> collection in 1995 was facilitated by the American Statistical
> Association. The two data sources are Association of American
> University Professors (AAUP) and US News & World Report (USNWR), which
> contribute 17 and 35 attributes, respectively, per university. There
> are many attributes with missing values for multiple universities.

2. The 'out' files are the ones that we generated as part of the study
reported in [1].

   The 'combined*' files give a combined version of the aaup and
   usnews data.

   The 'sorted*' files give a ranking of universities with
   deterministic weights.

   The 'random*' files give a ranking of universities with randomized
   weights (after a 10K iteration of Monte Carlo simulation with
   uniformly random weights).

3. The 'arith' and 'geo' refer to the use of the arithmetic mean and
geometric mean formulas, respectively, for computing a ranking score.

4. The 'uni' and 'non_uni' refer to the use of uniform (the same
weight or no weights case) and non-uniform weights (subjectively
derived weights) used in ranking score computations.

The src directory contains a Python program to create the
'combined.dat' file.

## REFERENCES

[1] A. Dasdan et al., How Reliable are University Rankings?,
URL="https://arxiv.org/abs/2004.09006", 2020.
