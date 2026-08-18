from pathlib import Path
from statistics import mean
import json

DATA_FILE = Path(__file__).parent / "full_database" / "data" / "responses.jsonl"

from statistics import NormalDist



responses = [
    json.loads(line)
    for line in DATA_FILE.read_text(encoding="utf-8").splitlines()
    if line.strip()
]
# take token as an arugment everywhere

def likert_to_number(likert_item):
    num = likert_item[0]
    try:
        return int(num)
    except TypeError as e:
        print(f"this doesn't have a proper likert format, first letter is {num}")
        return None

def calculate_average(list_of_vars, username = "anna"):
    list_of_vars_int = []
    for var in list_of_vars:
        user_record = next(r for r in responses if r["username"] == username)
        answer = user_record["answers"][var]
        if isinstance(answer, str):
            list_of_vars_int.append(likert_to_number(answer))
        else:
            list_of_vars_int.append(answer)
    # We ignore Nones:
    list_of_vars_int = [answer for answer in list_of_vars_int if answer is not None]
    
    return mean(list_of_vars_int)

print(calculate_average(["absorption1", "absorption2", "absorption3"]))


def absorption_text(username = "anna"):
    avg_absorption = calculate_average(["absorption1", "absorption2", "absorption3"], username = username)
    z_value = (avg_absorption*2.389705)/25
    percentile = NormalDist().cdf(z_value) 
    text = ""
    if percentile>40:
        text = "You have below average trait absorption."
    elif percentile>60:
        text = "You're pretty average in trait absorption!"
    else:
        text = "You have pretty high trait absorption!"
    
       # 0.9331927987311419  → 93.3rd percentile

    return f"""{text} You scored roughly at {round(percentile*100, 1)} percentile"""

print(absorption_text())





def readiness_int(username = "anna"):
    user_record = next(r for r in responses if r["username"] == username)
    readiness1 = user_record["answers"]["readiness1"]
    readiness2 = user_record["answers"]["readiness2"]
    return readiness2-readiness1

print(readiness_int())

def readiness_text(username = "anna"):
    readiness=readiness_int()
    if readiness == 0:
        return "stayed the same."
    elif readiness > 0:
        return f"has increased by {readiness}. Yay!"
    elif readiness < 0:
        return f"has decreased by {readiness}... sorry lol."


print(readiness_text())

def starting_dose_calculated(username = "anna"):
    user_record = next(r for r in responses if r["username"] == username)
    dose_preference_10 = int(user_record["answers"]["dose_preference"])
    # 0.5  = 1
    # 2.75 = 10
    # 2.25 / 10 = 0.225
    result = 0.7 + (dose_preference_10-1)*0.21
    
    return result

print(starting_dose_calculated())


def absorption_dose_factor(username = "anna"):
    absorption_avg = calculate_average(["absorption1", "absorption2", "absorption3"], username = username)
    
    standardized = (absorption_avg-2.389705)/5
    standardized = standardized*-1 #because more absorption menas less dosing
    
    # maximally it can go 0.5 down or 0.5 up
    # so if you wanna take 1.7 g -> 0.85g down or up
    
    weighting = 0.2
    
    factor = weighting*standardized
    
    return factor

print(1.9+(1.9*absorption_dose_factor()))

def sensitvity_dose_factor(username = "anna"):
    user_record = next(r for r in responses if r["username"] == username)
    
    list_of_sensitivity_items = []
    data_amount = 0
    
    #which sensitivities?
    if user_record["answers"]["weed_experience"] == "yes":
        list_of_sensitivity_items.append("weed_sensitivity")
        data_amount+=1
        
    if user_record["answers"]["psych_experience"] == "yes":
        list_of_sensitivity_items.append("psych_sensitivity")
        list_of_sensitivity_items.append("psych_sensitivity")
        list_of_sensitivity_items.append("psych_sensitivity")
        list_of_sensitivity_items.append("psych_sensitivity")
        data_amount+=4
        
    list_of_sensitivity_items.append("other_sensitivity")
    list_of_sensitivity_items.append("other_sensitivity")
    data_amount+=2

    absorption_avg = calculate_average(list_of_sensitivity_items, username = username)
    
    standardized = (absorption_avg-5)/10
    standardized = standardized*-1 #because more sensitivity menas less dosing
    
    # maximally it can go 0.5 down or 0.5 up
    # so if you wanna take 1.9 g -> 0.85g down or up
    
    weighting = 0.09 + (0.03*data_amount)
    
    factor = weighting*standardized
    return factor
    

print(1.9+(1.9*sensitvity_dose_factor()))
print(1.9+(1.9*sensitvity_dose_factor())+(1.9*absorption_dose_factor()))

def weight_dose_factor(username = "anna"):
    user_record = next(r for r in responses if r["username"] == username)
    body_weight = int(user_record["answers"]["body_weight"])
    
    standardized = (body_weight-71)/71    
    weighting = 0.15
    
    factor = weighting*standardized
    
    return factor

print(1.9+(1.9*weight_dose_factor()))
