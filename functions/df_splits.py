def df_splits(df):
    """
    Parameter df is the Data Frame name
    Function creates train/validate/test split. After it requests a target,
     and creates X and y features/vectors
    """
    
    from sklearn.model_selection import train_test_split

    # train and test (test_size=0.20)
    train, test = train_test_split(df, test_size=0.2, random_state=42)

    # train and val (test_size=0.20)
    train, val = train_test_split(train, test_size=0.2, random_state=42)

    # Split the dataframes into their respective X (feature) matrices and y
    # (target) vector

    return train, test, val
