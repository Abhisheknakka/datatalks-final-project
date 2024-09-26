import os

# Base folder path
BASE_FOLDER = 'C:/Users/karth/Documents/datatalks-final-project/'

# Derived folder paths
dataset_folder = os.path.join(BASE_FOLDER, 'dataset/')
main_folder = os.path.join(BASE_FOLDER, 'menu_assistant/')
notebook_folder = os.path.join(BASE_FOLDER, 'notebooks/')
# Add other directories if necessary

# Example of how to print or check paths
if name == "main":
    print("Base folder:", BASE_FOLDER)
    print("Input data folder:", dataset_folder)
    print("main  folder:", main_folder)
    print("notebooks data folder:",notebook_folder)