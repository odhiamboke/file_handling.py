import datetime

# File Creation
try:
    with open('my_file.txt', 'x') as f:
        pass
except FileExistsError as e:
    pass

try:
    with open('my_file.txt', 'w') as f:
        f.write('Hello, world!\n')
        f.write('This is a file created by Python.\n')
        f.write('The current date and time is: {}\n'.format(datetime.datetime.now().strftime('%a, %b %d %H:%M')))
except Exception as e:
    print('Error creating file:', e)

# File Reading and Display
try:
    with open('my_file.txt', 'r') as f:
        print('File contents:')
        print(f.read())
except Exception as e:
    print('Error reading file:', e)

# File Appending
try:
    with open('my_file.txt', 'a') as f:
        f.write('\nThis is an appended line.')
        f.write('\nThis is another appended line.')
        f.write('\nThis is the last appended line.')
except Exception as e:
    print('Error appending to file:', e)

# Error Handling
try:
    # Try to open a non-existent file
    with open('non_existent_file.txt', 'r') as f:
        print(f.read())
except FileNotFoundError as e:
    print('File not found:', e)
except PermissionError as e:
    print('Permission denied:', e)
except Exception as e:
    print('Unexpected error:', e)
finally:
    print('This will run whether there was an error or not.')