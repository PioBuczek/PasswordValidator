
![ValidatorPassword](https://github.com/PioBuczek/PasswordValidator/assets/137912290/dd347673-238c-4ccf-b2e4-f056c8e7ec49)


### A few words about project:

Project is an application written in Python, used to validate and save a user's login and password. It allows users to check the strength of their passwords, ensuring they meet specific criteria, such as length, presence of digits, uppercase and lowercase letters, and special characters. Additionally, the application securely stores validated passwords in a PostgreSQL database.


### How start this application ?

Before we start, you need to create a database(This project is used PostgreSQL version 15). You need to know, that this project was tested in Postgres. 

Firstly, you need to clone my repo to my GitHub, and you need to use commande: 
<div class="termy">

```console
git clone https://github.com/PioBuczek/PasswordValidator.git
```
</div> 

Then you need to go into a higher file, you need the command:
<div class="termy">

```console
cd PasswordValidator
```

You need to create Environment Variables. You can set up environment variables in your system by following these steps:

1. Open "Control Panel" and search for "System Properties."
2. Click on "Environment Variables."
3. In the "System Variables" section, click "New" to add a new variable.
4. Add the variable name (e.g., pv_dbname) and its corresponding value (e.g., my_database_name).
5. Repeat the above step for all the environment variables listed above.

After setting up the environment variables, create a .env file in the root directory of the project and add the environment variables there in the following format:

<div class="termy">

```console
pv_dbname=my_database_name
pv_host=my_host
pv_user=my_username
pv_password=my_password
pv_port=my_port

```
</div> 


If you don't want set up environment variables, you can create a .env file in the root directory of the project and add the environment variables there in the following format:


```console
python -m venv YourVenv
./YourVenv/Scripts/activate.ps1
pip install -r requirements.txt  
python main.py
```

### More details

The main elements of project are:

The "functions.py" file contains classes, that implements a various password validators. Each class represents a diffrent condition that must be met by the password.

The "database.bd" file contains class, that acts as a Context Manager and allows you to connect and interact with PostgreSQL database. In database stores saveed logins and hashed passwords, that have met all validation requirements. 

The "interface.py" file contains class, that implements a graphic interpface using Tkinter library. Interface allows user to enter login and passoword, and then chceck, that password meets all validation requirements. If so, the password is saved in the database. 

The "main.py" contains function, that launches application and creates the main graphic window.

The "settings.py" file contains classe, that is responsible for reading and storing environment variables needed for a specific application. It uses the os.getenv() function to retrieve the values of environment variables. These environment variables are crucial for configuring the application to connect to a database.


Project "PasswordValidator" include also a set of unit test, that check the correct operation of individual componets of application. The tests were written using the unittest module.

In application, I used abstract class for validators, exception handling and then use of a context manager to interact with the database. 
