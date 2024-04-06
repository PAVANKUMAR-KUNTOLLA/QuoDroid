import tempfile
import os
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from robot.api import TestSuiteBuilder
from robot.running.model import TestSuite
from decouple import config

@csrf_exempt
def execute_tests(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            tests = data.get('tests', [])
            
            for test in tests:
                with tempfile.NamedTemporaryFile(delete=False, suffix='.robot') as temp_file:
                    temp_file_path = temp_file.name

                    with open(temp_file_path, 'w') as f:
                        f.write("***Settings ***\n")
                        f.write("Library    SeleniumLibrary\n\n")
                        f.write("***Variables ***\n")

                        browser = ""
                        url = ""
                        
                        chrome_driver_dir = config("chrome_driver_dir")
                        chrome_driver_path = os.path.join(chrome_driver_dir, "chromedriver.exe")

                        for step in test['steps']:
                            if step.startswith("Open Browser browser="):
                                browser = step.split("Open Browser browser=")[1].split(",")[0].strip()
                            elif step.startswith("Go To url="):
                                url = step.split("Go To url=")[1].split(",")[0].strip()

                        if not browser:
                            raise ValueError("Browser not found in test steps")

                        if not url:
                            raise ValueError("URL not found in test steps")

                        f.write(f"${{browser}}\t{browser.lower()}\n")
                        f.write(f"${{url}}\t{url}\n")
                        

                        f.write("***Test Cases***\n")
                        title = test.get('title')
                        f.write(f"{title}\n")
                        f.write(f"\tOpen Browser\t{url}\t{browser.lower()}\texecutable_path={chrome_driver_path}\n")
                        f.write(f"\tSleep  2\n")
                        f.write(f"\tClose Browser\n")

                suite = TestSuiteBuilder().build(temp_file_path)
                result = suite.run()

            return JsonResponse({'status': result.return_code})

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
