QuoDroid

Steps to setup the project

git clone https://github.com/PAVANKUMAR-KUNTOLLA/QuoDroid.git
python -m venv venv
linux - source venv\bin\activate, windows - venv\Script\activate
cd core
pip install -r requirements.txt
python manage.py runserver

Chrome Driver Integration
1. Download Chrome Driver
Visit the official ChromeDriver website: ChromeDriver Downloads
Download the appropriate Chrome driver compatible with your system.
2. Extract Chrome Driver
Extract the downloaded Chrome driver archive to obtain the executable file.
3. Set Chrome Driver Path
Create a file named .env in the root directory of your project.
Add the following content to the .env file, specifying the path to the Chrome driver executable:
chrome_driver_dir=/path/to/chromedriver
Replace /path/to/chromedriver with the actual path to the Chrome driver executable on your system.


API Endpoints
1. Execute Test Suite
URL:  http://127.0.0.1:8000/testai/tests/v1/execute
Method: POST
Headers: Content-Type: application/json
Body:
json format
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

