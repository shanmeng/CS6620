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
1. Clone the repository.
```
bash

git clone https://github.com/shanmeng/CS6620.git
cd CS6620
```
2. Install dependencies.
```
bash

pip install -r requirements.txt
```
3. Run the code.
```
python

from packer import suggest_items

items = suggest_items(destination="Tokyo", duration=4, weather="cold")
print(items)
```
This command discovers and runs all unit tests in the project.

4. Run the test
```
bash
python -m unittest discover
```

5. CI/CD Pipeline
This project includes an automated GitHub Actions workflow, which runs tests automatically on:
- Push to `main` branch
- Pull requests
- Manual trigger via the HitHub "Actions" tab

Test results are viewable under the Actions tab on the repository page.


## Future Steps
This CI/CD Pipeline Part 1 project will be followed by 
- User preferences and saved profiles
- Real-time weather integration
- Visual packing checklist
