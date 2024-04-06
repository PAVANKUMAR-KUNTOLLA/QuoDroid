QuoDroid\n
Steps to Set up the Project:\n
Clone the Repository:\n\n
git clone https://github.com/PAVANKUMAR-KUNTOLLA/QuoDroid.git\n\n
Create Virtual Environment:\n\n
python -m venv venv\n\n
Activate Virtual Environment:\n\n
Linux:\n\n
source venv/bin/activate\n\n
Windows:\n
venv\Scripts\activate\n\n
Navigate to Core Directory:\n\n
cd QuoDroid/core\n\n
Install Requirements:\n\n
pip install -r requirements.txt\n\n
Run the Server:\n\n
python manage.py runserver\n\n
Chrome Driver Integration:\n\n
Download Chrome Driver:\n\n
Visit the official ChromeDriver website.\n
Download the appropriate Chrome driver compatible with your system.\n\n
Extract Chrome Driver:\n\n
Extract the downloaded Chrome driver archive to obtain the executable file.\n\n
Set Chrome Driver Path:\n\n
Create a file named .env in the root directory of your project.\n
Add the following content to the .env file, specifying the path to the Chrome driver executable:\n
javascript\n\n
chrome_driver_dir=/path/to/chromedriver\n
Replace /path/to/chromedriver with the actual path to the Chrome driver executable on your system.\n\n
API Endpoints:\n\n
Execute Test Suite:\n
URL: http://127.0.0.1:8000/testai/tests/v1/execute\n
Method: POST\n
Headers: Content-Type: application/json\n
Body:\n
{\n
  "tests": [\n
    {\n
      "title": "Test Case 1",\n
      "steps": [\n
        "Open Browser browser=chrome",\n
        "Go To url=https://google.com"\n
      ]\n
    }\n
  ]\n
}\n
