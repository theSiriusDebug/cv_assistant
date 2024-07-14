**Step 1: Set up Your Python Environment**

Before you begin, ensure you have Python installed on your system. To create a virtual environment, run the following command:
```
python3 -m venv myenv
```

**Step 2: Register on Groq and Obtain an API Key**

Register on the Groq website at [https://console.groq.com/login](https://console.groq.com/login) and generate an API key. Once you have your key, export it as an environment variable:
```
export GROQ_API_KEY="your_key_here"
```

**Step 3: Configure Your Project**

Create two files:

1. **config.txt**: Store your personal information and default cover letter in this file.
2. **job_description.txt**: Store the job description in this file.

**Step 4: Run the Application**

To start the application, activate your virtual environment and run the following command:
```
source env/bin/activate

python3 main.py
```
