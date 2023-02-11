file = input("File name: ").strip().lower()

# file = 'cat.png'

if '.' in file:
    file = file.split(".")[1]

    match file:
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "gif":
            print("image/gif")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case "bin":
            print("application/octet-stream")

else:
    print("application/octet-stream")