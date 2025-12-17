def http_status(status): # like switch case
    match status:
        case 200:
            return 1
        case 300:
            return 2
        case 400:
            return 3
        case _:
            return 0

print(http_status(200))