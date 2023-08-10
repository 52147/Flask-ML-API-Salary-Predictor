# Flask ML API: Salary Predictor

This API uses a pre-trained model to predict the salary based on a given experience in years.

## Table of Contents

- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Endpoints](#endpoints)
- [Testing](#testing)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

- Python 3.x installed.
- `pip` installed (usually comes with Python).
- Basic knowledge of Flask and Python.
- Postman or `curl` for endpoint testing.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd model_backend
   ```
   
2. **Set up a Virtual Environment** (Recommended):
   This keeps dependencies for this project separate from your global Python environment.

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Start the Server**:
   ```bash
   python server.py
   ```
   Once started, the API should be live at http://localhost:5001/.

## Endpoints
1. **Salary Prediction**:
   - **Endpoint**: /api
   - **Method**: POST
   - **Body**:
   - ```
     {
       "exp": <experience_in_years_as_float>
     }
     ```
   - Returns: Predicted salary and a message.
2. **Health Check**:
   - **Endpoint**: /test
   - **Method**: GET
   - **Returns**: A "Hello, World!" string to verify the server is running.
3. **Model Metadata**:
   - **Endpoint**: `/model/metadata`
   - **Method**: `GET`
   - **Returns**: Metadata about the model such as its name, creation date, version, and description.
4. **Server Status**:
   - **Endpoint**: `/server/status`
   - **Method**: `GET`
   - **Returns**: The current time on the server, its running status, and its load average (UNIX systems only).

## Testing
For local testing, you can use curl:
```bash
curl -X POST -H "Content-Type: application/json" -d '{"exp": 1.8}' http://localhost:5001/api
```
Or, use **Postman**:

Set the method to POST.
1. Enter the URL http://localhost:5001/api.
2. Under Headers, set Content-Type to application/json.
3. Under Body, select raw input and input {"exp": 1.8}.
4. Hit send and review the response.
## Troubleshooting
1. **Address already in use**: Ensure no other services are running on port 5001 or change the port in server.py.
2. **Model not found**: Ensure model.pkl is in the root directory.
## Contributing
1. Fork the repository.
2. Create a new branch for your features or bug fixes.
3. Commit changes and open a pull request.
4. Ensure your code is clear and has comments where needed.

## License
The code in this project is licensed under the MIT license. See the [LICENSE]() file for more information.

