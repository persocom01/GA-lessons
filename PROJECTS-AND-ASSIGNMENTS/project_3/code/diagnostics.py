# Module containing personalized data cleaning and exploration tools.


class Sebastian:

    def __init__(self, df=None, inplace=False):
        if df is not None:
            if not inplace:
                self.df = df.copy()
            else:
                self.df = df
        self.df_size = None
        self.null_dict = None

    def get_nulls(self):
        self.df_size = self.df.shape[0]
        self.null_dict = {}
        for k, v in self.df.isnull().sum().iteritems():
            self.null_dict[k] = v
        return self.null_dict

    # Drops columns with 75% or more null values.
    def drop_null_cols(self, null_size=0.75):
        if self.null_dict is None:
            raise Exception(r'use get_nulls(df) first.')
        for k, v in self.null_dict.items():
            if v/self.df_size >= null_size:
                del self.df[k]
        return self.df
