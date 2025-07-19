import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    fd = pd.DataFrame(employees)
    fd['salary'] = fd['salary']*2
    return fd
    
    
