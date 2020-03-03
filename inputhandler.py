def prompt_input():
    filteroption = input("Input filter option (empty will default to none): ")
    if filteroption == "Address Range":
        try:
            key = float(input("Input distance(km) from reference: "))
            lat = float(input("Input latitude of reference point: "))
            long = float(input("Input longitude of reference point: "))
            return [filteroption, key, lat, long]
        except ValueError:
            print("Ensure the data is the correct type")
    elif filteroption != "":
        key = input("Input search term: ")
        return [filteroption, key]
    else:
        return [None, None]
