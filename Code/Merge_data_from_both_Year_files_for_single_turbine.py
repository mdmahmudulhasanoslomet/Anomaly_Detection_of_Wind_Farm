import pandas as pd

def merge_csv_files(file_2016, file_2017, output_file):
    # Load datasets from given file paths
    df_2016 = pd.read_csv(file_2016)
    df_2017 = pd.read_csv(file_2017)
    
    # Merge datasets
    merged_df = pd.concat([df_2016, df_2017], ignore_index=True)
    
    # Save merged dataset to the specified output file
    merged_df.to_csv(output_file, index=False)
    
    print(f"Merged dataset saved as {output_file}")

# Example usage with correct file paths
file_2016 = "C:/Own use/Thesis/Wind_Turbine/Datasets/Scada_Data(Wind_Turbine)/Wind-Turbine-SCADA-signals-2016/Without_Grd_Column/Latest/Wind-Turbine-SCADA-signals-2016_(T11)_TimeSequence.csv"
file_2017 = "C:/Own use/Thesis/Wind_Turbine/Datasets/Scada_Data(Wind_Turbine)/Wind-Turbine-SCADA-signals-2016/Without_Grd_Column/Latest/Wind-Turbine-SCADA-signals-2017_(T11)_TimeSequence.csv"
output_file = "C:/Own use/Thesis/Wind_Turbine/Datasets/Scada_Data(Wind_Turbine)/Wind-Turbine-SCADA-signals-2016/Without_Grd_Column/Latest/Wind-Turbine-SCADA-signals(T11)_TimeSequence.csv"

merge_csv_files(file_2016, file_2017, output_file)


