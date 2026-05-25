#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      GP80
#
# Created:     27/10/2025
# Copyright:   (c) GP80 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import pandas as pd

df = pd.read_csv("ai_eu.csv")

geolocator = Nominatim(user_agent="my_geocoder", timeout=10)  # ← increase to 10s
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)

df["location"] = df["Country"].apply(geocode)

# Extract latitude and longitude into separate columns
df["latitude"] = df["location"].apply(lambda loc: loc.latitude if loc else None)
df["longitude"] = df["location"].apply(lambda loc: loc.longitude if loc else None)

# Optionally inspect
print(df[["Country", "latitude", "longitude"]])
