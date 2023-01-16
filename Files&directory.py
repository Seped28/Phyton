#checking files in a directoty using the relative path
from pathlib import Path

path = Path()
#to find python files in the directory
for file in path.glob('*.py'):
    #you can add a single * to search all files and directoried 
    print(file)
 
        
