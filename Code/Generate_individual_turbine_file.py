import pandas as pd

# Load the Excel file
excel_file_path = "C:/Own use/Thesis/Wind_Turbine/Datasets/Scada_data/Wind Turbines Logs 2017.xlsx"

# Read the Excel file into a pandas DataFrame
df = pd.read_excel(excel_file_path)

# Function to filter turbine information and save a specific column or entire dataframe to CSV
def filter_turbine_and_save_csv(turbine_name, output_csv_path):
    # Filter the data by the specified turbine using the correct column name "Turbine_ID"
    filtered_df = df[df['Turbine_Identifier'] == turbine_name]
    
    if filtered_df.empty:
        print(f"No data found for {turbine_name}.")
        return
    
    # Save the entire filtered dataframe to CSV file
    filtered_df.to_csv(output_csv_path, index=False)
    print(f"CSV file for {turbine_name} saved successfully at '{output_csv_path}'")

# Example usage
turbine_name = input("Enter the turbine name: ")
output_csv = f"C:/Own use/Thesis/Wind_Turbine/Datasets/Scada_data/Wind Turbines Logs 2017/Wind Turbines Logs 2017({turbine_name}).csv"

# Call the function to filter turbine data and save it to CSV
filter_turbine_and_save_csv(turbine_name, output_csv)
