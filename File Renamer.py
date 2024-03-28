import os
import shutil

# Global variables for directory and destination
directory = ""
destination = ""
config_file = "config.txt"
extensions = ['.jpg', '.jpeg', '.png', '.webp', '.gif']

# Function to load configuration
def load_config():
    global directory, destination
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            lines = f.readlines()
            directory = lines[0].strip()
            destination = lines[1].strip()

# Function to save configuration
def save_config():
    with open(config_file, "w") as f:
        f.write(directory + "\n")
        f.write(destination + "\n")

# Function to rename files with specified name and sequential numbering
def rename_files(new_name):
    global directory, destination,extensions 
    
    # Change directory
    os.chdir(directory)
    
    # Get a list of files in the directory
    files = os.listdir()
    
    # Initialize a counter for numbering files
    count = 1
    
    # Iterate through the files and rename them
    for file in files:
        # Split the filename and its extension
        filename, extension = os.path.splitext(file)
        
        # Check if the file extension is in the list of supported image extensions
        if extension.lower() in extensions:
            # Rename the file with specified name and sequential numbering
            new_filename = f"{new_name}_{count:03d}{extension}"  # Format count with leading zeros
            os.rename(file, new_filename)
            
            # Increment the counter
            count += 1
    
    # Move the renamed files to the destination directory
    for file in os.listdir(directory):
        if file.startswith(new_name):
            shutil.move(os.path.join(directory, file), destination)

# Function to change directory
def change_directory():
    global directory
    
    new_directory = input("Enter the new directory path: ")
    if os.path.isdir(new_directory):
        directory = new_directory
        save_config()
        print(f"Directory changed to {directory}")
    else:
        print("Invalid directory path. Please try again.")

# Function to change destination
def change_destination():
    global destination
    
    new_destination = input("Enter the new destination path: ")
    if os.path.isdir(new_destination):
        destination = new_destination
        save_config()
        print(f"Destination changed to {destination}")
    else:
        print("Invalid destination path. Please try again.")

# Function to change filename
def change_filename():
    global directory, destination, extensions
    
    if not directory:
        print("Please set a directory first.")
        return
    
    if not destination:
        print("Please set a destination first.")
        return
    
    # Check for picture file types
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and any(f.endswith(ext) for ext in extensions)]
    if not files:
        print("There are no files in the directory to rename.")
        return
    
    # Prompt the user to enter the desired name for the files
    new_name = input("Enter the desired name for the files: ")
    
    # Call the function to rename files and move them to the destination
    try:
        rename_files(new_name)
        print("Files renamed and moved successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to display menu and get user input
def menu():
    print("=== File Renaming Script ===")
    print("1. Rename and Move Files")
    print("2. Change Directory")
    print("3. Change Destination")
    print("4. Exit")
    choice = input("Enter your choice: ")
    print()
    return choice

# Main function
def main():
    global directory, destination

    load_config()
    
    while True:
        choice = menu()
        
        if choice == '1':
            change_filename()
        
        elif choice == '2':
            change_directory()
        
        elif choice == '3':
            change_destination()
        
        elif choice == '4':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
        print()

if __name__ == "__main__":
    main()
