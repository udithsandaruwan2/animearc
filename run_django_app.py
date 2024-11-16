import os
import subprocess

# Navigate to Django project folder
os.chdir(r"D:\github\animearc")

# Activate virtual environment and runserver
subprocess.Popen(r'venv\Scripts\activate && python manage.py runserver', shell=True)

# Open the shortcut
os.startfile(r"C:\Users\udith\OneDrive\Desktop\animearc.lnk")
