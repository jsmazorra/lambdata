# my_lambdata/class3.py
​
import pandas
from datetime import datetime
# GOAL: refactor from a functional approach to OOP approach
# could make a State class
# could create a class for Abbreviations
# could have the data frame a attribute of the class instance,
# ... have the existing function a method of the class.
​
​
class DataTransformer():
    def __init__(self, my_df):
        """
        Params my_df (pandas.DataFrame) with with column called "abbrev" which has state abbrevs
        """
        self.df = my_df.copy()
​
    def another_example(self):
        print("WE'RE DOING ANOTHER THING")
        self.convert_names()
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
        #print(type(self.df["abbrev"])) #> <class 'pandas.core.series.Series'>
        self.df["state_name"] = self.df["abbrev"].map(names_map)
        #return self.df
​
    @staticmethod
    def progress_message():
        print(datetime.now())
​
    def do_stuff(self, my_message):
        print(self.df.columns, my_message)
​
if __name__ == "__main__":
​
    df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    transformer = DataTransformer(df)
    print(transformer.df.head())
    #transformer.convert_names()
    transformer.another_example()
    print(transformer.df.head())
    #transformer.do_stuff("HELLO WEDNESDAY!!!")
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
Collapse



12:53
reconvene at :00

Tyler Sheppard:lambda-shield:  13:00
@channel, come on back!

Harrison Kang  13:05
class DataTransformer( pd.DataFrame)
:+1:
1


Joseph Wilson:darksouls_praise_dark:  13:10
instead of using self.df use self
:this:
3
:+1:
1


Mike Rossetti  13:14
inheritance approach
​
# my_lambdata/class3.py
​
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


    # df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
    # full_df = convert_names(df)
    # print(full_df.head())

    # df2 = pandas.DataFrame({"abbrev": ["GA", "NY", "CA", "CO"]})
    # full_df2 = convert_names(df2)
    # print(full_df2.head())


# my_lambdata/class3.py
​
# GOAL: refactor from a functional approach to OOP approach
# could make a State class
# could create a class for Abbreviations
# could have the data frame a attribute of the class instance,
# ... have the existing function a method of the class.
​
​


class DataTransformer():
    def __init__(self, my_df):
        """
        Params my_df (pandas.DataFrame) with with column called "abbrev" which has state abbrevs
        """
        self.df = my_df.copy()


​


def another_example(self):
    print("WE'RE DOING ANOTHER THING")
    self.convert_names()


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
    #print(type(self.df["abbrev"])) #> <class 'pandas.core.series.Series'>
    self.df["state_name"] = self.df["abbrev"].map(names_map)

    #return self.df
​


@staticmethod
def progress_message():
    print(datetime.now())


​


def do_stuff(self, my_message):
    print(self.df.columns, my_message)


​
if __name__ == "__main__":
​
df = pandas.DataFrame({"abbrev": ["CT", "CO", "CA", "TX"]})
transformer = DataTransformer(df)
print(transformer.df.head())
#transformer.convert_names()
transformer.another_example()
print(transformer.df.head())
#transformer.do_stuff("HELLO WEDNESDAY!!!")
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
Collapse

12: 53
reconvene at: 00

Tyler Sheppard: lambda-shield:  13: 00


@channel, come on back!
Harrison Kang  13: 05


class DataTransformer(pd.DataFrame)


: +1:
1


Joseph Wilson: darksouls_praise_dark:  13: 10
instead of using self.df use self
: this:
3
: +1:
1


Mike Rossetti  13: 14
inheritance approach
​
# my_lambdata/class3.py
​
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
