from dataclasses import dataclass
import json
import time


#This is state management for the agent, stateful agent.
@dataclass
class AgentProfile:
    agent_name: str
    model_engine: str
    temperature: float

    #Default values
    max_retries: int = 3
    is_active: bool = True

#No need to create constructor, dataclass will handle it and we can directly create instances of AgentProfile with the required attributes.

print("-- Initializing Agent Profile --")

primary_agent = AgentProfile(agent_name="DataBot_v1", model_engine="gpt-4", temperature=0.3)

print(f"Agent Name: {primary_agent.agent_name}, initialized with Model Engine: {primary_agent.model_engine} and Temperature: {primary_agent.temperature}")

config_filename = "agent_config.json"

print("\n-- Saving Configuration to JSON File --")
with open(config_filename, 'w') as config_file:
    json.dump(primary_agent.__dict__, config_file, indent=4)


print(f"Configuration saved to {config_filename}")

# Robust Error handling in Python
def mock_api_call(payload: dict, simulate_timeout=False, simulate_missing_key=False):
    print("\n-- Simulating API Call --")
    try:
        #simulate a missing key when llm forget to return key
        if simulate_missing_key:
            malformed_response = {"text":"hello world"}
            tokens = malformed_response['usage_metrics']
            print("Tokens Used:", tokens)

        if simulate_timeout:
            time.sleep(10)
            raise TimeoutError("Simulated API timeout occurred.")
        
        print("API call successful with payload:", payload)
    except KeyError as e:
        print(f"KeyError: Missing key in API response - {e}")
    except TimeoutError as e:
        print(f"TimeoutError: {e}")
    finally:
        print("API call simulation completed.")

if __name__ == "__main__":
    mock_api_call(payload={'data': 'test'}, simulate_timeout=True)

    mock_api_call(payload={'data': 'test'}, simulate_timeout=True, simulate_missing_key=True)