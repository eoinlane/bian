import requests
from langchain.tools import Tool
from langchain.agents import initialize_agent

# Define API tools
create_invoice_tool = Tool(
    name="CreateInvoice",
    func=lambda params: requests.post(
        "http://customer_billing:8000/create", json=params
    ).json(),
    description="Creates a new invoice in the Customer Billing system.",
)

get_overdue_tool = Tool(
    name="GetOverdueInvoices",
    func=lambda: requests.get("http://customer_billing:8000/overdue").json(),
    description="Fetches overdue invoices for follow-up actions.",
)


# Define Ollama LLM integration
class OllamaLLM:
    def __init__(self, base_url="http://ollama:11434", model="llama3"):
        self.base_url = base_url
        self.model = model

    def generate(self, prompt):
        response = requests.post(
            f"{self.base_url}/api/generate",
            json={"model": self.model, "prompt": prompt},
        )
        print("Raw Response Content:", response.text)  # Add this line
        response.raise_for_status()
        return response.json()["text"]


# Initialize LangChain agent
ollama_llm = OllamaLLM(model="llama3")  # Replace "llama2" with your desired model
tools = [create_invoice_tool, get_overdue_tool]


# Simulate agent interaction using Ollama LLM
def run_agent(prompt):
    response = ollama_llm.generate(prompt)
    return response


# Sample usage
response = run_agent("Fetch all overdue invoices and suggest actions.")
print(response)
