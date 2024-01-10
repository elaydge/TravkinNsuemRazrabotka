import pandas as pd

data = pd.read_excel('lab_pi_101.xlsx')

df = pd.DataFrame(data) 
pi101_row = df[df['Группа']=='ПИ101']

df = df.iloc[1:] #исключение первой строки

#студенты с уникальным номером из группы Пи101 
unique_student_row = pi101_row['Личный номер студента'].unique()  
unique_student_row_str = [str(number) for number in unique_student_row] 
unique_student_row_str = ', '.join(unique_student_row_str)
#годы контроля ПИ101
year_control = pi101_row['Год'].unique()
year_control_row_str = [str(number) for number in year_control]
year_control_row_str = ', '.join(year_control_row_str)
#тип контроля пи101
type_control = pi101_row['Уровень контроля'].unique()
type_control_str = [str(number) for number in type_control]
type_control_str = ', '.join(type_control_str)

#global print
print('В исходном датасете содержалось', len(df) ,'оценок, из них', len(pi101_row),
'оценок относятся к группе ПИ101\n'
'В датасете находятся оценки', len(unique_student_row) ,
'студентов со следующими личными номерами:', unique_student_row_str, 
'\nИспользуемые формы контроля:', type_control_str ,
'\nДанные представлены по следующим учебным годам:',year_control_row_str)