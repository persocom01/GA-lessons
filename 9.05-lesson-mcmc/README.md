# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Lesson: Markov Chain Monte Carlo (MCMC) Methods

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Lesson | MCMC Notebook | [Link](./starter-code.ipynb)|

---

## Learning Objectives

*After this lesson, students will be able to:*

1. Identify the Markov property.
2. Describe Monte Carlo simulations.
3. Describe how MCMC works.
4. Identify situations where MCMC is beneficial.

---

## Student Requirements

*Before this lesson(s), students should already be able to:*

1. Describe prior distributions, likelihood functions, and posterior distributions.
2. Fit models and produce traceplots in PyMC.

---

## LESSON OUTLINE

> Total Time: *120 minutes*

I. Recap (10 minutes)
- Priors, Likelihoods, Posteriors
- Conjugacy

II. Markov Chains (30 minutes)
- Markov Property

III. Monte Carlo Methods (30 minutes)
- Monte Carlo Simulations

IV. MCMC Methods (50 minutes)
- Acceptance-Rejection Algorithms
- Visualization

---

## OPTIONAL: Resources for Practice and Learning

*For supplemental reading material on this topic, check out the following resources:*
- [A DSI-DC-6 grad's blog post about MCMC methods.](https://towardsdatascience.com/a-zero-math-introduction-to-markov-chain-monte-carlo-methods-dcba889e0c50)
- [A great set of recommendations for how to visualize posterior distributions.](https://ctg2pi.wordpress.com/2015/02/24/principles-of-posterior-visualization/)
- [A visualization of MCMC for two parameters](https://chi-feng.github.io/mcmc-demo/app.html#RandomWalkMH,standard)
- If you like Bayesian ideas but want to learn more/solidify your understanding, check [this out](http://jamessample.github.io/enviro_mod_notes/). (Despite the link, it's not just about environmental statistics, but those interested in spatiotemporal projects and work will likely be heavily Bayesian-oriented.) This will be a great buildup from the most basic aspects of statistics/distributions all the way to MCMC, so you could learn a lot that we, because of time, simply can't get into. Within these notes, there are also some **excellent** iPython notebooks with neat 2D and 3D visualizations available.
- [The source for most of the in-class gifs as well as an MCMC walkthrough](https://blog.stata.com/2016/11/15/introduction-to-bayesian-statistics-part-2-mcmc-and-the-metropolis-hastings-algorithm/)
- [This blog post](https://jeremykun.com/2015/04/06/markov-chain-monte-carlo-without-all-the-bullshit/) helps those who aren't a fan of the statistical notation. 
- [Here's a GREAT overview of MCMC AND its application in Python.](http://twiecki.github.io/blog/2015/11/10/mcmc-sampling/)
- [Lots of people post references on StackOverflow for introductions to MCMC. These will be more rigorous.](http://stats.stackexchange.com/questions/256290/basic-references-on-mcmc-for-bayesian-statistics)
- [Exceptional textbook on Bayesian inference and statistical thinking](http://xcelab.net/rmpubs/sr2/statisticalrethinking2.pdf)
- [This 18min video lecture](https://www.youtube.com/watch?v=12eZWG0Z5gY) nicely describes the problem and the WHY of MCMC. It's hard to predict crazy probability distributions across a ton of features! The video also delves into the **intuition** behind it.
- If you like video lecture, MIT OpenCourseWare has two video lectures ([1](https://www.youtube.com/watch?v=IkbkEtOOC1Y)) ([2](https://www.youtube.com/watch?v=ZulMqrvP-Pk)) on MCMC. Note: These will be more technical videos!
- [Math-heavy Cornell lecture](http://www.cs.cornell.edu/selman/cs475/lectures/intro-mcmc-lukas.pdf)
- [Here's a more thorough deeper Python implementation](https://people.duke.edu/~ccc14/sta-663/MCMC.html) of MCMC sampling.
- [Notes on Markov Chains, including aperiodicity and irreducibility](http://www.math.chalmers.se/Stat/Grundutb/Chalmers/TMS081/oldpage/Lecture_notes/lecture3.pdf)
- [Accessible Medium article on Monte Carlo simulations](https://towardsdatascience.com/monte-carlo-without-the-math-90630344ff7b)
