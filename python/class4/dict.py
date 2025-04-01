# Dictionaries:

thisDict = {
    "brand": "Honda",
    "model": "city",
    "year": 2004,
    "isStock": True,
    "colors": ["red", "white", "black"]
}

thisDict["model"] = "WR-V"

print(thisDict)
print(thisDict["brand"])
print(len(thisDict))
print(type(thisDict))

thisDict.update({"year": 2025})
print(thisDict)

thisDict.popitem()
thisDict.clear()

print(thisDict)
