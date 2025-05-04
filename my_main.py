import os
from dotenv import load_dotenv
import requests
from datetime import datetime

load_dotenv()

APP_ID  = os.getenv("APP_ID")
API_KEY = os.getenv("API_KEY")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_params = {
    "query" : input("Tell me which exercises you did: ")
}

headers = {
    "x-app-id" : APP_ID,
    "x-app-key" : API_KEY
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
response_data = response.json()["exercises"]

sheety_endpoint = "https://api.sheety.co/cc92f9f277a3d6e4ad5f0c900edfbf73/bảnSaoCủaMyWorkouts/workouts"

sheety_header = {"Authorization" : "Bearer asgdsajkhfgdsajkhfgsk"}

def add_row(date,time,exercise_sub, duration, calories):
    request_params = {
        "workout" : {
            "date" : date,
            "time": time,
            "exercise": exercise_sub.capitalize(),
            "duration": duration,
            "calories": calories
        }
    }
    sheety_response = requests.post(url=sheety_endpoint,json=request_params, headers=sheety_header)
    print(sheety_response.status_code)

for exercise in response_data:
    current_date = datetime.now().strftime("%d/%m/%Y")
    current_time = datetime.now().strftime("%H:%M:%S")
    exercise_subject =  exercise["name"]
    duration = exercise["duration_min"]
    calories = exercise["nf_calories"]
    add_row(current_date,current_time,exercise_subject,duration, calories)





print("Processing")
print(response.status_code)
print(response.json())



