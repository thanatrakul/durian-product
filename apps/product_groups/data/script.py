
import csv

from .models import ProductGroup

with open("apps/product_groups/data/product_group_masterdata.csv") as f:

    reader = csv.reader(f)
    for row in reader:
        _, created = ProductGroup.objects.get_or_create(
            name=row[0],
            mms_id=int(row[1]),
            lms_id=int(row[2]),
            slug="-".join(row[0].split(" ").lower())
        )
