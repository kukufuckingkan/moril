from pandas import DataFrame

# Function to color the specified row green
def addColor(row, identifier,color):
    if identifier < 1:
        raise Exception("Invalid id. Id must be greater than or equal to 1.")
    if row.name == identifier - 1:  # Change this to color the specific row (adjusting for 0-based index)
        return [f'background-color: {color}'] * len(row)
    return [''] * len(row)

# Function to apply colors to the DataFrame for multiple rows
def colors(df: DataFrame, items: list, color: str):
    # Apply the coloring function for all items
    styled_df = df.style
    for item in items:
        styled_df = styled_df.apply(addColor, axis=1, identifier=item,color=color)
    return styled_df