# WeatherWardobe
# Inspiration
Ever feel like choosing an outfit was too frustrating or stressful? Us too! That's why we wanted to build a product that catered to everyday needs in an inexpensive way!

# What it does
WeatherWardrobe scans all your clothing, identifies each article's traits, and organizes them in a digital wardrobe. Based on weather forecast and clothing style, WeatherWardrobe will pick the perfect outfit for you at the mere press of a button!

# How we built it
Using Google's Cloud and Vision APIs, the Raspberry Pi running the program can identify the article of clothing in realtime (for example, the program can differentiate between a pair of shorts and a pair of jeans). Google's APIs accurately predict clothing while they are on you and helps conduct analyses on the best combinations of clothing for catered styles. Information is stored and gathered through Google Cloud-based services that make management of data easy. Once WeatherWardrobe has cataloged all of your clothing, it collects weather information from the OpenWeatherMap API. Using our algorithm, WeatherWardobe takes the combination of all this information to surmise the best outfit to look stylish and to be prepared for the weather. Never let a rainy day or heatwave stress you again.

# Challenges we ran into
Using the Vision API to recognize objects in realtime and develop an accurate algorithm were the biggest challenges. This was also our first venture with Google Cloud servers and we are happy to say we utilized it greatly for the final project, besides the initial steep learning curve.

# Accomplishments that we're proud of
Learning Google Cloud and Google Vision APIs. We also had a great time working with Raspberry Pi 4 again.

# What we learned
Optimization of cloud-based computing, analytical skills of complex weather data, JSON, and advanced OpenCV.

# What's next for WeatherWardrobe
Implementation in smart home ecosystems.

# Built With
cv2
dlib
google-cloud
googlevision
numpy
opencv
openweathermap
scipy
