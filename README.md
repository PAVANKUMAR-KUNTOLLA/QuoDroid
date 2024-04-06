QuoDroid
Steps to Set up the Project:
Clone the Repository:

git clone https://github.com/PAVANKUMAR-KUNTOLLA/QuoDroid.git

Create Virtual Environment:

python -m venv venv

Activate Virtual Environment:

Linux:

source venv/bin/activate

Windows:
venv\Scripts\activate

Navigate to Core Directory:

cd QuoDroid/core

Install Requirements:

pip install -r requirements.txt

Run the Server:

python manage.py runserver

Chrome Driver Integration:

Download Chrome Driver:

Visit the official ChromeDriver website.
Download the appropriate Chrome driver compatible with your system.

Extract Chrome Driver:

Extract the downloaded Chrome driver archive to obtain the executable file.

Set Chrome Driver Path:

Create a file named .env in the root directory of your project.
Add the following content to the .env file, specifying the path to the Chrome driver executable:
javascript

chrome_driver_dir=/path/to/chromedriver
Replace /path/to/chromedriver with the actual path to the Chrome driver executable on your system.

API Endpoints:

Execute Test Suite:
URL: http://127.0.0.1:8000/testai/tests/v1/execute
Method: POST
Headers: Content-Type: application/json
Body:
{
  "tests": [
    {
      "title": "Test Case 1",
      "steps": [
        "Open Browser browser=chrome",
        "Go To url=https://google.com"
      ]
    }
  ]
}
