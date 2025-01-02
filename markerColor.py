def getMarkerColor(capacity: int):
    if capacity < 70000:
        return "red"
    elif capacity < 80000:
        return "beige"
    else:
        return "darkred"
