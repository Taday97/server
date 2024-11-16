# Django Project - API for Managing Products, Subcategories, and Subproducts

This is a Django project implementing a RESTful API for managing products, subcategories, and subproducts. It uses Django REST Framework (DRF) to create and consume endpoints for performing CRUD (Create, Read, Update, Delete) operations on products, subcategories, and subproducts, with name-based filtering and model relationships.

## Features

- **Products**: Create and retrieve products. Filter products by name.
- **Subcategories**: Create and retrieve subcategories. Filter subcategories by name and associate them with products.
- **Subproducts**: Create and retrieve subproducts. Filter subproducts by name and associate them with subcategories and products.
- **SelectData**: Create and retrieve SelectData objects that link products, subcategories, and subproducts.

## API Endpoints

### Products
- **GET** `/products/`: Get all products.
- **GET** `/products/filter/`: Filter products by name (`name` query parameter).
- **POST** `/products/`: Create a new product.

### Subcategories
- **GET** `/subcategories/`: Get all subcategories.
- **GET** `/subcategories/{productId}/`: Get all subcategories associated with a specific product by `productId`.
- **GET** `/subcategories/filter/`: Filter subcategories by name (`name` query parameter).
- **POST** `/subcategories/`: Create a new subcategory.

### Subproducts
- **GET** `/subproducts/`: Get all subproducts.
- **GET** `/subproducts/{subCategoryId}/`: Get all subproducts associated with a specific subcategory by `subCategoryId`.
- **GET** `/subproducts/filter/`: Filter subproducts by name (`name` query parameter).
- **POST** `/subproducts/`: Create a new subproduct.

### SelectData
- **GET** `/selectdata/`: Get all SelectData objects.
- **POST** `/selectdata/`: Create a new SelectData object linking products, subcategories, and subproducts.

## Technologies

- **Django**: A web framework for Python.
- **Django REST Framework**: Extension for building RESTful APIs in Django.
- **Python 3.x**: Programming language.
- **SQLite** (default, can be configured to use PostgreSQL or other DBMS).

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/Taday97/my-django-project.git
cd my-django-project
