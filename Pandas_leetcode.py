//practice
Write a solution to create a DataFrame from a 2D list called student_data. This 2D list contains the IDs and ages of some students.

The DataFrame should have two columns, student_id and age, and be in the same order as the original 2D list.

The result format is in the following example.

 

Example 1:

Input:
student_data:
[
  [1, 15],
  [2, 11],
  [3, 11],
  [4, 20]
]
Output:
+------------+-----+
| student_id | age |
+------------+-----+
| 1          | 15  |
| 2          | 11  |
| 3          | 11  |
| 4          | 20  |
+------------+-----+

ans:
import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df=pd.DataFrame(student_data,columns=['student_id', 'age'])
    return df



second question ans:

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    n_col,n_row=players.shape
    return [n_col,n_row]


First 3rows:

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    select_3_rows=employees.head(3)
    return select_3_rows



select data:
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    selected_data=students.loc[students['student_id']==101,['name','age']]
    return selected_data


Create a new Column:

def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus']=employees['salary']*2
    return employees


Drop duplicates based on specific columns with keep first occurence:
import pandas as pd

def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    df=customers.drop_duplicates(subset=['email'],keep='first')
    return df


Drop missing value if any column has Nan:
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    cleared_nan=students.dropna(subset=['name'])

    return cleared_nan


modify a column value:
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary']=employees['salary'].apply(lambda x:x*2)
    return employees

Reaname Columns:
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    df=students.rename(columns={
        'id':'student_id',
        'first':'first_name',
        'last':'last_name',
        "age":'age_in_years'

    } )
    return df


change data type of specific column
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade']=students['grade'].astype(int)
    return students

Fill missing value where is Nan,none:
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity']= products['quantity'].fillna(0)
    return products



concat:
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df=pd.concat([df1,df2],axis=0)
    return df


Method chainig:
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    fil_val=animals[animals['weight']>100]
    sort_val=fil_val.sort_values(by=['weight'],ascending=False)
    return sort_val[['name']].reset_index(drop=True)




