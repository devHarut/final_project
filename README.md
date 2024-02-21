# Password Strength Test

[Video Demo](https://youtu.be/hUthuBWwRyI)

## Description

When the user runs program, they are greeted with a menu:

- Option 1 is to see some preset passwords I have put into the program and their strengths.
- Option 2 is for the user to enter any password of their choice and let the program do its thing and print the strength of their password.
- Option 3 exits the program.

The program will repeatedly cycle the menu until the user has chosen option 3 to exit.

The way I value the password's strength is by:

- If the password has less than 8 characters, it's considered very weak.
- If the password has more than 8 but less than 12 characters, it's considered weak.
- If the password has upper case, lower case, and numbers, it is considered strong.
- If the password has upper and lower case along with numbers and special characters, it's considered very strong.

## Program Overview:

- I have defined four constant variables for the different password strengths at the top.

- The main function consists of the implementation of the menu inside of a loop.

- The test preset password function consists of four unique passwords I have hard coded and those passwords get passed through the get strength function and then is finally printed out along with its strengths, so when the user chooses option 1 they see 4 passwords and their strengths as an example.

- The get strength string function just returns a string form of the various password strengths I have defined at the top of the program as constant variables.

- The test password strength function is the heart of the program which any password that gets passed through is verified by the length of the password, if it has upper case and/or lowercase, along with if it has numbers or special characters and then a strength is determined.

- The test custom password function tests the strength of the password the user inputted when choosing option 2 from the menu.
