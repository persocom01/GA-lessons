# Module containing personalized data cleaning and exploration tools.

# CZ deals with word processing.
# She pastes 1 yen stickers on things she likes.


class CZ:

    def __init__(self):
        # Contractions dict.
        self.contractions = {
            "n't": " not",
            "'s": " is",
            "'m": " am",
            "'ll": " will",
            "'ve": " have",
            "'re": " are"
        }

    # To tokenize is to split the sentence into words.
    def re_tokenize(self, sentence):
        from nltk.tokenize import RegexpTokenizer
        retoken = RegexpTokenizer(r'\w+')
        sentence = sentence.lower()
        words = retoken.tokenize(sentence)
        return words

    # Lemmatizing eliminates things like the s from plurals like apples.
    def lemmatize_sentence(self, sentence):
        from nltk.stem import WordNetLemmatizer
        wnlem = WordNetLemmatizer()
        words = self.re_tokenize(sentence)
        words = [wnlem.lemmatize(word) for word in words]
        # Returns sentence instead of individual words.
        return ' '.join(words)

    # Stemming is a more drastic approach than lemmatizing. It truncates words
    # to get to the root word.
    def stem_sentence(self, sentence):
        from nltk.stem.porter import PorterStemmer
        p_stem = PorterStemmer()
        words = self.re_tokenize(sentence)
        words = [p_stem.stem(word) for word in words]
        # Returns sentence instead of individual words.
        return ' '.join(words)

    def text_cleaner(self, text, *args, inplace=False):
        import re
        if inplace is False:
            text = text.copy()
        for i in range(len(text)):
            for arg in args:
                if isinstance(arg, dict):
                    for k, v in arg.items():
                        text[i] = re.sub(k, v, text[i])
                elif callable(arg):
                    text[i] = arg(text[i])
                else:
                    text[i] = re.sub(arg, r' ', text[i])
        return text

# Sebastian deals with data cleaning.


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
