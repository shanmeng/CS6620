Name: Shan Meng
Date: May 29, 2025
Class: CS6620, Summer
Notes: CI/CD Pipeline Part 1



# PackMyBag – Travel Packing Assistant
This is a Python module for suggesting what to pack based on the user's:
- Destination
- Trip duration
- Weather conditions

It’s a core component of a future travel assistant app.


## What Categories Included
- Hygiene
- Clothes, automatically adjusted by duration and weather
- Electronics
- Extras, e.g. swimwear, baby items, pet items...


## How to Use
```
python

from packer import suggest_items

items = suggest_items(destination="Tokyo", duration=4, weather="cold")
print(items)
```
This command discovers and runs all unit tests in the project.


## Run Tests
```
bash
python -m unittest discover
```

## CI/CD Pipeline
This project includes an automated GitHub Actions workflow, which runs tests automatically on:
- Push to `main` branch
- Pull requests
- Manual trigger via the HitHub "Actions" tab

Test results are viewable under the Actions tab on the repository page.


## Future Steps
This CI/CD Pipeline Part 1 project will be followed with 
- User preferences and saved profiles
- Real-time weather integration
- Visual packing checklist
