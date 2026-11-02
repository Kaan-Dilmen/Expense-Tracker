# Report Functions
def category_totals(df):
    return df.groupby("category")["amount"].sum()


def monthly_totals(df):
    return df.groupby(df["date"].dt.to_period("M"))["amount"].sum()


def biggest_expense(df):
    return df.loc[df["amount"].idxmax()]
