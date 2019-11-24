import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import sklearn.preprocessing as skpp
import sklearn.model_selection as skms
import sklearn.linear_model as sklm
import sklearn.metrics as skm


def ordinal_scale(df, mapping=None, start_num=0):
    '''
    A convenience mapping function that accepts a DataFrame and returns it with
    each column defined as keys in the mapping dictionary mapped to its values.
    '''
    if mapping:
        cols = mapping.keys()
        for col in cols:
            df[col] = df[col].map(
                {k: i+start_num for i, k in enumerate(mapping[col])})
            if df[col].isnull().sum() > 0:
                print(
                    f'WARNING: not all values in column "{col}" were mapped.')
    else:
        cols = df.columns
        ord = skpp.OrdinalEncoder()
        df[cols] = ord.fit_transform(df[cols])
    return df


def vif_feature_select(df, max_score=5.0, n_features=-1, inplace=False, drop_list=False, drops=None):
    '''
    Takes a DataFrame and returns it after recursively eliminating columns
    with the highest VIF scores until either the remainder have a VIF score
    of less than max_score, or there are n_features left.
    '''
    if not inplace:
        df = df.copy()
    if not drops:
        drops = []
    features = df.columns
    vifs = np.linalg.inv(df.corr().values).diagonal()
    max_vif_index = np.argmax(vifs)
    if n_features < 0 and vifs[max_vif_index] >= max_score:
        drops.append(features[max_vif_index])
        del df[features[max_vif_index]]
        return vif_feature_select(df, max_score, n_features, inplace, drop_list, drops)
    elif n_features >= 0 and len(features) > n_features:
        drops.append(features[max_vif_index])
        del df[features[max_vif_index]]
        return vif_feature_select(df, max_score, n_features, inplace, drop_list, drops)
    else:
        if drop_list:
            print('returning list of dropped features.')
            return drops
        else:
            return df


def subplot_dist(df, kind='dist', cols=None, titles=None, xlabels=None, ylabels=None, meanline=False, medianline=False, **kwargs):
    # Accepts all columns if they can be converted to numbers if cols argument
    # is not given.
    if not cols:
        cols = []
        if kind == 'count':
            cols = [x for x in df.select_dtypes(include='object').columns]
        else:
            for col in df.columns:
                try:
                    df[col] = pd.to_numeric(df[col])
                    cols.append(col)
                except ValueError:
                    pass

    # Sets number of figure rows based on number of DataFrame columns.
    if len(cols) > 4:
        ncols = 3
        nrows = int(np.ceil(len(cols)/3))
    else:
        ncols = 2
        nrows = int(np.ceil(len(cols)/2))
    # Sets figure size based on number of figure rows.
    fig, ax = plt.subplots(nrows=nrows, ncols=ncols, figsize=(16, 5*nrows))
    # Makes the list of lists flat.
    ax = ax.ravel()

    for i, col in enumerate(cols):
        is_list = isinstance(col, (list, tuple))
        if is_list and kind != 'box':
            print('distplot does not plot multiple series in one graph.')
            continue
        if kind == 'dist':
            sb.distplot(df[col], ax=ax[i], **kwargs)
            if meanline:
                ax[i].axvline(np.mean(df[col]), color='r',
                              linestyle='-', linewidth=1)
            if medianline:
                ax[i].axvline(np.median(df[col]), color='purple',
                              linestyle='--', linewidth=1)
        # Boxplotting option.
        elif kind == 'box':
            sb.boxplot(data=df[col], ax=ax[i], **kwargs)
            if not is_list and meanline:
                ax[i].axhline(np.mean(df[col]), color='r',
                              linestyle='-', linewidth=1)
        # Countplot option for nominal variables.
        elif kind == 'count':
            sb.countplot(x=col, data=df, ax=ax[i], **kwargs)

        if titles:
            ax[i].set_title(titles[i])
        if xlabels:
            ax[i].set_xlabel(xlabels[i])
        if ylabels:
            ax[i].set_ylabel(ylabels[i])


def adj_r2(X, y, y_hat):
    return 1 - (1-skm.r2_score(y, y_hat))*(len(y)-1)/(len(y)-X.shape[1]-1)


__all__ = ['np', 'pd', 'sb', 'plt', 'skpp', 'skms',
           'sklm', 'skm', 'ordinal_scale', 'vif_feature_select', 'subplot_dist', 'adj_r2']
