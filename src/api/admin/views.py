from sqladmin import ModelView
from src.infrastructure.database.models import User, Category, Product


class UserAdmin(ModelView, model=User):
    column_list = [User.id, User.email, User.phone_number, User.first_name, User.last_name, User.access_level, User.date_created]
    column_details_exclude_list = [User.password_hash]
    can_delete = False
    name = "User"
    name_plural = "Users"
    icon = "fa-solid fa-user"


class CategoryAdmin(ModelView, model=Category):
    column_list = [Category.id, Category.name, Category.description]
    name = "Category"
    name_plural = "Categories"
    icon = "fa-solid fa-user"


class ProductAdmin(ModelView, model=Product):
    column_list = [Product.id, Product.name, Product.description, Product.price, Product.quantity, Product.category_id, Product.category]
    name = "Product"
    name_plural = "Products"
    icon = "fa-solid fa-user"
