import re
from datetime import datetime
import os
import fitz


def load_resume(resume_folder):
    resumes = []
    resume_names = []
    for filename in os.listdir(resume_folder):
        if filename.endswith('.pdf'):
            # Open the PDF file
            with open(os.path.join(resume_folder, filename), 'rb') as f:
                # Read the PDF file
                text= ""
                with fitz.open(f) as doc:
                    for page in doc:
                        text += str(page.get_text())
                        # print(text)
                resumes.append(" ".join(text.split("\n")))
                # print(text)
                # print("------------------------------------------------------------------------------------------")
        resume_names.append(filename)
    return resumes , resume_names



def extract_experience(resume_texts):
    total_exp = []    
    for resume_text in resume_texts:
        experience_years = 0
        
        # # Search for internship and project information
        # pattern1 = r"(?:Duration\s*-\s*([A-Z]{3}\s*\d{4})\s*–)|(?:\d{4}\s*-\s*\d{4})"
        # matches1 = re.findall(pattern1, resume_text)
        
        # # Calculate the total years of experience from specific date ranges
        # for match in matches1:
        #     if match[0]:
        #         start_year = int(match[0].split()[1])
        #         end_year = int(match[0].split()[2])
        #         experience_years += (end_year - start_year)
        #     elif match[1]:
        #         start_year = int(match[1].split('-')[0])
        #         end_year = int(match[1].split('-')[1])
        #         experience_years += (end_year - start_year)
        
        # Search for "Oct 2021 to Present" pattern
        pattern2 = r"([A-Z][a-z]{2}\s\d{4})\s*to\s*Present"
        matches2 = re.findall(pattern2, resume_text)
        
        # Calculate the total years of experience from "Oct 2021 to Present" pattern
        current_year = datetime.now().year
        for match in matches2:
            start_year = int(match.split()[1])
            experience_years += (current_year - start_year)
        
        # Search for specific date range pattern like "Feb 2021 to Sep 2021"
        pattern3 = r"([A-Z][a-z]{2}\s\d{4})\s*to\s*([A-Z][a-z]{2}\s\d{4})"
        matches3 = re.findall(pattern3, resume_text)
        
        # Calculate the total years of experience from specific date range pattern
        for match in matches3:
            start_year = int(match[0].split()[1])
            start_month = datetime.strptime(match[0].split()[0], "%b").month
            end_year = int(match[1].split()[1])
            end_month = datetime.strptime(match[1].split()[0], "%b").month
            
            # Calculate the difference in years and months
            months_diff = (end_year - start_year) * 12 + (end_month - start_month)
            experience_years += months_diff / 12
        
        # Search for specific date range pattern like "JUN 2022 - JULY 2022"
        pattern4 = r"([A-Z][a-z]{2,9})\s*\d{4}\s*-\s*([A-Z][a-z]{2,9})\s*\d{4}"
        matches4 = re.findall(pattern4, resume_text)
        
        # Calculate the total years of experience from specific date range pattern
        for match in matches4:
            start_month = datetime.strptime(match[0], "%B").month
            start_year = int(match[0].split()[1])
            end_month = datetime.strptime(match[1], "%B").month
            end_year = int(match[1].split()[1])
            
            # Calculate the difference in years and months
            months_diff = (end_year - start_year) * 12 + (end_month - start_month)
            experience_years += months_diff / 12
        
        # Search for specific date range pattern like "OCT-2022 - MARCH-2023"
        pattern5 = r"([A-Z]{3})-\d{4}\s*-\s*([A-Z]{3})-\d{4}"
        matches5 = re.findall(pattern5, resume_text)
        
        # Calculate the total years of experience from specific date range pattern
        for match in matches5:
            start_month = datetime.strptime(match[0], "%b").month
            start_year = int(match[0].split('-')[1])
            end_month = datetime.strptime(match[1], "%b").month
            end_year = int(match[1].split('-')[1])
            
            # Calculate the difference in years and months
            months_diff = (end_year - start_year) * 12 + (end_month - start_month)
            experience_years += months_diff / 12
        
        # Search for specific date range pattern like "September 2019 – March 2022"
        pattern6 = r"([A-Z][a-z]{2,9})\s*\d{4}\s*–\s*([A-Z][a-z]{2,9})\s*\d{4}"
        matches6 = re.findall(pattern6, resume_text)
        
        # # Calculate the total years of experience from specific date range pattern
        # for match in matches6:
        #     start_year = int(match[0].split()[1])
        #     start_month = datetime.strptime(match[0].split()[0], "%B").month
        #     end_year = int(match[1].split()[1])
        #     end_month = datetime.strptime(match[1].split()[0], "%B").month
            
        #     # Calculate the difference in years and months
        #     months_diff = (end_year - start_year) * 12 + (end_month - start_month)
        #     experience_years += months_diff / 12
        
        # Search for specific date range pattern like "September 2022 – present"
        pattern7 = r"([A-Z][a-z]{2,9})\s*\d{4}\s*–\s*present"
        matches7 = re.findall(pattern7, resume_text)
        
        # # Calculate the total years of experience from specific date range pattern
        # current_year = datetime.now().year
        # for match in matches7:
        #     start_year = int(match.split()[1])
        #     start_month = datetime.strptime(match.split()[0], "%B").month
            
        #     # Calculate the difference in years and months
        #     months_diff = (current_year - start_year) * 12 + (datetime.now().month - start_month)
        #     experience_years += months_diff / 12
        
        # Search for specific date range pattern like "12/2022 – 02/2023"
        pattern8 = r"(\d{2})/(\d{4})\s*–\s*(\d{2})/(\d{4})"
        matches8 = re.findall(pattern8, resume_text)
        
        # Calculate the total years of experience from specific date range pattern
        for match in matches8:
            start_month = int(match[0])
            start_year = int(match[1])
            end_month = int(match[2])
            end_year = int(match[3])
            
            # Calculate the difference in years and months
            months_diff = (end_year - start_year) * 12 + (end_month - start_month)
            experience_years += months_diff / 12
            
        total_exp.append(round(experience_years, 2))
        
        # print(pattern1)
        print(pattern2)
        print(pattern3)
        print(pattern4)
        print(pattern5)
        print(pattern6)
        print(pattern7)
        print(pattern8)
        print("--------------------------------------------------------------------------------------------------------------------------------------------")
    
    return total_exp

if __name__ == "__main__":
    resume_folder = '/home/indianic/Desktop/sentimate/resume_ranking/AI_ML_CVs'
    resumes , resume_name = load_resume(resume_folder)
    total_exps = extract_experience(resumes)
    for i in range(len(resumes)):
        print(resume_name[i],'----------------------------',total_exps[i])