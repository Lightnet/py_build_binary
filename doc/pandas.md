



https://www.freecodecamp.org/news/dataframe-to-csv-how-to-save-pandas-dataframes-by-exporting/
```py
import pandas as pd

# Create a sample dataframe
Biodata = {'Name': ['John', 'Emily', 'Mike', 'Lisa'],
        'Age': [28, 23, 35, 31],
        'Gender': ['M', 'F', 'M', 'F']
        }
df = pd.DataFrame(Biodata)

# Save the dataframe to a CSV file
df.to_csv('Biodata.csv', index=False)
```

```python
DataFrame.to_csv(filename, sep=',', index=False, encoding='utf-8')
```