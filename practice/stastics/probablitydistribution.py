# Probability distribution:
# Describes possible outcomes and their probabilities.
#
# Discrete → countable outcomes
# Continuous → values within a range
#
# Normal distribution:
# Bell-shaped distribution described by mean and standard deviation.
# 68% → within 1 SD
# 95% → within 2 SD
# 99.7% → within 3 SD

# Normal distribution:
# - Bell-shaped
# - Symmetric
# - Mean ≈ Median ≈ Mode
# - Unimodal (one peak)
# - Continuous distribution
# - 68-95-99.7 rule applies
#
# 1 SD → 68%
# 2 SD → 95%
# 3 SD → 99.7%

# Z-score:
# Measures how many standard deviations a value is
# away from the mean.
#
# z = (x - mean) / standard_deviation
#
# z = 0  → at mean
# z > 0  → above mean
# z < 0  → below mean

# Central Limit Theorem (CLT):
# Taking many sufficiently large random samples from a population
# and calculating their means produces a sampling distribution
# that tends to become approximately normal.
#
# The original population does not need to be normally distributed.

# Central Limit Theorem:
# Distribution of sample means tends to become approximately normal
# when the sample size is sufficiently large.
#
# Mean of sample means ≈ population mean
# Standard error = population SD / sqrt(sample size)

# Standard Error (SE):
# Measures the variability of a sample statistic,
# especially the sample mean, across repeated samples.
#
# SE = population SD / sqrt(sample size)
#
# Larger sample size → smaller SE → more precise estimate
#
# Standard Deviation → spread of individual values
# Standard Error     → spread/uncertainty of sample mean

# Confidence Interval:
# A range used to estimate a population parameter from a sample.
#
# Common 95% CI (when using a normal critical value):
# CI = sample_mean ± 1.96 × SE
#
# Repeated 95% CI procedures capture the true parameter
# approximately 95% of the time.

# Hypothesis Testing:
# Used to determine whether sample data provides
# enough evidence against a null hypothesis.
#
# H0 → Null hypothesis (default assumption)
# Ha → Alternative hypothesis
#
# Common significance level: α = 0.05
#
# p-value < α  → Reject H0
# p-value >= α → Fail to reject H0

# Z-test:
# Population standard deviation is known.
# z = (sample_mean - hypothesized_mean) / (population_SD / sqrt(n))
#
# T-test:
# Population standard deviation is unknown.
# Use sample standard deviation.
# t = (sample_mean - hypothesized_mean) / (sample_SD / sqrt(n))
#
# One-sample t-test:
# degrees of freedom = n - 1

# Hypothesis test tails:
# Ha: μ < value → Left-tailed
# Ha: μ > value → Right-tailed
# Ha: μ != value → Two-tailed

# Chi-Square Test of Independence:
# Used to test whether two categorical variables are associated.
#
# H0 → Variables are independent
# Ha → Variables are associated
#
# Compares observed frequencies with expected frequencies.
#
# p < 0.05 → Reject H0


# ANOVA (Analysis of Variance):
# Used to compare means across 3 or more groups.
#
# H0 → All group means are equal
# Ha → At least one group mean is different
#
# ANOVA uses an F-statistic and p-value.
# p < 0.05 → Reject H0
#
# 2 groups → commonly t-test
# 3+ groups → commonly ANOVA

# ANOVA:
# Compares means across 3 or more groups.
# H0 → all group means are equal
# Ha → at least one mean differs
# Significant ANOVA → use post-hoc tests to find where differences are.