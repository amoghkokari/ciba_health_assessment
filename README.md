detailed instructions on how to set up and run the Azure Function locally

Setup instructions.
Environment variable details.
How to run the function locally.

# Insurance Requirements Extraction API - Azure Function

This project is an Azure Function that extracts insurance requirements from an input insurance clause and returns a structured JSON output. The function leverages a backend LLM (Large Language Model) to generate responses.

## Table of Contents

- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Running the Function Locally](#running-the-function-locally)
- [Testing the Function](#testing-the-function)
- [Additional Problems you might face](#dependencies)

---

## Getting Started

### Prerequisites

- **Azure Functions Core Tools** (v3 or higher): Required for local development and testing.
- **Python 3.8+**: The runtime environment for the Azure Function.
- **Visual Studio Code** (optional): Recommended IDE with the Azure Functions extension for easy management.

### 1. Clone the Repository

- Clone this repository to your local machine:
- ```bash
- git clone https://github.com/amoghkokari/ciba_health_assessment.git
- cd ciba_health_assessment

### 2. Install Dependencies

- **clause_env** virtual environemnt contains all the installed packages, you can just change to that environemnt and try running the application (from root directory source clause_env/bin/activate )
- **requirements.txt** file have all the required packeges you can directly do (from root directory pip install -r /path/to/requirements.txt) either in environment or virtual environment if you face any issues

## Environment Variables

- **LLM_API_KEY=your-llm-api-key** inside ciba_health_assessment create a .env file for environment varialbe and mention LLM_API_KEY, currently using gemini key which can be generatedd for free here - https://aistudio.google.com/app/apikey

## Running the Function Locally
- Open a terminal, or use visual studio's terminal, navigate to the project directory, and start the function locally using **func start**

## Testing the Function
- Instructions for testing the function locally using curl or any other HTTP client. You can use postman for post request on the endpoint. From terminal you can pass curl request

Example using curl:
curl -X POST http://localhost:7071/api/generate_response \
--header "Content-Type: application/json" \
--data '{ "clause": "your-insurance-clause-string" }'

example request
curl -X POST 'http://localhost:7071/api/generate_response' \
--header 'Content-Type: application/json' \
--data '{
    "clause" : "Insurance. Servco will obtain and maintain during the term of this Agreement the following types of insurance, in amounts not less than the following: (a) statutory limits worker’s compensation and employer’s liability in the amount of not less than $1,000,000 per occurrence; (b) commercial general liability in the amount of not less than $1,000,000 per occurrence and $2,000,000 aggregate; (c) commercial automobile liability (including all owned, non-owned and hired vehicles) in the amount of not less than $1,000,000 combined single limit; and (d) umbrella liability insurance in amount of not less than $5,000,000 per occurrence. Each such policy (excepting workers compensation and employers liability) shall list Client as an “additional insured”. Workers compensation and employer’s liability, commercial general liability and commercial automobile coverage shall be primary coverage. Umbrella liability follows the commercial general liability form, but is excess by nature. Workers compensation and employer’s liability, commercial general liability, and commercial automobile coverage shall provide waiver of subrogation in favor of Client. Workers compensation and employer’s liability, commercial general liability, commercial automobile coverage and umbrella liability coverage shall provide that the insurer shall give thirty (30) days prior written notice to Client prior to cancellation. Upon written request, copies of such policies or certificates thereof shall be delivered to Client by Servco. Servco shall cause each of its subcontractors to carry insurance of the types and amounts necessary to cover risks inherent in the work of that subcontractor. When requested by Client, Servco shall furnish Client with certificates of insurance evidencing coverage for each subcontractor."
}'

## Additional Problems you might face
 - The imports from different files werent working for me so I had to change path, here is the code if you face same problem
for mac users
- export PYTHONPATH="${PYTHONPATH}:/path/to/cloned/file/ciba_health_assessment/"
