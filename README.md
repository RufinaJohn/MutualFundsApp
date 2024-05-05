**RAGATHON CHALLENGE: MUTUAL FUND PERFORMANCE INSIGHTS APPLICATION**


1. **USAGE GUIDELINES.**

   **Steps to run this project on local system**

1. Clone the repository
1. The dataextraction.py file is run once at the start to generate mutualfunds.csv using the RAGathon Datasets provided in https://aiordinate.com/iitm-ragathon:

- MF Data - March 2022 - April 2021.pdf
- MF Data - March 2023 - April 2022.pdf
- MF Data - March 2024 - April 2023.pdf

1. Then run streamlit\_app.py using the command:

streamlit run streamlit\_app.py

1. The app opens at http://localhost:8501/

**Steps to use the app**

1. Use the tabs to navigate to various functionalities : Generate report, Visualize data, Upload reports and Report PDFs

1. Generate report tab:

   Choose the required schemes and fields to display the respective report. It could be downloaded as a csv file by clicking the download button at the top of the dataframe.

1. Visualize data tab:

   Choose the required schemes and fields to generate a line chart.

1. Upload reports tab:

   Choose one or more report pdfs and click update data to add its data to original dataset generated.

1. Report PDFs tab:

   View all the uploaded pdf and click the button to download them and delete button to delete all the reports.

1. Dataset tab:

   View the entire dataframe extracted from all the report pdfs. Click clear dataset button to delete all data.


1. **AN OVERVIEW OF THE APPLICATION’S FEATURES AND FUNCTIONALITIES.**

**Scheme Selection:**

`   `- Implement a selection tool that allows users to choose one or multiple mutual fund schemes. This feature enables tailored data retrieval, catering to specific user interests or analysis requirements.

**Single scheme**




**Multiple scheme**



**Scheme type**




**Scheme subtype**




**Fullscreen**




**Search data**




**Download Capability:**

`   `- Include a functionality that allows users to download the generated report as a .csv file, facilitating further data analysis or sharing outside the application.






**Field Selection and Calculation:**

`   `- Users should be able to select one or multiple data fields from the provided dataset. Additionally, the application must offer the capability to compute and select derived fields such as:

`     `- Net Inflow or Outflow: Calculated as `Funds Mobilized for the month - Repurchase/Redemption for the month`.

`     `- Net Asset under Management per Scheme: Determined by dividing the `Net Assets Under Management` by the `No. of Schemes`.

`     `- Net Inflow or Outflow per Scheme: This is the ratio of `Net Inflow or Outflow` to the `No. of Schemes`.

**I have included the above three calculated field in the dataframe. Users can choose to view them or select all fields to display.**




**Dynamic Reporting:**

`   `- Based on the user’s selections of schemes and fields, dynamically generate a report on the screen. This real-time data visualization supports immediate analysis and decision-making.

**Dynamic csv reports**




**Dynamic graph reports**






**Data Upload Functionality:**

`   `- Provide a feature to upload new monthly reports in PDF format. This capability ensures that the application remains up-to-date with the latest mutual fund performance data.



**Inform if report is already uploaded**



**View and delete uploaded reports:**



**View and delete the generated dataframe:**



1. **ANY NECESSARY CONFIGURATIONS OR DEPENDENCIES NEEDED TO RUN THE APPLICATION.**

- The main packages required for the app are streamlit, pdfplumber, pandas, numpy, matplotlib and os.
- Refer requirements.txt for full details.
