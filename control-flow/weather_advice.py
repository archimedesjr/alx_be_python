weather_today = input("What's the weather like today? (sunny/rainy/cold): ").lower()
if weather_today == "sunny":
  recommendation = "Wear a t-shirt and sunglasses."
elif weather_today == "rainy":
  recommendation = "Don't forget your umbrella and a raincoat."
elif weather_today == "cold":
  recommendation = "Make sure to wear a warm coat and a scarf."
else:
  recommendation = "Sorry, I don't have recommendations for this weather."
print(recommendation)