def convert_distance(value: float,direction: str = "miles_to_km") -> str:
    #  конвертує відстань між милями і км. і повертає результат з одиницями виміру
    #  value число для конвертації
    #   direction -  "miles_to_km"   або   " km_to_miles"
    #  return   -  повертає результат
    if direction == "miles_to_km":
        result = value * 1.60934
        return f"{value} миль = {result:.4f} km "
    elif direction == "km_to_miles":
        result = value * 0.621371
        return f"{value} km = {result:.4f} миль "
    else:
        raise ValueError("Напрямок повинен бути 'miles_to_km'  або  'km_to_miles'")

def convert_fut(value:float,direction: str = "fut_to_metr"):

    if direction == "fut_to_metr":
        result = value * 0.3048
        return f"{value} fut = {result:4f} metr"
    elif direction == "metr_to_fut":
        result = value / 0.3048
        return f"{value} metr = {result:.4f} fut"
    else:
        raise ValueError("Напрямок 'fut_yo_metr ' або 'metr_to_fut' " )

print(convert_distance(5,"miles_to_km"))
print(convert_distance(10,"km_to_miles"))

print(convert_fut(10,"fut_to_metr"))
print(convert_fut(10,"metr_to_fut"))