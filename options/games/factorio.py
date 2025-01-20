import os

# Returns None if the variable doesn't exist
appdata_path = os.getenv("APPDATA")


# If exists
if appdata_path:
    # Construct the path to the Factorio saves folder
    factorio_saves = os.path.join(appdata_path, "Factorio", "saves")
    files = [
        f
        for f in os.listdir(factorio_saves)
        if os.path.isfile(os.path.join(factorio_saves, f))
    ]
    if files:
        # Sort files by creation time (newest first)
        files_sorted = sorted(
            files,
            key=lambda f: os.path.getctime(os.path.join(factorio_saves, f)),
            reverse=True,
        )
        print(files_sorted)
    else:
        print("No files found.")
    print(files_sorted[0])

# If doesn't exists
else:
    print("Windows APPDATA environment variable is not set. Not able to find Save!")
