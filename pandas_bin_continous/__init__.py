import pandas as pd 

def create_features(df, bin_edges, feature_name):
	bin_series = pd.cut(df['feature_name'], bins=bin_edges)

	for edge in bin_edges:
		name = feature_name + str(edge) + '_to_' _ str(edge + 1)
		df[name] = bin_series.apply(lambda i: 1 if i.left == edge else 0)

	return df