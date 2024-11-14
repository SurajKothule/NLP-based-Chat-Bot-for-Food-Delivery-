

import re
def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result

#if __name__=="__main__":
    #print(get_str_from_food_dict({"samosa":2,"aloo":3}))
    #print(extract_session_id("projects/foodieee-chatbot-for-food-hjbu/agent/sessions/d42a5529-6cb4-8d37-71a8-8593b87b9df9/contexts/ongoing-order"))