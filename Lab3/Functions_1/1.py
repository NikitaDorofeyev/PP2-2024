def grams_to_ounces_converter(grams):
    ounces = grams / 28.3495231
    return ounces

grams = float(input())

print(grams, "grams equal to", grams_to_ounces_converter(grams), "ounces")