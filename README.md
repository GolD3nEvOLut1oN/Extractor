# Extractor
Spiders for retrieve prices &amp; products from most ecommerces in Chile

## ***Working Stores***
Store | Status | Last Update
--- | --- | --- 
Falabella | <img src="https://www.iconexperience.com/_img/g_collection_png/standard/512x512/ok.png" width=18px;> | 16-Mar-2018
Paris | <img src="https://www.iconexperience.com/_img/g_collection_png/standard/512x512/ok.png" width=18px;> | 16-Mar-2018
Ripley | Not fully functional | Needs update
Abcdin | not implemented yet | -
Corona | not implemented yet | -
Hites | not implemented yet | -
Lider | not implemented yet | -
LaPolar | not implemented yet | -

## ***Features***
- Dynamically gets all categories
- Navigate through the website's pages automatically
- Retrieve all products from each page
- Download data as a json or csv format

## ***Data structure***

Field | Type | Description
--- | --- | ---
Name | String | *Consist of the name of the product that we get from the Store*
Main category | String | *Name of main category of the market. Ex: "Computers"*
Main category URL | String | *Main URL category of the market. Ex: "http://www.example.com/Computers"*
Sub category | String | *Name of category child from Main Category. Ex: "Notebooks Gamers"*
Sub category URL | String | *URL of category child from Main Category. Ex: "http://www.example.com/Computers/Notebooks_Gamers"*
Normal price | int | *This price usually represents the normal price of the product with no discount*
Internet price | int | *This price usually means that there is some discount over normal price*
Card price | int | *This price usually represents the discount with "Store's Credit Card Only" over Normal or Internet price*
Product URL | String | *The URL of the product that we've extracted*
Product Image | String | *not fully functional*
Store ID | int | *not implemented yet*
Store Name | String | *not implemented yet*

## ***Requirements***

- Python 3.6.2
- Pip 3
- Scrapy 1.5.2
- Ubuntu 16.4 LTS
- Anaconda 3 (for Windows instances)

## ***Tested on***
- Windows 10 Pro 64bits
- Ubuntu 16.4 LTS

## ***How to install***

- Step 1
``` some code or command here ```
- Step 2
``` some code or command here ```
- Step 3
``` some code or command here ```

## ***Usage***
- In ``` cmd ``` 
