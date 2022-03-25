# Simple Django app that loads all products from SHOPER Api and then creates products on SHOPIFY platform.


Currently my company is starting a branch in USA. On European market we are running a store via Shoper platform, but for US market we decided to go with Shopify.
Although, I could import all our products via csv file, I decided to create an API import program, that will do some cleaning on the data.

- Management command that pulls Images from Shoper is implemented!
- Second management command that downloads Products from Shoper is working.
- Adding Images to parrent Product on creation of Product object is working.
- Added kill_db.py script in root of the project to find and delete migration files and data base files.
- Working on: testing...
