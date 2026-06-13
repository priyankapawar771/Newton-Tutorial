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

system_prompt = f"System Instuction: You are a coorperate communicaion assistant. Task: Generate a professional email to all active users in the database. \n\n{context_block} Please ensure the email is concise and addresses all active users appropriately. and encorage them to stay engaged with the platform."

print("--Generated System Prompt--")
print(system_prompt)
print("---------------------------------")

def execute_llm_call(prompt_text, model_engine='gpt-4', **kwargs):
    print("Routing request to target model engine:", model_engine)
    print("Prompt Text:", prompt_text)
    print("Additional Parameters:", kwargs) 
    return f"Mock API Output: Welcome to the platform, {', '.join(active_users)}! We are excited to have you engaged with us. Stay tuned for more updates and opportunities to connect with the community."

if __name__ == "__main__":
    response = execute_llm_call(system_prompt, model_engine='gpt-4', temperature=0.7, max_tokens=150, top_k=5)
    print("LLM Response:\n", response)
