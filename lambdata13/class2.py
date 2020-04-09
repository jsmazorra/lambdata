import pandas


def convert_names(my_df):
    """
    Creates a new column called "state_name" which has the corresponding state name.
​
    Params my_df (pandas.DataFrame) with with column called "abbrev" which has state abbrevs
​
    See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
    """
    df = my_df.copy()
    names_map = {
        "AL": "Alabama",
        "CT": "Conn",
        "CA": "Cali",
        "CO": "Colo",
        "DC": "District of Columbia"
    }
    print(type(df["abbrev"]))  # > <class 'pandas.core.series.Series'>
    df["state_name"] = df["abbrev"].map(names_map)
    return df


if __name__ == "__main__":

    df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    full_df = convert_names(df)
    print(full_df.head())

    df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
    full_df2 = convert_names(df2)
    print(full_df2.head())
