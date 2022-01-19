#создай здесь свой индивидуальный проект!
import pandas as pd
df = pd.read_csv('train.csv')
df.drop(['id', 'bdate', 'has_photo', 'has_mobile', 'followers_count', 'graduation',
'relation', 'life_main', 'people_main', 'city', 'last_seen', 'occupation_name', 'career_start',
'career_end'], axis=1, inplace=True)
def sex_apply(sex):
    if sex == 2:
        return 0
    return 1

df['sex'] = df['sex'].apply(sex_apply)
# print(df['education_form'].value_counts())
df['education_form'].fillna('Full-time', inplace = True)
df[list(pd.get_dummies(df['education_form']).columns)] = pd.get_dummies(df['education_form'])
df.drop(['education_form'], axis = 1, inplace = True)
print(df['education_status'].value_counts())
def status_apply(status):
    if status == 'Undergraduate applicant':
        return 0
    elif status == "Student (Bachelor's)" or status == "Student (Master's)" or status == "Student (Specialist)":
        return 1
    elif status == "Alumnus (Specialist)" or status == "Alumnus (Master's)" or status == "Alumnus (Bachelor's)":
        return 2
    else:
        return 3
df['education_status'] = df['education_status'].apply(status_apply)
# print(df['education_status'].value_counts())
def langs_apply(lang):
    if lang.find('English') != -1:
        return 1
    else:
        return 0
df['langs'] = df['langs'].apply(langs_apply)
# print(df['langs'].value_counts())
df['occupation_type'].fillna('university', inplace = True)
def occupation_type_apply(occupation_type):
    if occupation_type == 'university':
        return 0
    else:
        return 1
df['occupation_type'] = df['occupation_type'].apply(occupation_type_apply)
df.info()