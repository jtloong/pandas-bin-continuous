import pandas as pd 

def create_features(df, bin_edges, feature_name):
	"""Returns your Pandas dataframe with new binary features based on binned values of your selected feature.
    Args:
        df: A Pandas Dataframe that includes your continuous feature
        bin_edges: A list of number by which to create the bounds of the bins
        feature_name: A string that is the name of the feature we are binning
    Returns:
        df: A Pandas DataFrame that includes your original and your new binary encoded features
    """
	bin_series = pd.cut(df[feature_name], bins=bin_edges)

	for index, edge in enumerate(bin_edges):
		name = feature_name + '_' + str(edge) + '_to_' + str(bin_edges[index + 1])
		df[name] = bin_series.apply(lambda i: 1 if i.left == edge else 0)

	return df