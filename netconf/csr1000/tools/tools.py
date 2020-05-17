def try_print(option, option_insert):
    try:
        print(f"{option}: {option_insert}")
    except:
        print(f"{option}: ")
        pass