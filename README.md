# Simple Django app that loads all products from SHOPER Api and then creates products on SHOPIFY platform.


Project was started some time ago for my former employer. They had the idea of starting a branch store in USA. Also, they had a running store at Shoper platform on European market.For US market they decided to go with Shopify.
-
Although, I could import all our products via csv file, I decided to create an API import program, that will do some cleaning on the data.


- Management command that pulls Images from Shoper is implemented!
- Second management command that downloads Products from Shoper is working.
- Adding Images to parrent Product on creation of Product object is working.
- Added kill_db.py script in root of the project to find and delete migration files and data base files.
- Added ProductUpdateFromShoperView that pulls Data for product in view from Shoper Api.
- Added CreateLanguageCopyOfProductAtShoper view that will create a copy of product from specified product's translation, locally and on your Shoper store.
- Refactored update_database, import_images, import_product commands.
- Added an 'external' app, that serves scripts for calling SHOPER's API.
- Working on: testing...

# Todo
- Product model have to be refactored again. Each translation have to be a seperate object. Current implementation is just silly. Translations are stored as fields on model.

