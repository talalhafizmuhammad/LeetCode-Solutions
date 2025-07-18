import pandas as pd

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    fd = pd.DataFrame(students)
    fd['grade'] = fd['grade'].astype(int)
    return fd
    
