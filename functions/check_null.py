def check_null(df):
    """
    Parameter df is the Data Frame name
    Function will list a sum of all null arranged by columns in a Data Frame
    """
    return df.isnull().sum()
