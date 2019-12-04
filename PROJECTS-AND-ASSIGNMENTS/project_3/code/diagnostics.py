# Module containing personalized data cleaning and exploration tools.


class Sebastian:

    def __init__(self):
        self.null_dict = None

    def get_nulls(self, df):
        self.null_dict = {}
        for k, v in df.isnull().sum().iteritems():
            if v > 0:
                self.null_dict[k] = v
        return self.null_dict

    # Drops columns with 75% or more null values.
    def drop_null_cols(self, df, null_size=0.75, inplace=False):
        if self.null_dict is None:
            raise Exception(r'use get_nulls(df) first.')
        if inplace is False:
            df = df.copy()
        df_size = df.shape[0]
        for k, v in self.null_dict.items():
            if null_size <= 1:
                if v/df_size >= null_size:
                    del df[k]
            else:
                if v >= null_size:
                    del df[k]
        return df
