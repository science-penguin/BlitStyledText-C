from os import system as blitstyledtext_system
blitstyledtext_executable_location = ""
def blitstyledtext_internal_blit(pixelmap):
    if(blitstyledtext_executable_location == ""):
        return 0
    else:
        input_str = blitstyledtext_executable_location
        for item0 in pixelmap:
            for item1 in pixelmap[item1]:
                input_str += f" {pixelmap[item0][item1]}"
        print(input_str)
def init(executable_location):
    blitstyledtext_executable_location = executable_location
    return blitstyledtext_internal_blit