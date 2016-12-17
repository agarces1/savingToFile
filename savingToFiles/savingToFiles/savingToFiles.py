fileName = "demo.csv"
#accessMode = 'w'
WRITE = 'w'#overwrites
APPEND = 'a'#adds to end of file
READWRITE = 'w+' #read anxd write
#myFile = open(fileName,accessMode)
#OR  for better readability
file = open(fileName, mode = WRITE)
#use the write function to write
#write does not put in a new line by itself
#use \n to specify text over multiple lines
file.write('Adrian, 22\n');
file.write('Stonehenge, 9000');
#if you open something always close it. get into the habit
file.close();
#good habit to print something out for user feed back
print('FIle written successfully');