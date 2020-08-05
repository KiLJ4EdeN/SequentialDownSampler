# SequentialDownSampler
Sequential down sampling implementation for imbalanced data classification.

[![License](https://img.shields.io/github/license/KiLJ4EdeN/SequentialDownSampler)](https://img.shields.io/github/license/KiLJ4EdeN/SequentialDownSampler) [![Version](https://img.shields.io/github/v/tag/KiLJ4EdeN/SequentialDownSampler)](https://img.shields.io/github/v/tag/KiLJ4EdeN/SequentialDownSampler) [![Code size](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/SequentialDownSampler)](https://img.shields.io/github/languages/code-size/KiLJ4EdeN/SequentialDownSampler) [![Repo size](https://img.shields.io/github/repo-size/KiLJ4EdeN/SequentialDownSampler)](https://img.shields.io/github/repo-size/KiLJ4EdeN/SequentialDownSampler) [![Issue open](https://img.shields.io/github/issues/KiLJ4EdeN/SequentialDownSampler)](https://img.shields.io/github/issues/KiLJ4EdeN/SequentialDownSampler)
![Issue closed](https://img.shields.io/github/issues-closed/KiLJ4EdeN/SequentialDownSampler)


# Usage:
## Install Dependencies w pip:

1- numpy


## Import the SequentialDownSampler Class and Create an Instance with Desired Settings.
```python
from SequentialDownSampler import SequentialDownSampler
seqds = SequentialDownSampler(X, Y, dclass=1, ratio=3)
```


## Perform Downsampling on your Dataset.
```python
X, Y = seqds.downsample()

print(X.shape)
print(Y.shape)
```
