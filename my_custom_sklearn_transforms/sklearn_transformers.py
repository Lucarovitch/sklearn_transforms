from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')


class AdjustMeanSubject(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        data = X.copy()
        data['NOTA_GO'] = data.apply(
            lambda row: ((row['NOTA_MF'] + row['NOTA_EM'] + row['NOTA_DE']) / 3) if np.isnan(row['NOTA_GO']) else row[
                'NOTA_GO'], axis=1
        )
        for num, name in enumerate(df_data_1['NOTA_GO'], start=0):
            data_new.append(1 if df_data_1['NOTA_GO'][num] != 0 else 0)
        df_data_1['APROVADO_GO'] = data_new

        data_new = []

        for num, name in enumerate(df_data_1['NOTA_MF'], start=0):
            data_new.append(1 if (df_data_1['NOTA_MF'][num] != 0) else 0)
        df_data_1['APROVADO_MF'] = data_new

        data_new = []

        for num, name in enumerate(df_data_1['NOTA_EM'], start=0):
            data_new.append(1 if (df_data_1['NOTA_EM'][num] != 0) else 0)
        df_data_1['APROVADO_EM'] = data_new

        data_new = []

        for num, name in enumerate(df_data_1['NOTA_DE'], start=0):
            data_new.append(1 if (df_data_1['NOTA_DE'][num] != 0) else 0)
        df_data_1['APROVADO_DE'] = data_new

        return data


class FeatureEngineering(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        df = X.copy()
        df['REPROVACOES_H'] = df['REPROVACOES_DE'] + df['REPROVACOES_EM']
        df['REPROVACOES_E'] = df['REPROVACOES_MF'] + df['REPROVACOES_GO']
        df['MEDIA_T'] = (df['NOTA_MF'] + df['NOTA_GO'] + df['NOTA_DE'] + df['NOTA_EM']) / 4

        return df
