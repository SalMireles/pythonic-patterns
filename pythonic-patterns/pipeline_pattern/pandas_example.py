import pandas as pd


# function to find mean
def mean_age_by_group(dataframe: pd.DataFrame, column: str) -> pd.DataFrame:

    # groups the data by a column and
    # returns the mean age per group
    return dataframe.groupby(column).mean()


# function to convert to uppercase
def uppercase_column_name(dataframe: pd.DataFrame) -> pd.DataFrame:
    return dataframe.copy().rename(columns=lambda x: x.upper())


def main() -> None:

    # Create empty dataframe
    data_frame = pd.DataFrame()

    # Creating a simple dataframe
    data_frame["name"] = ["Reema", "Shyam", "Jai", "Nimisha", "Rohit", "Riya"]
    data_frame["gender"] = ["Female", "Male", "Male", "Female", "Male", "Female"]
    data_frame["age"] = [31, 32, 19, 23, 28, 33]

    pipeline = data_frame.pipe(mean_age_by_group, column="gender").pipe(
        uppercase_column_name
    )

    # View dataframe
    print(pipeline)


if __name__ == "__main__":
    main()
