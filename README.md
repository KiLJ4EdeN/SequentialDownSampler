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
import numpy as np

# create a fake dataset.

X = np.random.rand(1000, 224, 224, 3)
Y = np.random.randint(0, 2, size=(1000))

# initiate the downsampler selecting the class to downsample and the ratio.
seqds = SequentialDownSampler(X, Y, dclass=1, ratio=3)
```


## Perform Downsampling on your Dataset.
```python

# perform downsampling.
X, Y = seqds.downsample()

print(X.shape)
print(Y.shape)
```
