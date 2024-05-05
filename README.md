**MUTUAL FUND PERFORMANCE INSIGHTS APPLICATION**

**(See Documentation.pdf for full details)**


1. **USAGE GUIDELINES.**  
  
   **Steps to run this project on local system**

a. Clone the repository  
b. The dataextraction.py file is run once at the start to generate mutualfunds.csv using the RAGathon mutual funds Datasets.

c. Then run streamlit\_app.py using the command:  
    streamlit run streamlit\_app.py

d. The app opens at http://localhost:8501/

**Steps to use the app**

- Use the tabs to navigate to various functionalities : Generate report, Visualize data, Upload reports and Report PDFs

- Generate report tab:

   Choose the required schemes and fields to display the respective report. It could be downloaded as a csv file by clicking the download button at the top of the dataframe.

- Visualize data tab:

   Choose the required schemes and fields to generate a line chart.

- Upload reports tab:

   Choose one or more report pdfs and click update data to add its data to original dataset generated.

- Report PDFs tab:

   View all the uploaded pdf and click the button to download them and delete button to delete all the reports.

- Dataset tab:

   View the entire dataframe extracted from all the report pdfs. Click clear dataset button to delete all data.


2. **AN OVERVIEW OF THE APPLICATION’S FEATURES AND FUNCTIONALITIES.**

- Scheme Selection
- Download Capability
- Field Selection and Calculation
- Dynamic Reporting
- Based on the user’s selections of schemes and fields, dynamically generate a report on the screen. This real-time data visualization supports immediate analysis and decision-making
- Dynamic csv reports
- Dynamic graph reports
- Data Upload Functionality
- Inform if report is already uploaded before uploading  
- View and delete uploaded reports  
- View and delete the generated dataframe
- Refer Documentation.pdf for full details

3. **ANY NECESSARY CONFIGURATIONS OR DEPENDENCIES NEEDED TO RUN THE APPLICATION.**

- The main packages required for the app are streamlit, pdfplumber, pandas, numpy, matplotlib and os.
- Refer requirements.txt for full details.
