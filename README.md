# Django Shoper-API Client. This app was created for an Ecommerce store with huge database of products.
-
Project was started some time ago for my former employer. They had the idea of starting a branch store in USA. Also, they had a running store at Shoper platform on European market. For US market they decided to go with Shopify.
-
Although, I could import all our products via csv file, I decided to create an API import program, that will do some cleaning on the data.
-
To use this client you have to create .env file with:
- SHOPER_STORE='your.domain'
- SHOPER_LOGIN='yourshoperlogin'
- SHOPER_PASSWORD='yourshoperpassword'
- After that you can simply use 'docker compose up' to build images.
- You will need to run migrations.
- After images were built you can use management command 'python manage.py fetch_database_update' to pull categories, products, images, translations and stocks.

What was developed:
- Management command that pulls Images from Shoper is implemented!
- Management command that pulls Categories from Shoper is implemented!
- Second management command that downloads Products from Shoper is working.
- Implemented fetch_database_update command that download Categories, Products, Images, Stocks and related Translations for all objects. It also joins all objects in proper relationships.
- Added kill_db.py script in root of the project to find and delete migration files and data base files.
- Added an 'external' app, that serves scripts for calling SHOPER's API.
- Panel View that works as an admin site.
- Category Detail View, Product Detail View.
- 

Stuff to implement:
- Search funcionality for Products. 
