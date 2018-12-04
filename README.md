# Pandas-Bin-Continuous

A [Pandas](https://pandas.pydata.org/) extension to allow you to encode binary features based on binned continuous values.

This module allows you to create seperate binary features based on whether your original feature lies within different bins. 

## Installation

```
git clone https://github.com/jtloong/pandas-bin-continous
cd pandas-bin-continuous
pip install .
```

## Usage

```
dataframe = pandas_bin_continuous.create_features(dataframe, bin_edges, feature_name)
```

Where bin_edges is a list of the different bounds of the bins. The bin_edges follows the same usage of bin lists as in [pandas.cut()](https://pandas.pydata.org/pandas-docs/version/0.23.4/generated/pandas.cut.html)

You can also view `example.ipynb` for a more full example of usage.