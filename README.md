![MarsShop](https://user-images.githubusercontent.com/71176889/136710419-08e4ded8-f0e7-4023-8af6-e8a81e9ce206.gif)





## How run the project?



##### Clone the repository :
```bash
$ git clone https://github.com/Saeedahmadi7714/Django-Ecommerce-Website.git
$ cd Django-Ecommerce-Website
```
##### Create a virtualenv and activate it:
 ```bash
$ python3 -m venv venv
$ . venv/bin/activate
```
##### Or on Windows cmd : 
 ```bash
> py -3 -m venv venv
> venv\Scripts\activate.bat
```
##### Install the requirements :
```bash
$ pip3 install -r requirements.txt
```
##### Go to the main project route:
```bash
$ cd store
```
##### Creating a .env file from file .evn_sample.txt : 
```bash
$ cd conf
```

** ##### Open and read .env_sample.txt **
** ##### back to store folder **

#####  Run the tests :
```bash
python3 manage.py tests
```

#####  Run makemigrations and migrate :
```bash
python3 manage.py makemigrations
python3 manage.py migrate
```

#####  Run the development server :
```bash
python3 manage.py runserver
```
Open http://127.0.0.1:8000 in your browser. 

## License
[GNU GPLv3](https://https://choosealicense.com/licenses/gpl-3.0/)






