import pandas as pd

def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    fd = pd.DataFrame(employees)
    return fd.head(3)
