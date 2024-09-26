import os

# Ask for ligand file
ligfile = input("Ligand_file:\t")

# Try to open the file
try:
    with open(ligfile, 'r') as fh:
        arr_file = fh.readlines()
except FileNotFoundError:
    print("Cannot open file")
    exit(1)

# Process each line in the ligand file
for i in range(len(arr_file)):
    print(arr_file[i].strip())  # Print each line (ligand file name)
    name = arr_file[i].strip().split('.')  # Split the name by dot (.)

# Run Vina for each ligand file
for i in range(len(arr_file)):
    ligand_file = arr_file[i].strip()  # Strip newline characters
    print(ligand_file)  # Print ligand file name
    # Execute Vina command
    vina_command = f"vina --config conf.txt --ligand {ligand_file}"
    os.system(vina_command)
