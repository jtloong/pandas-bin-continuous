# Pandas-Bin-Continuous

A [Pandas](https://pandas.pydata.org/) extension to allow you to encode binary features based on binned continuous values.

Sometimes keeping continous variables as floating point values or integers may actually throw off your model weights. It may be more useful to encode your continuous variables as seperate binary features decided by their value in different bins, which this extension should address. 

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

## Notes

Realized after I made this, that sklearn has a [binarizer class](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.Binarizer.html) in their preprocessing module. However, I think this is slightly more useful for features with a wide range of continuous values that you need to seperate into many bins. 