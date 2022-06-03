from wsgiref import headers
import pandas as pd

breakouts = ["acrobat", "sign", "documentcloud", "creativecloud", "products"]
file = input("what file you tryna split?\n")
column = str(input("what's the target column called?\n"))
df = pd.read_csv(file, low_memory=False)

# singular for now
def filter_csv(keyword, dataframe):
    filtered_df = dataframe[dataframe[column].str.contains(keyword)]
    return filtered_df

for cat in breakouts:
    kw = "/{}/".format(cat)
    tmp = filter_csv(kw, df)
    tmp.to_excel("{}_{}.xlsx".format(file[:-4],cat), index=False)
