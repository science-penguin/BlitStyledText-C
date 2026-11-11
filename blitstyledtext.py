from os import system as blitstyledtext_system
blitstyledtext_executable_location = ""
def blitstyledtext_internal_blit(pixelmap):
    global blitstyledtext_executable_location
    if blitstyledtext_executable_location == "":
        return 1
    else:
        input_str = f"{blitstyledtext_executable_location} {str(len(pixelmap))} {str(len(pixelmap[0]))}"
        for item0 in pixelmap:
            for item1 in item0:
                for item2 in item1:
                    input_str += f' "{item2}"'
        blitstyledtext_system(input_str)
        return 0
def init(executable_location):
    global blitstyledtext_executable_location
    blitstyledtext_executable_location = executable_location
    return blitstyledtext_internal_blit