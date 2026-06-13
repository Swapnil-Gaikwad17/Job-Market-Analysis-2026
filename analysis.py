import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set a professional dark style
plt.style.use('dark_background')
sns.set_theme(style="darkgrid", rc={"axes.facecolor": "#1e1e1e", "figure.facecolor": "#1e1e1e", "axes.edgecolor": "#1e1e1e"})

# Load the dataset
df = pd.read_csv('Job_Market_Skill_Demand_2026.csv')

# --- Graph 1: Average Salary by Industry ---
df['Avg_Salary'] = (df['Min_Salary_INR'] + df['Max_Salary_INR']) / 2
industry_salary = df.groupby('Industry')['Avg_Salary'].mean().sort_values(ascending=False)

plt.figure(figsize=(12, 7))
ax1 = sns.barplot(x=industry_salary.values, y=industry_salary.index, palette='mako')

for i, v in enumerate(industry_salary.values):
    ax1.text(v + 50000, i, f"₹{v/100000:.1f}L", color='white', va='center', fontweight='bold')

plt.title('Average Compensation by Industry Sector (2026)', fontsize=16, fontweight='bold', color='white', pad=20)
plt.xlabel('Average Salary (INR)', fontsize=12, color='#cccccc')
plt.ylabel('Industry', fontsize=12, color='#cccccc')
plt.xticks(color='#cccccc')
plt.yticks(color='white', fontsize=11)
plt.tight_layout()
plt.savefig('Industry_Salary_Pro.png', dpi=300)
plt.close()

# --- Graph 2: Work Type Distribution (Donut Chart) ---
work_type = df['Work_Type'].value_counts()
plt.figure(figsize=(9, 9))
colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
plt.pie(work_type, labels=work_type.index, autopct='%1.1f%%', colors=colors, startangle=140, 
        textprops={'color':"w", 'fontsize': 12, 'weight': 'bold'}, pctdistance=0.85)

centre_circle = plt.Circle((0,0),0.70,fc='#1e1e1e')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)

plt.title('Work Model Distribution (Post-Pandemic Landscape)', fontsize=16, fontweight='bold', color='white', pad=20)
plt.tight_layout()
plt.savefig('Work_Type_Pro.png', dpi=300)
plt.close()

# --- Graph 3: Salary Distribution across Experience Levels ---
plt.figure(figsize=(12, 7))
order = ['Entry-Level', 'Mid-Level', 'Senior', 'Lead', 'Executive']
ax3 = sns.boxplot(x='Experience_Level', y='Avg_Salary', data=df, order=order, palette='coolwarm')

plt.title('Salary Disparity by Experience Level', fontsize=16, fontweight='bold', color='white', pad=20)
plt.xlabel('Experience Level', fontsize=12, color='#cccccc')
plt.ylabel('Average Salary (INR)', fontsize=12, color='#cccccc')
plt.xticks(color='white', fontsize=11)
plt.yticks(color='#cccccc')

ticks = ax3.get_yticks()
ax3.set_yticklabels([f"₹{int(tick/100000)}L" for tick in ticks])

plt.tight_layout()
plt.savefig('Experience_Salary_Pro.png', dpi=300)
plt.close()

# --- Graph 4: Top In-Demand Tech Skills ---
tech_jobs = df[df['Industry'] == 'IT & Tech']
top_skills = tech_jobs['Required_Skills'].value_counts().head(5)

plt.figure(figsize=(12, 6))
ax4 = sns.barplot(x=top_skills.values, y=top_skills.index, palette='flare')

for i, v in enumerate(top_skills.values):
    ax4.text(v + 5, i, str(v), color='white', va='center', fontweight='bold')

plt.title('Top 5 In-Demand Skill Combinations (IT & Tech)', fontsize=16, fontweight='bold', color='white', pad=20)
plt.xlabel('Number of Job Postings', fontsize=12, color='#cccccc')
plt.ylabel('Skill Requirements', fontsize=12, color='#cccccc')
plt.xticks(color='#cccccc')
plt.yticks(color='white', fontsize=11)
plt.tight_layout()
plt.savefig('Top_Skills_Pro.png', dpi=300)
plt.close()

print("Professional charts generated successfully.")