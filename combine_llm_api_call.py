import time
users_database = [
    {"id": 101, "name": "Alice", "role": "admin", "is_active": True},
    {"id": 102, "name": "Bob", "role": "user", "is_active": False},
    {"id": 103, "name": "Charlie", "role": "editor", "is_active": True}
]

active_users = [user['name'] for user in users_database if user["is_active"]]
print("Active Users are:",active_users)
print(f"found{len(active_users)} active users in the database.")

context_block = ""

for index,name in enumerate(active_users, start=1):
    context_block += f"{index}. {name}\n"

print("Context Block:\n", context_block)

system_prompt = f"System Instuction: You are a coorperate communicaion assistant. \
                Task: Generate a professional email to all active users in the database. \n\n{context_block} Please ensure the email is concise and addresses all active users appropriately. \
                    and encorage them to stay engaged with the platform."

print("--Generated System Prompt--")
print(system_prompt)
print("---------------------------------")

def mock_api_call(prompt_text):
    print("\n-- Simulating API Call --")
    try:
        #make llm call and i got mock response
        time.sleep(10)
        #suppose this execute:
        #llm_response = llm.invoke(prompt_text)

        llm_response = {'result': ['Alice'], 'usage_metrics': {'tokens_used': 150, 'response_time': 1.2}}
        
        if llm_response:
            if llm_response['usage_metrics']:
                print("llm response :", llm_response)
            else:
                raise KeyError("Missing 'usage_metrics' key in LLM response.")
        else:
            raise TimeoutError("Simulated API timeout occurred.")
        
        print("API call successful ", llm_response)
    except KeyError as e:
        print(f"KeyError: Missing key in API response - {e}")
    except TimeoutError as e:
        print(f"TimeoutError: {e}")
    finally:
        print("API call simulation completed.")

if __name__ == "__main__":
    mock_api_call(system_prompt)
