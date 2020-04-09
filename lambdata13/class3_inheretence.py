# my_lambdata/class3.py
import pandas
​
# GOAL: inherit from DataFrame and create our own custom DF class
​


class CustomFrame(pandas.DataFrame):
    """
    Needs column called "abbrev" which has state abbrevs
    """


​


def convert_names(self):
    """
        Creates a new column called "state_name" which has the corresponding state name.
        See: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.map.html
        """
    names_map = {
        "AL": "Alabama",
        "CT": "Conn",
        "CA": "Cali",
        "CO": "Colo",
        "DC": "District of Columbia"
    }
    self["state_name"] = self["abbrev"].map(names_map)


​
if __name__ == "__main__":
​
#df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
custom_df = CustomFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
print(custom_df.head())
custom_df.convert_names()
print(custom_df.head())
​
​
​
​
​
​
​
#transformer = DataTransformer(df)
#print(transformer.df.head())
##transformer.convert_names()
#transformer.another_example()
#print(transformer.df.head())
##transformer.do_stuff("HELLO WEDNESDAY!!!")
​
​
exit()
​
print("--------------")
df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
transformer2 = DataTransformer(df2)
print(transformer2.df.head())
transformer2.convert_names()
print(transformer2.df.head())
​
#df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
#print(type(df)) #> pandas.DataFrame
#full_df = convert_names(df)
#print(full_df.head())
#
#df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
#full_df2 = convert_names(df2)
#print(full_df2.head())
#
#df = pandas.DataFrame({"a": [1,2,3]})
