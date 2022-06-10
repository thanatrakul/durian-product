from apps.lms.models import ProductsProduct
from apps.product_types.choices import ProductTypeChoice
from apps.products.choices import ProductGroupChoice
from apps.products.choices import ProductStatusChoice
from apps.products.choices import ProductTaxTypeChoice
from apps.products.forms import ProductForm
from apps.products.models import Product
from apps.users.models import User


lms_products = ProductsProduct.objects.all()

for data in lms_products:

    # Get Admin User
    admin_user = User.objects.get(username="bigadmin")

    data = {
        "id": data.id,
        "slug": data.slug,
        "name": data.name,
        "description": data.description_seo,
        "sku_code": data.id,
        "lagacy_sku": data.id,
        "tax": ProductTaxTypeChoice.EXCLUDE_VAT,
        "status": ProductStatusChoice.DRAFT,
        "product_type": ProductTypeChoice.COURSE,
        "product_group": ProductGroupChoice.TYPE_A,
        "created_user": admin_user,
        "updated_user": admin_user
    }

    Product.objects.create(**data)

    # form = ProductForm(data=data)
    # if form.is_valid():
    #     print("*" * 50, "Form Valid")
    #     form["created_user"] = admin_user
    #     form["updated_user"] = admin_user
    #     form.save()
    # else:
    #     print("*" * 50, "Form Invalid". form.errors)
