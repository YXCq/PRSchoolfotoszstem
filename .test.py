def bulk(arr):
    x = 0
    y = 0
    for i in arr.values():
        x =+ i[0]
        y = y + i[0]*4 + i[1]*4 + i[2]*9
    return x, y


print(bulk({
  "chicken": [20, 5, 10],  # per 100g chicken has 20g of protein, 5 grams of carbohydrates and 10 grams of fat.
  "eggs": [10, 5, 15],    # protein:10g , carbs:5g , fats: 15g
  "salmon": [27, 0, 10],
  "beans": [8, 25, 0],
  "bananas": [1, 23, 0],
}))
