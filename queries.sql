-- 1. Find the top 5 highest paying jobs for Entry-Level candidates
SELECT Job_Title, Industry, Location, Max_Salary_INR 
FROM Job_Market
WHERE Experience_Level = 'Entry-Level'
ORDER BY Max_Salary_INR DESC
LIMIT 5;

-- 2. Count the number of Remote vs On-Site jobs in Bengaluru
SELECT Work_Type, COUNT(Job_ID) as Total_Jobs
FROM Job_Market
WHERE Location = 'Bengaluru'
GROUP BY Work_Type;

-- 3. Calculate average minimum salary for Data Scientists and Software Engineers
SELECT Job_Title, AVG(Min_Salary_INR) as Average_Base_Pay
FROM Job_Market
WHERE Job_Title IN ('Data Scientist', 'Software Engineer')
GROUP BY Job_Title;

-- 4. Find companies offering hybrid work with a maximum salary above 15 Lakhs
SELECT Job_ID, Job_Title, Location, Required_Skills
FROM Job_Market
WHERE Work_Type = 'Hybrid' AND Max_Salary_INR > 1500000;