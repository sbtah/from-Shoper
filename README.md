---
# from-Shoper
- Manage your Shoper store.
- Find missconfigured products.
- Set new urls for products and create 303 redirect if needed.
- Create a new Product in your Store, from copy of existing product.
- Disable enitre Products or Translations.
- Mass edit of Product data in you Store.
- Algorythmic creation of new static urls for your Products.
- Fetch all data for Categories, Products, Images, Stocks. For now...
---
## Django project, with PostgreSQL database, using my own shoper-api client.
### To start:
  - clone repo
  - docker compose build
  - place .env file in same dir as manage.py, containing :
    - SHOPER_DOMAIN='<yourstoredomain.xx>',
    - SHOPER_LOGIN='<login_to_your_store>',
    - SHOPER_PASSWORD='<your_store_password>',
  - get data by: 'python manage.py fetch_database' ...
### Data you can track at this moment:
  - Categories,
  - Products,
  - Stocks,
  - Images,
  - Category Translations,
  - Product Translations,
  - Image Trasnlations
  ---