import spacy
import re

def extract_experience(resume_text):
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(resume_text)

    # Initialize variables
    total_experience = 0
    pattern = r'(\w+)\s+(\d+)\s*-\s*(\w+)\s+(\d+)'
    
    # Process each sentence in the document
    for sent in doc.sents:
        # Find matches for experience pattern
        matches = re.findall(pattern, sent.text)
        
        # Extract numerical values and add to total_experience
        for match in matches:
            start_month, start_year, end_month, end_year = match
            num_years = int(end_year) - int(start_year)
            total_experience += num_years
    
    return total_experience

resume_text = "Shraddha Sukumar Pisal Statistician | Data Scientist |  Data Analyst | Machine Learning  Mob - 8956043007 Email – shraddhapisal2000@gmail.com LinkedIn- https://www.linkedin.com/in/shraddha-pisal-4587a7210 Github- https://github.com/Shraddhap0 Career Objective A hard-working and a motivated student with the thirst of learning new things everyday. To enhance my  professional skills, knowledge and capabilities in organization which recognizes the value of hard work and trust  me with responsibilities and challenges. Passionate about finding solutions to real world problems. Internship - Projects 1. Company - Technocolabs Softwares Inc, Indore (Remote) ➢ Role - Data Analyst ➢ Duration - NOV 2022 – JAN 2023 ❖ •Mortgage Backed Securities Working on research, analysis, and preparation of project reports. • Worked on Data Analysis project for the company on various domains of tasks such as Data Analysis, Data  Manipulations, Data Classification techniques, Data Visualization, and deployment on a cloud platform with  python frameworks like Flask and Streamlit. 2. Company – AI Variant, Bangalore (Remote)  ➢ Role – Data Scientist ➢ Duration- FEB 2023 ❖ Bankruptcy Prevention • This is a classification project, since the variable to predict is binary (bankruptcy or non-bankruptcy). The  goal here is to model the probability that a business goes bankrupt from different features. • Worked on data analysis, data manipulation, machine learning algorithms and deployment with streamlit. Education ❖ Master degree in Statistics – Yashavantrao Chavan Institute of Science, Satara -July 2022 Score: 76.63%  (8.92 CGPA) ❖ Bachelor's degree in Statistics – Yashavantrao Chavan Institute of Science, Satara -July 2022 Score: 87% ❖ Class XII – Shahajiraje Mahavidyalaya,Khatav– Feb 2017 Score: 70.46% ❖ Class X – Kolhapur Divisional Board – March 2015 Score: 94% Academic Projects • Statistical Analysis of Heart Failure Patients Clinical Record : This project is based on secondary data which collected from website. Objectives of this project is study  survival analysis of patients, their association with demographic factors and to check accuracy. • Statistical Analysis of Brand Preference of Mobile Phones Among People : This project is based on primary data which is collected through google forms. The main objectives of this  project is to study perception buying behavior of people towards various phones, to study factors which helps in  sale of mobile phones, factors that influence decision making in purchasing mobile phones, to know preference  level associated with different mobile phones. Certifications ❖ certification program in Data Science by ExcelR Solutions – Nov 2022 cert no: 13739/EXCELR/20012023 ❖ Research Training at RIRD-Rayat Institute of Research and Development, Satara RIRD/RTP/2022/1185. ❖ Certification Course in Python - Yashavantrao Chavan Institute Science, Satara 2020-21/7279 ❖ Biostatistics and Design of Experiments-NPTEL online Certification NPTEL22BT13S44210178/2022 ❖ Maharashtra State Certificate in Information Technology (MS-CIT)Cert. No.17-3842885 ❖ Government Certificate in Computer Typing Basic Course (GCC-TBC) Cert. No151202090237 Technical Skills ❖ Analytical Tools: Tableau, Power BI, Advanced Excel. ❖ Programming Languages: Python, R Software, Machine learning, SAS ❖ Relational Database: MySQL Database ❖ Office Tools: Microsoft Office Applications (MS-Word, MS Excel, MS PowerPoint, MS Outlook) Key Skills ❖ Adaptable & Quick learner ❖ Team Player & Attention to details ❖ Leadership & Decision-making abilities ❖ Problem solving abilities ❖ Time management abilities Declaration- I hereby declare that the above-mentioned information is correct up to my knowledge and I bear the responsibility for the  correctness of the above-mentioned particulars. Date -   / / 2023 Regards           Shraddha Sukumar Pisal "


experience = extract_experience(resume_text)
print(experience)
