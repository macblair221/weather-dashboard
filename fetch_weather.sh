#!/bin/bash

# Set coordinates (Eugene, OR)
LAT=44.0521
LON=123.0897

# Today's date for filename
DATE=$(date +%Y-%m-%d)
OUTFILE="weather_data/weather_$DATE.json"

# Fetch weather data using curl
curl -s "https://api.open-meteo.com/v1/forecast?latitude=$LAT&longitude=$LON&hourly=temperature_2m,relative_humidity_2m&timezone=auto" -o "$OUTFILE"

echo "Weather data saved to $OUTFILE"
