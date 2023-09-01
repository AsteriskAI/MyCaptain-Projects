extensions = {
    "py": "python",
    "txt": "text",
    "png": "PNG image",
    "jpg": "JPEG image" 
}

filename = input("Enter file name: ")

parts = filename.split(".")

if len(parts) > 1 :
    extent = parts[1].lower()

    filetype = extensions.get(extent)

    print(f"The file type of the '{filename}' is: '{filetype}'")

else:
    print("")