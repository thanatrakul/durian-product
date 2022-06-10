from apps.commons.managers.lms import LMSRawDataManager
from django.db import models


class AboutUsAdvisors(models.Model):
    fullname = models.CharField(unique=True, max_length=200)
    role = models.CharField(unique=True, max_length=200)
    profile_image = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'about_us_advisors'


class AboutUsBanner(models.Model):
    banner_name = models.CharField(max_length=100)
    banner_image = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'about_us_banner'


class AboutUsContent(models.Model):
    details = models.TextField(blank=True, null=True)
    columns = models.IntegerField()
    rows = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'about_us_content'


class AboutUsGallery(models.Model):
    images = models.CharField(max_length=100)
    info = models.ForeignKey('AboutUsInfo', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'about_us_gallery'


class AboutUsInfo(models.Model):
    map_token = models.TextField()
    address = models.TextField()

    class Meta:
        managed = False
        db_table = 'about_us_info'


class AboutUsPartnerships(models.Model):
    partnership_name = models.CharField(unique=True, max_length=100)
    partnership_image = models.ForeignKey('FilerImage', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'about_us_partnerships'


class AboutUsPhone(models.Model):
    phone_description = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=30)
    info = models.ForeignKey(AboutUsInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'about_us_phone'


class AboutUsRole(models.Model):
    name_role = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'about_us_role'


class AboutUsSocialmedia(models.Model):
    name = models.CharField(unique=True, max_length=100)
    image = models.CharField(max_length=100)
    link = models.CharField(unique=True, max_length=200)
    info = models.ForeignKey(AboutUsInfo, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'about_us_socialmedia'


class AboutUsStaff(models.Model):
    fullname = models.CharField(unique=True, max_length=200)
    profile_image = models.ForeignKey('FilerImage', models.DO_NOTHING, blank=True, null=True, related_name="+")
    role = models.ForeignKey(AboutUsRole, models.DO_NOTHING)
    seq = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'about_us_staff'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.BooleanField()
    primary = models.BooleanField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


class AccountingsBank(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=150)
    logo = models.CharField(max_length=100)
    icon = models.CharField(max_length=100)
    swift_code = models.CharField(max_length=25)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'accountings_bank'


class AccountingsBankaccount(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=150)
    branch = models.CharField(max_length=150)
    ac_name = models.CharField(max_length=150)
    ac_number = models.CharField(max_length=50)
    ac_type = models.SmallIntegerField()
    remark = models.TextField()
    qr_code = models.CharField(max_length=100, blank=True, null=True)
    bank = models.ForeignKey(AccountingsBank, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'accountings_bankaccount'


class AccountingsBilling(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    bill_id = models.CharField(unique=True, max_length=255)
    bill_type = models.SmallIntegerField()
    balance_type = models.SmallIntegerField()
    bill_data = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'accountings_billing'


class AccountingsSms(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    date = models.DateField()
    time = models.TimeField()
    order = models.IntegerField()
    balance = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'accountings_sms'


class AdvertisementsAdvertising(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    utm_source = models.CharField(max_length=255)
    utm_medium = models.CharField(max_length=255)
    utm_campaign = models.CharField(max_length=255)
    utm_term = models.CharField(max_length=255, blank=True, null=True)
    utm_content = models.CharField(max_length=255, blank=True, null=True)
    web_url = models.CharField(max_length=200)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    desktop = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'advertisements_advertising'


class AssetsFilemedialibrary(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    media_file = models.CharField(max_length=100, blank=True, null=True)
    media_size = models.DecimalField(max_digits=10, decimal_places=2)
    thumbnail_desktop = models.CharField(max_length=100, blank=True, null=True)
    thumbnail_mobile = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'assets_filemedialibrary'


class AssetsMedialibrary(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    media_source = models.SmallIntegerField()
    media_type = models.SmallIntegerField()
    media_file = models.CharField(max_length=100, blank=True, null=True)
    s3_key = models.CharField(max_length=255, blank=True, null=True)
    youtube_id = models.CharField(max_length=255, blank=True, null=True)
    has_local_cdn = models.BooleanField()
    duration = models.SmallIntegerField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    media_size = models.DecimalField(max_digits=10, decimal_places=2)
    media_player_color = models.CharField(max_length=10)
    thumbnail_desktop = models.CharField(max_length=100, blank=True, null=True)
    thumbnail_mobile = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'assets_medialibrary'


class AssetsVideomedialibrary(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    media_source = models.SmallIntegerField()
    media_file = models.CharField(max_length=100, blank=True, null=True)
    s3_key = models.CharField(max_length=255)
    youtube_id = models.CharField(max_length=255, blank=True, null=True)
    has_local_cdn = models.BooleanField()
    duration = models.SmallIntegerField()
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    media_size = models.DecimalField(max_digits=10, decimal_places=2)
    media_player_color = models.CharField(max_length=10)
    thumbnail_desktop = models.CharField(max_length=100, blank=True, null=True)
    thumbnail_mobile = models.CharField(max_length=100, blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'assets_videomedialibrary'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthorsAuthor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    alias = models.CharField(max_length=100)
    photo = models.CharField(max_length=100, blank=True, null=True)
    author_user = models.OneToOneField('UsersUser', models.DO_NOTHING, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'authors_author'


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField('UsersUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class B2BCompany(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name_th = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    company_logo = models.CharField(max_length=100, blank=True, null=True)
    tel = models.CharField(max_length=10, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'b2b_company'


class B2BCompanyEmployee(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    employee_id = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    company = models.ForeignKey(B2BCompany, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'b2b_company_employee'


class B2BOrderB2B(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    total_user = models.IntegerField(blank=True, null=True)
    company = models.ForeignKey(B2BCompany, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'b2b_order_b2b'


class B2BOrderCompanyProduct(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    total_user = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(B2BOrderB2B, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    company = models.ForeignKey(B2BCompany, models.DO_NOTHING, blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'b2b_order_company_product'


class B2BPrePostEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    time = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enrollment = models.ForeignKey('EnrollmentsEnrollment', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    simulation_enrollment = models.ForeignKey('EnrollmentsSimulationEnrollment', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'b2b_pre_post_enrollment'


class CouponsBulkCouponMapper(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    bulk_coupon = models.ForeignKey('CouponsBulkGenerateCoupon', models.DO_NOTHING)
    coupon = models.ForeignKey('CouponsCoupon', models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'coupons_bulk_coupon_mapper'


class CouponsBulkGenerateCoupon(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=4)
    status = models.SmallIntegerField()
    remark = models.TextField(blank=True, null=True)
    total_code = models.IntegerField()
    generate_log = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    profile_template = models.ForeignKey('DurianfromsFromTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons_bulk_generate_coupon'


class CouponsClaimedCouponItem(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    log = models.TextField(blank=True, null=True)
    coupon = models.ForeignKey('CouponsCoupon', models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    item_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'coupons_claimed_coupon_item'


class CouponsCoupon(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=4)
    status = models.SmallIntegerField()
    remark = models.TextField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=14)
    claimed_user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    profile_data = models.ForeignKey('DurianfromsData', models.DO_NOTHING, blank=True, null=True)
    profile_template = models.ForeignKey('DurianfromsFromTemplate', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons_coupon'


class CoursesCourse(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    version = models.CharField(max_length=255)
    other = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'courses_course'


class CoursesLesson(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    other = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    syllabus = models.ForeignKey('CoursesSyllabus', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    document = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses_lesson'


class CoursesLessoncontent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content_id = models.IntegerField()
    other = models.JSONField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson = models.ForeignKey(CoursesLesson, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'courses_lessoncontent'


class CoursesSyllabus(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    has_free_content = models.BooleanField()
    document = models.CharField(max_length=100, blank=True, null=True)
    total_video_length = models.IntegerField()
    total_exercise_count = models.IntegerField()
    other = models.JSONField()
    course = models.ForeignKey(CoursesCourse, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'courses_syllabus'


class CoursesVideo(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_free = models.BooleanField()
    title = models.CharField(max_length=255)
    video_length = models.SmallIntegerField()
    size = models.IntegerField()
    file = models.CharField(max_length=100, blank=True, null=True)
    s3_path = models.CharField(max_length=255, blank=True, null=True)
    cdn_path = models.CharField(max_length=255, blank=True, null=True)
    url = models.TextField(blank=True, null=True)
    generate_url = models.BooleanField()
    cover_image = models.CharField(max_length=100, blank=True, null=True)
    other = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    cdn_durian = models.TextField(blank=True, null=True)
    generate_cdn_durian = models.BooleanField()
    is_ready_cdn_durian = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'courses_video'


class CoursesVideoPolicies(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    enable_s3 = models.BooleanField()
    enable_cdn_inet = models.BooleanField()
    enable_cdn_durian = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'courses_video_policies'


class CoursesVideocdnconvertjob(models.Model):
    job_ref = models.CharField(max_length=255)
    status = models.SmallIntegerField()
    raw_request = models.TextField(blank=True, null=True)
    raw_response = models.TextField(blank=True, null=True)
    video = models.ForeignKey(CoursesVideo, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses_videocdnconvertjob'


class DashboardDashboard(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_dashboard'


class DashboardDashboardType(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content_id = models.IntegerField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    dashboard = models.ForeignKey(DashboardDashboard, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_dashboard_type'


class DashboardItemCollection(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    max_score = models.FloatField(blank=True, null=True)
    require_score = models.FloatField(blank=True, null=True)
    icon_image = models.CharField(max_length=100, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    item_group = models.ForeignKey('DashboardItemCollectionGroup', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_item_collection'


class DashboardItemCollectionGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_item_collection_group'


class DashboardLevel(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    icon_image = models.CharField(max_length=100, blank=True, null=True)
    background_image = models.CharField(max_length=100, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    level_group = models.ForeignKey('DashboardLevelGroup', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_level'


class DashboardLevelGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_level_group'


class DashboardLevelRequire(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    level = models.ForeignKey(DashboardLevel, models.DO_NOTHING)
    level_require = models.ForeignKey(DashboardLevel, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_level_require'


class DashboardLevelSyllabus(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    level = models.ForeignKey(DashboardLevel, models.DO_NOTHING)
    syllabus = models.ForeignKey('GadgetsSyllabus', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_level_syllabus'


class DashboardRequireContent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content = models.ForeignKey('GadgetsContent', models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    item = models.ForeignKey(DashboardItemCollection, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_require_content'


class DashboardSkill(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(unique=True, max_length=200)
    max_score = models.FloatField(blank=True, null=True)
    icon_image = models.CharField(max_length=100, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    skill_group = models.ForeignKey('DashboardSkillGroup', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_skill'


class DashboardSkillGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'dashboard_skill_group'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoCeleryBeatClockedschedule(models.Model):
    clocked_time = models.DateTimeField()
    enabled = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_clockedschedule'


class DjangoCeleryBeatCrontabschedule(models.Model):
    minute = models.CharField(max_length=240)
    hour = models.CharField(max_length=96)
    day_of_week = models.CharField(max_length=64)
    day_of_month = models.CharField(max_length=124)
    month_of_year = models.CharField(max_length=64)
    timezone = models.CharField(max_length=63)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_crontabschedule'


class DjangoCeleryBeatIntervalschedule(models.Model):
    every = models.IntegerField()
    period = models.CharField(max_length=24)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_intervalschedule'


class DjangoCeleryBeatPeriodictask(models.Model):
    name = models.CharField(unique=True, max_length=200)
    task = models.CharField(max_length=200)
    args = models.TextField()
    kwargs = models.TextField()
    queue = models.CharField(max_length=200, blank=True, null=True)
    exchange = models.CharField(max_length=200, blank=True, null=True)
    routing_key = models.CharField(max_length=200, blank=True, null=True)
    expires = models.DateTimeField(blank=True, null=True)
    enabled = models.BooleanField()
    last_run_at = models.DateTimeField(blank=True, null=True)
    total_run_count = models.IntegerField()
    date_changed = models.DateTimeField()
    description = models.TextField()
    crontab = models.ForeignKey(DjangoCeleryBeatCrontabschedule, models.DO_NOTHING, blank=True, null=True)
    interval = models.ForeignKey(DjangoCeleryBeatIntervalschedule, models.DO_NOTHING, blank=True, null=True)
    solar = models.ForeignKey('DjangoCeleryBeatSolarschedule', models.DO_NOTHING, blank=True, null=True)
    one_off = models.BooleanField()
    start_time = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)
    headers = models.TextField()
    clocked = models.ForeignKey(DjangoCeleryBeatClockedschedule, models.DO_NOTHING, blank=True, null=True)
    expire_seconds = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictask'


class DjangoCeleryBeatPeriodictasks(models.Model):
    ident = models.SmallIntegerField(primary_key=True)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_celery_beat_periodictasks'


class DjangoCeleryBeatSolarschedule(models.Model):
    event = models.CharField(max_length=24)
    latitude = models.DecimalField(max_digits=9, decimal_places=6)
    longitude = models.DecimalField(max_digits=9, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'django_celery_beat_solarschedule'
        unique_together = (('event', 'latitude', 'longitude'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class DurianfromsData(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    data = models.JSONField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    form_template = models.ForeignKey('DurianfromsFromTemplate', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'durianfroms_data'


class DurianfromsFormField(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    field_name = models.CharField(max_length=255)
    field_type = models.SmallIntegerField()
    choices = models.TextField(blank=True, null=True)  # This field type is a guess.
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    template = models.ForeignKey('DurianfromsFromTemplate', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    multiple = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'durianfroms_form_field'


class DurianfromsFromTemplate(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'durianfroms_from_template'


class DurianpolicyDurianpolicy(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    type_policy = models.SmallIntegerField()
    data_policy = models.TextField(blank=True, null=True)
    version = models.CharField(max_length=10)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'durianpolicy_durianpolicy'


class EasyThumbnailsSource(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_source'
        unique_together = (('storage_hash', 'name'),)


class EasyThumbnailsThumbnail(models.Model):
    storage_hash = models.CharField(max_length=40)
    name = models.CharField(max_length=255)
    modified = models.DateTimeField()
    source = models.ForeignKey(EasyThumbnailsSource, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnail'
        unique_together = (('storage_hash', 'name', 'source'),)


class EasyThumbnailsThumbnaildimensions(models.Model):
    thumbnail = models.OneToOneField(EasyThumbnailsThumbnail, models.DO_NOTHING)
    width = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'easy_thumbnails_thumbnaildimensions'


class EnrollmentsActivateFromEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    course_enrollment = models.ForeignKey('EnrollmentsCourseEnrollment', models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enrollment = models.ForeignKey('EnrollmentsEnrollment', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_activate_from_enrollment'


class EnrollmentsCourseEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    is_activated = models.BooleanField()
    activated_at = models.DateTimeField(blank=True, null=True)
    active_status = models.SmallIntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    life_time_limit = models.IntegerField(blank=True, null=True)
    has_learned = models.BooleanField()
    remark = models.TextField(blank=True, null=True)
    bandwidth = models.DecimalField(max_digits=8, decimal_places=2)
    bandwidth_limit = models.IntegerField()
    other = models.JSONField()
    course = models.ForeignKey(CoursesCourse, models.DO_NOTHING, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_course_enrollment'


class EnrollmentsEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    expiration_date = models.DateTimeField(blank=True, null=True)
    is_activated = models.BooleanField()
    activated_at = models.DateTimeField(blank=True, null=True)
    active_status = models.SmallIntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    life_time_limit = models.IntegerField(blank=True, null=True)
    is_welcome = models.BooleanField()
    is_verified = models.BooleanField()
    other = models.JSONField()
    remark = models.TextField(blank=True, null=True)
    base_enrollment = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_enrollment'


class EnrollmentsEnrollmentCourseEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    course_enrollment = models.ForeignKey(EnrollmentsCourseEnrollment, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enrollment = models.ForeignKey(EnrollmentsEnrollment, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_enrollment_course_enrollment'


class EnrollmentsGadgetEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    remark = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    gadget = models.ForeignKey('GadgetsGadget', models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    durianform_data = models.ForeignKey(DurianfromsData, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enrollments_gadget_enrollment'


class EnrollmentsGadgetExamEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    ticket_id = models.CharField(unique=True, max_length=10, blank=True, null=True)
    status = models.SmallIntegerField()
    answer_sheet = models.JSONField(blank=True, null=True)
    summary = models.JSONField(blank=True, null=True)
    time_limit = models.IntegerField(blank=True, null=True)
    time_spend = models.IntegerField()
    score = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    pause_limit = models.IntegerField(blank=True, null=True)
    pause_count = models.IntegerField()
    start_at = models.DateTimeField(blank=True, null=True)
    submit_at = models.DateTimeField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    gadget_enrollment = models.ForeignKey(EnrollmentsGadgetEnrollment, models.DO_NOTHING)
    gadget_exam = models.ForeignKey('GadgetsGadgetExam', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_gadget_exam_enrollment'


class EnrollmentsLearningRecord(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson_content = models.ForeignKey(CoursesLessoncontent, models.DO_NOTHING)
    lesson_record = models.ForeignKey('EnrollmentsLessonRecord', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_learning_record'


class EnrollmentsLearningRecordLog(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson_content = models.ForeignKey(CoursesLessoncontent, models.DO_NOTHING)
    lesson_record = models.ForeignKey('EnrollmentsLessonRecordLog', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_learning_record_log'
        unique_together = (('lesson_record', 'lesson_content', 'content_type', 'content_id'),)


class EnrollmentsLessonRecord(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson = models.ForeignKey(CoursesLesson, models.DO_NOTHING)
    syllabus_record = models.ForeignKey('EnrollmentsSyllabusRecord', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_lesson_record'


class EnrollmentsLessonRecordLog(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson = models.ForeignKey(CoursesLesson, models.DO_NOTHING)
    syllabus_record = models.ForeignKey('EnrollmentsSyllabusRecordLog', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_lesson_record_log'
        unique_together = (('syllabus_record', 'lesson'),)


class EnrollmentsSimulationEnrollment(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    ticket_id = models.CharField(unique=True, max_length=8, blank=True, null=True)
    answer_json = models.JSONField()
    summary_json = models.JSONField()
    package_time = models.IntegerField()
    spend_time = models.IntegerField()
    pause_count = models.SmallIntegerField()
    score = models.DecimalField(max_digits=8, decimal_places=2)
    started_at = models.DateTimeField(blank=True, null=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    max_pause_allow = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    package = models.ForeignKey('SimulationsPackage', models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    simulation = models.ForeignKey('SimulationsSimulation', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    wrong_answers_json = models.JSONField()

    class Meta:
        managed = False
        db_table = 'enrollments_simulation_enrollment'


class EnrollmentsSyllabusRecord(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    course_enrollment = models.ForeignKey(EnrollmentsCourseEnrollment, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    syllabus = models.ForeignKey(CoursesSyllabus, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_syllabus_record'


class EnrollmentsSyllabusRecordLog(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    progress = models.DecimalField(max_digits=5, decimal_places=2)
    course_enrollment = models.ForeignKey(EnrollmentsCourseEnrollment, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    syllabus = models.ForeignKey(CoursesSyllabus, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'enrollments_syllabus_record_log'
        unique_together = (('course_enrollment', 'syllabus'),)


class ExaminationsAnswerchoice(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    caption = models.TextField()
    caption_image = models.CharField(max_length=100, blank=True, null=True)
    is_correct = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey('ExaminationsExercise', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_answerchoice'


class ExaminationsAnswerfill(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    before_label = models.CharField(max_length=255, blank=True, null=True)
    answer = models.CharField(max_length=255)
    post_label = models.CharField(max_length=255, blank=True, null=True)
    force_numeric = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey('ExaminationsExercise', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_answerfill'


class ExaminationsExam(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    advertising_enable = models.BooleanField()
    advertising_display = models.SmallIntegerField()
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255, blank=True, null=True)
    intro = models.TextField(blank=True, null=True)
    home_ranking = models.IntegerField(blank=True, null=True)
    is_free = models.BooleanField()
    exercise_language = models.SmallIntegerField()
    description = models.TextField()
    difficulty = models.SmallIntegerField()
    cover_desktop = models.CharField(max_length=100, blank=True, null=True)
    cover_mobile = models.CharField(max_length=100, blank=True, null=True)
    other = models.JSONField()
    title_seo = models.TextField()
    author = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_exam'


class ExaminationsExamAdvertisings(models.Model):
    exam = models.ForeignKey(ExaminationsExam, models.DO_NOTHING)
    advertising = models.ForeignKey(AdvertisementsAdvertising, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examinations_exam_advertisings'
        unique_together = (('exam', 'advertising'),)


class ExaminationsExamClassifications(models.Model):
    exam = models.ForeignKey(ExaminationsExam, models.DO_NOTHING)
    classification = models.ForeignKey('PublicationsClassification', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examinations_exam_classifications'
        unique_together = (('exam', 'classification'),)


class ExaminationsExamauthor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exam = models.ForeignKey(ExaminationsExam, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_examauthor'
        unique_together = (('exam', 'author'),)


class ExaminationsExamexercise(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exam = models.ForeignKey(ExaminationsExam, models.DO_NOTHING)
    exercise = models.ForeignKey('ExaminationsExercise', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_examexercise'
        unique_together = (('exam', 'exercise'),)


class ExaminationsExamsubjectrelated(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exam = models.ForeignKey(ExaminationsExam, models.DO_NOTHING)
    subject = models.ForeignKey('PublicationsClassification', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_examsubjectrelated'
        unique_together = (('exam', 'subject'),)


class ExaminationsExercise(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    difficulty = models.SmallIntegerField()
    question = models.TextField()
    answer = models.TextField()
    answer_type = models.SmallIntegerField()
    hint = models.TextField(blank=True, null=True)
    remark = models.TextField()
    score_value = models.DecimalField(max_digits=5, decimal_places=2)
    multiple_choice = models.BooleanField()
    other = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    render_mathjax = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'examinations_exercise'


class ExaminationsExerciseChapters(models.Model):
    exercise = models.ForeignKey(ExaminationsExercise, models.DO_NOTHING)
    classification = models.ForeignKey('PublicationsClassification', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examinations_exercise_chapters'
        unique_together = (('exercise', 'classification'),)


class ExaminationsExerciseClassifications(models.Model):
    exercise = models.ForeignKey(ExaminationsExercise, models.DO_NOTHING)
    classification = models.ForeignKey('PublicationsClassification', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examinations_exercise_classifications'
        unique_together = (('exercise', 'classification'),)


class ExaminationsExercisemediaquestion(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey(ExaminationsExercise, models.DO_NOTHING)
    media = models.ForeignKey(AssetsMedialibrary, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'examinations_exercisemediaquestion'


class ExaminationsExercisevideoanswer(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    free_video = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey(ExaminationsExercise, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    video = models.ForeignKey(AssetsVideomedialibrary, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examinations_exercisevideoanswer'


class ExaminationsExercisewikipedia(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey(ExaminationsExercise, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    wikipedia = models.ForeignKey('WikipediasWikipedia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'examinations_exercisewikipedia'
        unique_together = (('exercise', 'wikipedia'),)


class ExtensionSlackpricinglogs(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    channel = models.CharField(max_length=20)
    ts = models.CharField(max_length=50)
    pricing_type_id = models.IntegerField()
    pricing_id = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'extension_slackpricinglogs'


class FaqsFaq(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    show = models.BooleanField()
    question = models.TextField()
    answer = models.TextField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'faqs_faq'


class FilerClipboard(models.Model):
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'filer_clipboard'


class FilerClipboarditem(models.Model):
    clipboard = models.ForeignKey(FilerClipboard, models.DO_NOTHING)
    file = models.ForeignKey('FilerFile', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'filer_clipboarditem'


class FilerFile(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)
    field_file_size = models.BigIntegerField(db_column='_file_size', blank=True, null=True)  # Field renamed because it started with '_'.
    sha1 = models.CharField(max_length=40)
    has_all_mandatory_data = models.BooleanField()
    original_filename = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    uploaded_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    is_public = models.BooleanField()
    folder = models.ForeignKey('FilerFolder', models.DO_NOTHING, blank=True, null=True)
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    polymorphic_ctype = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    mime_type = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'filer_file'


class FilerFolder(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField()
    created_at = models.DateTimeField()
    modified_at = models.DateTimeField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    owner = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'filer_folder'
        unique_together = (('parent', 'name'),)


class FilerFolderpermission(models.Model):
    type = models.SmallIntegerField()
    everybody = models.BooleanField()
    can_edit = models.SmallIntegerField(blank=True, null=True)
    can_read = models.SmallIntegerField(blank=True, null=True)
    can_add_children = models.SmallIntegerField(blank=True, null=True)
    folder = models.ForeignKey(FilerFolder, models.DO_NOTHING, blank=True, null=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'filer_folderpermission'


class FilerImage(models.Model):
    file_ptr = models.OneToOneField(FilerFile, models.DO_NOTHING, primary_key=True)
    field_height = models.IntegerField(db_column='_height', blank=True, null=True)  # Field renamed because it started with '_'.
    field_width = models.IntegerField(db_column='_width', blank=True, null=True)  # Field renamed because it started with '_'.
    date_taken = models.DateTimeField(blank=True, null=True)
    default_alt_text = models.CharField(max_length=255, blank=True, null=True)
    default_caption = models.CharField(max_length=255, blank=True, null=True)
    author = models.CharField(max_length=255, blank=True, null=True)
    must_always_publish_author_credit = models.BooleanField()
    must_always_publish_copyright = models.BooleanField()
    subject_location = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'filer_image'


class FilerThumbnailoption(models.Model):
    name = models.CharField(max_length=100)
    width = models.IntegerField()
    height = models.IntegerField()
    crop = models.BooleanField()
    upscale = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'filer_thumbnailoption'


class GadgetsContent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content_id = models.IntegerField()
    content_group = models.ForeignKey('GadgetsContentGroup', models.DO_NOTHING)
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'gadgets_content'


class GadgetsContentGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250)
    element_id = models.CharField(max_length=50)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson = models.ForeignKey('GadgetsLesson', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    content_group_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'gadgets_content_group'
        unique_together = (('lesson', 'element_id'),)


class GadgetsFileContent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    file = models.CharField(max_length=100)
    file_type = models.SmallIntegerField()
    title = models.TextField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'gadgets_file_content'


class GadgetsGadget(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250)
    slug = models.CharField(unique=True, max_length=200)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    dashboard = models.ForeignKey(DashboardDashboard, models.DO_NOTHING, blank=True, null=True)
    render_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'gadgets_gadget'


class GadgetsGadgetExam(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    time_limit = models.IntegerField(blank=True, null=True)
    enrol_limit = models.IntegerField(blank=True, null=True)
    can_view_answer = models.BooleanField()
    pause_limit = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    gadget = models.ForeignKey(GadgetsGadget, models.DO_NOTHING)
    simulation = models.ForeignKey('SimulationsSimulation', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    element_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gadgets_gadget_exam'


class GadgetsGadgetExamRequire(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    exam_count = models.IntegerField(blank=True, null=True)
    exam_score = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    gadget_exam = models.ForeignKey(GadgetsGadgetExam, models.DO_NOTHING, related_name="+")
    require_gadget_exam = models.ForeignKey(GadgetsGadgetExam, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'gadgets_gadget_exam_require'


class GadgetsLesson(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250)
    element_id = models.CharField(max_length=50)
    show_content_list = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    syllabus = models.ForeignKey('GadgetsSyllabus', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    lesson_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'gadgets_lesson'
        unique_together = (('syllabus', 'element_id'),)


class GadgetsRichContent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    has_image = models.BooleanField()
    has_video = models.BooleanField()
    rich_content = models.TextField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'gadgets_rich_content'


class GadgetsSyllabus(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=250)
    element_id = models.CharField(max_length=50)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    gadget = models.ForeignKey(GadgetsGadget, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'gadgets_syllabus'
        unique_together = (('gadget', 'element_id'),)


class GadgetsTextContent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'gadgets_text_content'


class HealthCheckDbTestmodel(models.Model):
    title = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'health_check_db_testmodel'


class HomebannersHomebanner(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=100)
    mobile_image = models.CharField(max_length=100, blank=True, null=True)
    to_url = models.CharField(max_length=255, blank=True, null=True)
    alternative_text = models.CharField(max_length=255)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'homebanners_homebanner'


class HometestimonialsHometestimonial(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    order = models.IntegerField()
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=100)
    mobile_image = models.CharField(max_length=100, blank=True, null=True)
    video_url = models.TextField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'hometestimonials_hometestimonial'


class InvoicesInvoice(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    tax_number = models.CharField(max_length=13)
    is_headquarter = models.BooleanField()
    address = models.ForeignKey('UsersAddress', models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.OneToOneField('OrdersOrder', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    address_v2 = models.ForeignKey('UsersAddressversiontwo', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'invoices_invoice'


class LogResponseOdoo(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=255)
    status_code = models.CharField(max_length=30, blank=True, null=True)
    raw_response = models.TextField(blank=True, null=True)
    body = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'log_response_odoo'


class LogsSessionidodoo(models.Model):
    token = models.TextField()

    class Meta:
        managed = False
        db_table = 'logs_sessionidodoo'


class MarketingMarketingChannel(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(unique=True, max_length=50)
    name = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'marketing_marketing_channel'


class MarketingProductgroups(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(unique=True, max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    slack_logo = models.CharField(max_length=255)
    is_active = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'marketing_productgroups'


class MarketingWebMarketingChannel(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    channel = models.ForeignKey(MarketingMarketingChannel, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'marketing_web_marketing_channel'


class NewsGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(unique=True, max_length=255)
    slug = models.CharField(unique=True, max_length=80)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enable = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'news_group'


class NewsNews(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    advertising_enable = models.BooleanField()
    advertising_display = models.SmallIntegerField()
    topic = models.CharField(max_length=255)
    is_pinned = models.BooleanField()
    subtitle = models.TextField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    content = models.TextField(blank=True, null=True)
    desktop_cover = models.CharField(max_length=255, blank=True, null=True)
    mobile_cover = models.CharField(max_length=255, blank=True, null=True)
    classification = models.ForeignKey('PublicationsClassification', models.DO_NOTHING, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'news_news'


class NewsNewsAdvertisings(models.Model):
    news = models.ForeignKey(NewsNews, models.DO_NOTHING)
    advertising = models.ForeignKey(AdvertisementsAdvertising, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'news_news_advertisings'
        unique_together = (('news', 'advertising'),)


class NewsNewsAuthor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    news = models.ForeignKey(NewsNews, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'news_news_author'
        unique_together = (('news', 'user'),)


class NewsNewsGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    group = models.ForeignKey(NewsGroup, models.DO_NOTHING)
    news = models.ForeignKey(NewsNews, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'news_news_group'


class NewsRelateNews(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    news = models.ForeignKey(NewsNews, models.DO_NOTHING, related_name="+")
    relate_news = models.ForeignKey(NewsNews, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'news_relate_news'


class NewsRelateProduct(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    news = models.ForeignKey(NewsNews, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'news_relate_product'


class OrdersOrder(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    payment_method = models.SmallIntegerField(blank=True, null=True)
    sale_status = models.SmallIntegerField()
    is_verified = models.BooleanField()
    pricing_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    discount = models.IntegerField(blank=True, null=True)
    total_price = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    detail = models.TextField(blank=True, null=True)
    is_approve = models.BooleanField()
    approved_at = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    invoice_request = models.BooleanField()
    is_quickpay = models.BooleanField()
    other = models.JSONField()
    chat_link = models.CharField(max_length=255, blank=True, null=True)
    order_id = models.CharField(unique=True, max_length=20, blank=True, null=True)
    order_ref = models.CharField(max_length=255, blank=True, null=True)
    source = models.SmallIntegerField()
    static_address = models.TextField(blank=True, null=True)
    static_invoice_address = models.TextField(blank=True, null=True)
    address = models.ForeignKey('UsersAddress', models.DO_NOTHING, blank=True, null=True, related_name="+")
    approve_by = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enrollment = models.ForeignKey(EnrollmentsEnrollment, models.DO_NOTHING, blank=True, null=True)
    invoice_address = models.ForeignKey('UsersAddress', models.DO_NOTHING, blank=True, null=True, related_name="+")
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    pricing_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    promotion = models.ForeignKey('PromotionsPromotion', models.DO_NOTHING, blank=True, null=True)
    quickpay_link = models.ForeignKey('QuickpayLink', models.DO_NOTHING, blank=True, null=True)
    sale_agent = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    sale_staff = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    simulation_enrollment = models.ForeignKey(EnrollmentsSimulationEnrollment, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    gtm_transaction_collected = models.BooleanField()
    is_fill_acc = models.BooleanField()
    real_transaction = models.BooleanField()
    transaction_date = models.DateTimeField(blank=True, null=True)
    selling_product = models.ForeignKey('SkuSellingproduct', models.DO_NOTHING, blank=True, null=True)
    sms = models.ForeignKey(AccountingsSms, models.DO_NOTHING, blank=True, null=True)
    actual_amount = models.IntegerField()
    address_v2 = models.ForeignKey('UsersAddressversiontwo', models.DO_NOTHING, blank=True, null=True, related_name="+")
    invoice_address_v2 = models.ForeignKey('UsersAddressversiontwo', models.DO_NOTHING, blank=True, null=True, related_name="+")
    marketing_channel = models.ForeignKey(MarketingMarketingChannel, models.DO_NOTHING, blank=True, null=True)
    billing_id = models.CharField(max_length=50, blank=True, null=True)
    billing_status = models.SmallIntegerField(blank=True, null=True)
    selling_product_list = models.JSONField(blank=True, null=True)
    created_status = models.SmallIntegerField()
    bo_id = models.CharField(max_length=50, blank=True, null=True)
    billing_remark = models.CharField(max_length=255, blank=True, null=True)
    bo_status = models.SmallIntegerField()
    token = models.CharField(max_length=255, blank=True, null=True)
    is_durian_order_created = models.BooleanField()
    is_durian_order_updated = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'orders_order'


class OrdersOrderDetail(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField()
    unit_count = models.DecimalField(max_digits=10, decimal_places=2)
    unit_name = models.SmallIntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    item_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'orders_order_detail'


class OrdersOrderExternal(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    order_ref = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    total_revenue = models.FloatField(blank=True, null=True)
    sale_platform = models.SmallIntegerField()
    marketing_channel = models.TextField()
    seller = models.CharField(max_length=255)
    customer_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    shipping_address = models.JSONField()
    invoice_address = models.JSONField(blank=True, null=True)
    total_discount = models.FloatField(blank=True, null=True)
    chat_link = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    invoice_number = models.CharField(max_length=255, blank=True, null=True)
    is_cancelled = models.BooleanField()
    is_paid = models.BooleanField()
    discounts = models.JSONField(blank=True, null=True)
    selling_products = models.JSONField()
    transactions = models.JSONField()
    billing_id = models.CharField(max_length=50, blank=True, null=True)
    billing_remark = models.CharField(max_length=255, blank=True, null=True)
    billing_status = models.SmallIntegerField(blank=True, null=True)
    bo_id = models.CharField(max_length=50, blank=True, null=True)
    bo_status = models.SmallIntegerField()
    status = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'orders_order_external'


class OrdersOrderScoreCard(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    score_card = models.CharField(max_length=100)
    extend_life_time = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'orders_order_score_card'


class PartnershipsAdvisor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    web_url = models.CharField(max_length=200)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.CharField(max_length=100)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'partnerships_advisor'


class PartnershipsPartner(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    web_url = models.CharField(max_length=200)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    partner_type = models.SmallIntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()
    logo = models.CharField(max_length=100)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'partnerships_partner'


class PaymentPoliciesCardPaymentPolicy(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    provider = models.SmallIntegerField()
    fee_detail = models.TextField(blank=True, null=True)
    is_selected = models.BooleanField()
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    icon_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_card_payment_policy'


class PaymentPoliciesInstallmentBank(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    icon_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    panel_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_installment_bank'


class PaymentPoliciesInstallmentProvider(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_selected = models.BooleanField()
    provider = models.SmallIntegerField()
    code = models.CharField(max_length=100, blank=True, null=True)
    customer_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    merchant_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    monthly_min_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    min_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    installment_bank = models.ForeignKey(PaymentPoliciesInstallmentBank, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_installment_provider'


class PaymentPoliciesInstallmentTerm(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    term = models.SmallIntegerField()
    customer_interest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    merchant_interest = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    installment_provider = models.ForeignKey(PaymentPoliciesInstallmentProvider, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    min_amount = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_policies_installment_term'


class PaymentPoliciesInternetBankingBank(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    icon_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    panel_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_internet_banking_bank'


class PaymentPoliciesInternetBankingProvider(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_selected = models.BooleanField()
    service_name = models.CharField(max_length=200, blank=True, null=True)
    provider = models.SmallIntegerField()
    code = models.CharField(max_length=100, blank=True, null=True)
    customer_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    merchant_fee = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    ibanking_bank = models.ForeignKey(PaymentPoliciesInternetBankingBank, models.DO_NOTHING)
    panel_image = models.ForeignKey(FilerImage, models.DO_NOTHING, blank=True, null=True, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_internet_banking_provider'


class PaymentPoliciesPaymentPolicy(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable_transfer_payment = models.BooleanField()
    enable_ibanking_payment = models.BooleanField()
    enable_card_payment = models.BooleanField()
    enable_installment_payment = models.BooleanField()
    enable_qr_payment = models.BooleanField()
    enable_counter_service = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_payment_policy'


class PaymentPoliciesProductInstallmentBank(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    terms = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    installment_bank = models.ForeignKey(PaymentPoliciesInstallmentBank, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_product_installment_bank'


class PaymentPoliciesQrCodePaymentPolicy(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    provider = models.SmallIntegerField()
    fee_detail = models.TextField(blank=True, null=True)
    is_selected = models.BooleanField()
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    icon_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_qr_code_payment_policy'


class PaymentPoliciesTransferAccountAllowed(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    bank_account = models.ForeignKey(AccountingsBankaccount, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payment_policies_transfer_account_allowed'
        unique_together = (('product', 'bank_account'),)


class PaymentsPaymenttransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    transaction_method = models.SmallIntegerField()
    transaction_date = models.DateTimeField()
    total_revenue = models.DecimalField(max_digits=9, decimal_places=2)
    tax = models.DecimalField(max_digits=9, decimal_places=2)
    detail = models.TextField(blank=True, null=True)
    transaction_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    transaction_content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'payments_paymenttransaction'


class PricingsPackageList(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    benefit = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    dummy_price = models.IntegerField(blank=True, null=True)
    lifetime_limit = models.SmallIntegerField(blank=True, null=True)
    dummy_lifetime_limit = models.SmallIntegerField(blank=True, null=True)
    banner = models.ForeignKey(FilerImage, models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    prices = models.DecimalField(max_digits=10, decimal_places=2)
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    cost_of_product = models.DecimalField(max_digits=10, decimal_places=2)
    discount_main_product = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    prices_total = models.DecimalField(max_digits=10, decimal_places=2)
    is_purchase = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pricings_package_list'


class PricingsPackageListGiveaway(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    lifetime_limit = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    package = models.ForeignKey(PricingsPackageList, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    simulation_package = models.ForeignKey('PricingsSimulationPackageList', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prices_total = models.DecimalField(max_digits=10, decimal_places=2)
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    cost_of_product = models.DecimalField(max_digits=10, decimal_places=2)
    discount_giveaway_product = models.DecimalField(max_digits=10, decimal_places=2)
    is_giveaway = models.BooleanField()
    order_billing = models.IntegerField()
    order_website = models.IntegerField()
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'pricings_package_list_giveaway'


class PricingsQuickpayProductManualPrice(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    lifetime_limit = models.IntegerField()
    price = models.IntegerField()
    has_book = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'pricings_quickpay_product_manual_price'


class PricingsQuickpayProductManualPriceGiveaway(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    lifetime_limit = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    manual_price = models.ForeignKey(PricingsQuickpayProductManualPrice, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    simulation_package = models.ForeignKey('PricingsSimulationPackageList', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'pricings_quickpay_product_manual_price_giveaway'


class PricingsSimulationPackageList(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)
    dummy_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    benefit = models.TextField()
    max_pause_allow = models.IntegerField(blank=True, null=True)
    time = models.IntegerField()
    banner = models.ForeignKey(FilerImage, models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    simulation_package = models.ForeignKey('SimulationsPackage', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    is_purchase = models.BooleanField()
    acc_name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricings_simulation_package_list'


class PricingsSinglePrice(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField()
    price = models.IntegerField(blank=True, null=True)
    dummy_price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    lifetime_limit = models.SmallIntegerField(blank=True, null=True)
    dummy_lifetime_limit = models.SmallIntegerField(blank=True, null=True)
    banner = models.ForeignKey(FilerImage, models.DO_NOTHING, blank=True, null=True, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    prices = models.IntegerField()
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    is_purchase = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'pricings_single_price'


class PricingsSinglePriceGiveaway(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    lifetime_limit = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    price = models.ForeignKey(PricingsSinglePrice, models.DO_NOTHING)
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    simulation_package = models.ForeignKey(PricingsSimulationPackageList, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    prices = models.DecimalField(max_digits=10, decimal_places=2)
    prices_total = models.DecimalField(max_digits=10, decimal_places=2)
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pricings_single_price_giveaway'


class ProductsBadge(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_badge'


class ProductsCardCoverImage(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_default = models.BooleanField()
    image = models.CharField(max_length=255)
    mobile_image = models.CharField(max_length=255, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_card_cover_image'


class ProductsCategory(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_category'


class ProductsFeatureImage(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255)
    mobile_image = models.CharField(max_length=255, blank=True, null=True)
    show_text = models.BooleanField()
    text = models.TextField()
    text_color = models.CharField(max_length=255)
    row_group = models.SmallIntegerField()
    to_url = models.TextField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_feature_image'


class ProductsLandingCoverImage(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_schedule = models.BooleanField()
    show_on_landing = models.BooleanField()
    show_on_wall = models.BooleanField()
    image = models.CharField(max_length=255)
    mobile_image = models.CharField(max_length=255)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_landing_cover_image'


class ProductsLandingImage(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    mobile_image = models.CharField(max_length=255, blank=True, null=True)
    youtube_url = models.CharField(max_length=255, blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    caption = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey('ProductsProduct', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_landing_image'


class ProductsProduct(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    enable = models.BooleanField()
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    advertising_enable = models.BooleanField()
    advertising_display = models.SmallIntegerField()
    enable_transfer_payment = models.BooleanField()
    enable_ibanking_payment = models.BooleanField()
    enable_card_payment = models.BooleanField()
    enable_installment_payment = models.BooleanField()
    enable_qr_payment = models.BooleanField()
    enable_counter_service = models.BooleanField()
    name = models.CharField(max_length=255)
    title_seo = models.TextField()
    description_seo = models.TextField()
    sub_title = models.TextField()
    sku = models.CharField(max_length=255, blank=True, null=True)
    trademark = models.SmallIntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    home_page_ranking = models.IntegerField()
    list_page_ranking = models.IntegerField()
    product_type = models.SmallIntegerField()
    product_detail_landing = models.TextField(blank=True, null=True)
    product_detail_wall = models.TextField(blank=True, null=True)
    refund_days = models.SmallIntegerField()
    product_benefit = models.TextField(blank=True, null=True)
    product_suitable = models.TextField(blank=True, null=True)
    facebook_page = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=50, blank=True, null=True)
    allow_individual_activate = models.BooleanField()
    enable_package = models.BooleanField()
    bandwidth_limit = models.IntegerField()
    other = models.JSONField()
    pricing_type = models.SmallIntegerField()
    pricing_countdown_start = models.DateTimeField(blank=True, null=True)
    pricing_countdown_end = models.DateTimeField(blank=True, null=True)
    pedigree = models.CharField(max_length=1025, blank=True, null=True)
    price = models.IntegerField()
    brand = models.CharField(max_length=70)
    alias_slug_1 = models.CharField(max_length=50, blank=True, null=True)
    alias_slug_2 = models.CharField(max_length=50, blank=True, null=True)
    premium_type = models.SmallIntegerField()
    has_guarantee = models.BooleanField()
    guarantee_detail = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    bill_type = models.SmallIntegerField()
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    unit = models.SmallIntegerField(blank=True, null=True)
    vat = models.BooleanField()
    dimension_border = models.DecimalField(max_digits=10, decimal_places=2)
    dimension_length = models.DecimalField(max_digits=10, decimal_places=2)
    dimension_weight = models.DecimalField(max_digits=10, decimal_places=2)
    dimension_width = models.DecimalField(max_digits=10, decimal_places=2)
    cost_of_product = models.DecimalField(max_digits=10, decimal_places=2)
    acc_name = models.CharField(max_length=255, blank=True, null=True)
    pdf_preview = models.CharField(max_length=100, blank=True, null=True)
    product_property = models.JSONField(blank=True, null=True)
    rating_score = models.DecimalField(max_digits=3, decimal_places=2)
    product_property_template = models.ForeignKey('ProductsProductPropertyTemplate', models.DO_NOTHING, blank=True, null=True)
    is_full_page = models.BooleanField()
    product_banner_wall = models.CharField(max_length=255, blank=True, null=True)
    product_banner_wall_mobile = models.CharField(max_length=255, blank=True, null=True)
    can_be_purchased = models.BooleanField()
    is_active = models.BooleanField()
    isbn = models.CharField(max_length=255, blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    package_size = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    shopee_description = models.TextField(blank=True, null=True)
    thickness = models.FloatField(blank=True, null=True)
    warehouse_product_type = models.SmallIntegerField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    width = models.FloatField(blank=True, null=True)
    barcode = models.CharField(max_length=255, blank=True, null=True)
    is_sale = models.BooleanField()

    objects = LMSRawDataManager()

    class Meta:
        managed = False
        db_table = 'products_product'


class ProductsProductAdvertisings(models.Model):
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    advertising = models.ForeignKey(AdvertisementsAdvertising, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products_product_advertisings'
        unique_together = (('product', 'advertising'),)


class ProductsProductBadge(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    badge = models.ForeignKey(ProductsBadge, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_badge'


class ProductsProductCategory(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(ProductsCategory, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_category'
        unique_together = (('product', 'category'),)


class ProductsProductItem(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_item'


class ProductsProductOwner(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    manageable = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    instructor = models.ForeignKey('UsersInstructor', models.DO_NOTHING)
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_owner'


class ProductsProductPropertyField(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    field_name = models.CharField(max_length=255)
    pin = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    template = models.ForeignKey('ProductsProductPropertyTemplate', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_property_field'


class ProductsProductPropertyTemplate(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100)
    note = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_property_template'


class ProductsProductRelateItem(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING, related_name="+")
    relate_product = models.ForeignKey(ProductsProduct, models.DO_NOTHING, blank=True, null=True, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_product_relate_item'


class ProductsTestimonial(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    image = models.CharField(max_length=255)
    mobile_image = models.CharField(max_length=255)
    title = models.TextField()
    caption = models.TextField()
    youtube_url = models.CharField(max_length=255)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'products_testimonial'


class PromotionsPromotion(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    require_coupon = models.BooleanField()
    show_countdown = models.BooleanField()
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    code = models.CharField(max_length=255)
    quantity = models.SmallIntegerField(blank=True, null=True)
    limit_per_user = models.IntegerField(blank=True, null=True)
    limit_per_day = models.IntegerField(blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)
    price = models.IntegerField()
    dummy_price = models.IntegerField(blank=True, null=True)
    lifetime_limit = models.IntegerField()
    dummy_lifetime_limit = models.SmallIntegerField(blank=True, null=True)
    other = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    ordering = models.IntegerField(blank=True, null=True)
    prices = models.DecimalField(max_digits=10, decimal_places=2)
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    discount_main_product = models.DecimalField(max_digits=10, decimal_places=2)
    cost_of_product = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)
    prices_total = models.DecimalField(max_digits=10, decimal_places=2)
    is_purchase = models.BooleanField()
    is_loop = models.BooleanField()
    time_loop_hr = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'promotions_promotion'
        unique_together = (('product', 'code'),)


class PromotionsPromotionCoupon(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=100)
    is_redeemed = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    promotion = models.ForeignKey(PromotionsPromotion, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'promotions_promotion_coupon'


class PromotionsPromotionGiveaway(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField()
    lifetime_limit = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING, blank=True, null=True)
    promotion = models.ForeignKey(PromotionsPromotion, models.DO_NOTHING)
    simulation_package = models.ForeignKey(PricingsSimulationPackageList, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    prices_total = models.DecimalField(max_digits=10, decimal_places=2)
    product_group = models.ForeignKey(MarketingProductgroups, models.DO_NOTHING, blank=True, null=True)
    discount_giveaway_product = models.DecimalField(max_digits=10, decimal_places=2)
    order_billing = models.IntegerField()
    is_giveaway = models.BooleanField()
    order_website = models.IntegerField()
    cost_of_product = models.DecimalField(max_digits=10, decimal_places=2)
    margin = models.DecimalField(max_digits=10, decimal_places=2)
    min_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'promotions_promotion_giveaway'


class PublicationsClassification(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(max_length=255)
    pedigree = models.CharField(max_length=1025, blank=True, null=True)
    content = models.TextField()
    cover_desktop = models.CharField(max_length=100, blank=True, null=True)
    cover_mobile = models.CharField(max_length=100, blank=True, null=True)
    other = models.JSONField()
    lft = models.IntegerField()
    rght = models.IntegerField()
    tree_id = models.IntegerField()
    level = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    parent = models.ForeignKey('self', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'publications_classification'
        unique_together = (('slug', 'parent'),)


class QuickLink(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    shorten_link = models.CharField(unique=True, max_length=255)
    full_link = models.CharField(max_length=255)
    views = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quick_link'


class QuickLinkMapGenerate(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quick_link = models.ForeignKey(QuickLink, models.DO_NOTHING)
    quick_link_option = models.ForeignKey('QuickLinkOptionGenerate', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quick_link_map_Generate'


class QuickLinkOptionGenerate(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    prefix = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField()
    remark = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quick_link_option_generate'


class QuickpayInstallmentBanks(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    terms = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    installment_bank = models.ForeignKey(PaymentPoliciesInstallmentBank, models.DO_NOTHING)
    link = models.ForeignKey('QuickpayLink', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quickpay_installment_banks'


class QuickpayLegacyClaimLink(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    claimed_at = models.DateTimeField(blank=True, null=True)
    token = models.TextField()
    email = models.CharField(max_length=100)
    payment_ref_id = models.CharField(max_length=20)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    link = models.ForeignKey('QuickpayLink', models.DO_NOTHING)
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'quickpay_legacy_claim_link'


class QuickpayLink(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    schedule_start_at = models.DateTimeField(blank=True, null=True)
    schedule_end_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    enable_transfer_payment = models.BooleanField()
    enable_ibanking_payment = models.BooleanField()
    enable_card_payment = models.BooleanField()
    enable_installment_payment = models.BooleanField()
    enable_qr_payment = models.BooleanField()
    enable_counter_service = models.BooleanField()
    link_id = models.CharField(unique=True, max_length=255, blank=True, null=True)
    pricing_id = models.IntegerField(blank=True, null=True)
    show_countdown = models.BooleanField()
    manual_price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    manual_lifetime_limit = models.IntegerField(blank=True, null=True)
    user_limit = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    custom_cover = models.ForeignKey(FilerImage, models.DO_NOTHING, blank=True, null=True, related_name="+")
    pricing_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    promotion = models.ForeignKey(PromotionsPromotion, models.DO_NOTHING, blank=True, null=True)
    sale_agent = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    manual_tag_transaction = models.BooleanField()
    marketing_channel = models.ForeignKey(MarketingMarketingChannel, models.DO_NOTHING, blank=True, null=True)
    link_id_with_checksum = models.CharField(unique=True, max_length=255, blank=True, null=True)
    is_auth_by_user = models.BooleanField()
    is_auth_required = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'quickpay_link'


class QuickpayTransferAccountAllowed(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    bank_account = models.ForeignKey(AccountingsBankaccount, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    link = models.ForeignKey(QuickpayLink, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quickpay_transfer_account_allowed'
        unique_together = (('link', 'bank_account'),)


class QuizAnswer(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    is_correct_ordering = models.IntegerField(blank=True, null=True)
    is_correct = models.BooleanField()
    answer_text = models.CharField(max_length=255, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz = models.ForeignKey('QuizQuiz', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    prefix = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_answer'


class QuizMaxScore(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    max_score = models.FloatField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz_set = models.ForeignKey('QuizQuizSet', models.DO_NOTHING)
    skill = models.ForeignKey(DashboardSkill, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quiz_max_score'


class QuizQuestion(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    content_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz = models.ForeignKey('QuizQuiz', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    header = models.BooleanField()
    remark_number = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_question'


class QuizQuiz(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    answer_type = models.SmallIntegerField()
    answer_detail = models.TextField(blank=True, null=True)
    recording = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz_group = models.ForeignKey('QuizQuizGroup', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz_number = models.CharField(max_length=20, blank=True, null=True)
    quiz_type = models.SmallIntegerField()

    class Meta:
        managed = False
        db_table = 'quiz_quiz'


class QuizQuizGroup(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    question_type = models.SmallIntegerField()
    answer_type = models.SmallIntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz_set = models.ForeignKey('QuizQuizSet', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz_quiz_group'


class QuizQuizSet(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    answer_pdf = models.CharField(max_length=100, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quiz_quiz_set'


class QuizScoreSkill(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    quiz = models.ForeignKey(QuizQuiz, models.DO_NOTHING)
    skill = models.ForeignKey(DashboardSkill, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'quiz_score_skill'


class ReversionRevision(models.Model):
    date_created = models.DateTimeField()
    comment = models.TextField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")

    class Meta:
        managed = False
        db_table = 'reversion_revision'


class ReversionVersion(models.Model):
    object_id = models.CharField(max_length=191)
    format = models.CharField(max_length=255)
    serialized_data = models.TextField()
    object_repr = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    revision = models.ForeignKey(ReversionRevision, models.DO_NOTHING)
    db = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'reversion_version'
        unique_together = (('db', 'content_type', 'object_id', 'revision'),)


class SimpleTestsSegmentRecommendProduct(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    promotion = models.ForeignKey(PromotionsPromotion, models.DO_NOTHING, blank=True, null=True)
    segment_score = models.ForeignKey('SimpleTestsSegmentscore', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simple_tests_segment_recommend_product'


class SimpleTestsSegmentscore(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    segment_title = models.CharField(max_length=70)
    mininum_score = models.DecimalField(max_digits=5, decimal_places=2)
    maxinum_score = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    desktop = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simple_test = models.ForeignKey('SimpleTestsSimpletest', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simple_tests_segmentscore'


class SimpleTestsSimpletest(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(unique=True, max_length=255)
    sub_title = models.CharField(max_length=80, blank=True, null=True)
    title_seo = models.CharField(max_length=70)
    description_seo = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    navbar_title = models.CharField(max_length=70, blank=True, null=True)
    max_score = models.DecimalField(max_digits=8, decimal_places=2)
    shuffle_exercises = models.BooleanField()
    desktop = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    test_taking_description = models.TextField()
    total_time = models.DecimalField(max_digits=8, decimal_places=2)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    profile_template = models.ForeignKey(DurianfromsFromTemplate, models.DO_NOTHING, blank=True, null=True)
    answer_pdf = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simple_tests_simpletest'


class SimpleTestsSimpletestauthor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    author = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simple_test = models.ForeignKey(SimpleTestsSimpletest, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simple_tests_simpletestauthor'
        unique_together = (('simple_test', 'author', 'live'),)


class SimpleTestsSimpletestexercise(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey(ExaminationsExercise, models.DO_NOTHING)
    simple_test = models.ForeignKey(SimpleTestsSimpletest, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simple_tests_simpletestexercise'


class SimpleTestsSimpletestsegmentscore(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    segment_score = models.ForeignKey(SimpleTestsSegmentscore, models.DO_NOTHING)
    simple_test = models.ForeignKey(SimpleTestsSimpletest, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simple_tests_simpletestsegmentscore'


class SimpleTestsTesttaker(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    answer_value = models.JSONField()
    name = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simple_test = models.ForeignKey(SimpleTestsSimpletest, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    profile_data = models.ForeignKey(DurianfromsData, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simple_tests_testtaker'


class SimulationsPackage(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(max_length=50)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simulation = models.ForeignKey('SimulationsSimulation', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    cost_of_product = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'simulations_package'


class SimulationsPackageAllowSections(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    package = models.ForeignKey(SimulationsPackage, models.DO_NOTHING)
    section = models.ForeignKey('SimulationsSection', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simulations_package_allow_sections'


class SimulationsPart(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    part_name = models.CharField(max_length=70)
    total_score = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    media = models.CharField(max_length=200, blank=True, null=True)
    example_html = models.TextField(blank=True, null=True)
    part_direction = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    section = models.ForeignKey('SimulationsSection', models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simulations_part'


class SimulationsPartScoreGuide(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    show_guide = models.BooleanField()
    guide_text = models.CharField(max_length=255, blank=True, null=True)
    guide_color = models.CharField(max_length=10)
    min_score = models.DecimalField(max_digits=5, decimal_places=2)
    max_score = models.DecimalField(max_digits=5, decimal_places=2)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    part = models.ForeignKey(SimulationsPart, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simulations_part_score_guide'


class SimulationsQuestion(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    question_caption = models.CharField(max_length=70)
    max_choice = models.IntegerField()
    question_html = models.TextField()
    answer_list = models.TextField()  # This field type is a guess.
    score_list = models.TextField()  # This field type is a guess.
    ref_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    part = models.ForeignKey(SimulationsPart, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    explanations = models.TextField()

    class Meta:
        managed = False
        db_table = 'simulations_question'


class SimulationsSection(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    section_name = models.CharField(max_length=70)
    total_score = models.DecimalField(max_digits=8, decimal_places=2)
    time = models.DecimalField(max_digits=8, decimal_places=2)
    section_type = models.SmallIntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simulation = models.ForeignKey('SimulationsSimulation', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    pass_score = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simulations_section'


class SimulationsSimulation(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    sub_title = models.TextField(blank=True, null=True)
    exam_info = models.TextField()
    test_book_style = models.SmallIntegerField()
    scorecard_style = models.SmallIntegerField()
    max_score = models.DecimalField(max_digits=8, decimal_places=2)
    answer_value_type = models.SmallIntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    media = models.CharField(max_length=200, blank=True, null=True)
    is_show_answer = models.BooleanField()
    slug = models.CharField(unique=True, max_length=50, blank=True, null=True)
    answer_pdf = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'simulations_simulation'


class SimulationsSimulationtutorial(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simulation = models.ForeignKey(SimulationsSimulation, models.DO_NOTHING)
    tutorial = models.ForeignKey('SimulationsTutorial', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simulations_simulationtutorial'


class SimulationsTutorial(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    mobile_text = models.TextField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'simulations_tutorial'


class SkuMastersku(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    master_sku_id = models.CharField(unique=True, max_length=255)
    ref_product_id = models.IntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    legacy_sku = models.CharField(unique=True, max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sku_mastersku'


class SkuSellingproduct(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    selling_product_id = models.CharField(unique=True, max_length=255)
    sku_id = models.CharField(max_length=255)
    name = models.CharField(max_length=500, blank=True, null=True)
    price = models.IntegerField()
    pricing_type = models.CharField(max_length=255)
    pricing_type_id = models.IntegerField()
    ref_product_id = models.IntegerField()
    ref_pricing_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    ref_data = models.JSONField()

    class Meta:
        managed = False
        db_table = 'sku_sellingproduct'


class SkuSku(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    sku_id = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    product_type_id = models.IntegerField()
    ref_product_id = models.IntegerField()
    ref_data = models.JSONField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'sku_sku'


class SocialAuthAssociation(models.Model):
    server_url = models.CharField(max_length=255)
    handle = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    issued = models.IntegerField()
    lifetime = models.IntegerField()
    assoc_type = models.CharField(max_length=64)

    class Meta:
        managed = False
        db_table = 'social_auth_association'
        unique_together = (('server_url', 'handle'),)


class SocialAuthCode(models.Model):
    email = models.CharField(max_length=254)
    code = models.CharField(max_length=32)
    verified = models.BooleanField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_code'
        unique_together = (('email', 'code'),)


class SocialAuthNonce(models.Model):
    server_url = models.CharField(max_length=255)
    timestamp = models.IntegerField()
    salt = models.CharField(max_length=65)

    class Meta:
        managed = False
        db_table = 'social_auth_nonce'
        unique_together = (('server_url', 'timestamp', 'salt'),)


class SocialAuthPartial(models.Model):
    token = models.CharField(max_length=32)
    next_step = models.SmallIntegerField()
    backend = models.CharField(max_length=32)
    data = models.TextField()
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_partial'


class SocialAuthUsersocialauth(models.Model):
    provider = models.CharField(max_length=32)
    uid = models.CharField(max_length=255)
    extra_data = models.TextField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    created = models.DateTimeField()
    modified = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'social_auth_usersocialauth'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)


class StorePackaging(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    freight = models.DecimalField(max_digits=10, decimal_places=2)
    packing_fee = models.DecimalField(max_digits=10, decimal_places=2)
    weight = models.DecimalField(max_digits=10, decimal_places=2)
    width = models.DecimalField(max_digits=10, decimal_places=2)
    length = models.DecimalField(max_digits=10, decimal_places=2)
    border = models.DecimalField(max_digits=10, decimal_places=2)
    max_weight = models.DecimalField(max_digits=10, decimal_places=2)
    max_width = models.DecimalField(max_digits=10, decimal_places=2)
    max_length = models.DecimalField(max_digits=10, decimal_places=2)
    max_border = models.DecimalField(max_digits=10, decimal_places=2)
    cost_of_packaging = models.DecimalField(max_digits=10, decimal_places=2)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'store_packaging'


class StoreProductwithstoreid(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    store_id = models.CharField(max_length=255, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'store_productwithstoreid'


class SuperLandingContent(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=150)
    navbar_title = models.CharField(max_length=70, blank=True, null=True)
    show_title = models.BooleanField()
    content = models.TextField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    topic = models.ForeignKey('SuperLandingTopic', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'super_landing_content'


class SuperLandingSuggestExam(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_important = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    exam = models.ForeignKey(ExaminationsExam, models.DO_NOTHING)
    topic = models.ForeignKey('SuperLandingTopic', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'super_landing_suggest_exam'
        unique_together = (('topic', 'exam'),)


class SuperLandingSuggestNews(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_important = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    news = models.ForeignKey(NewsNews, models.DO_NOTHING)
    topic = models.ForeignKey('SuperLandingTopic', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'super_landing_suggest_news'
        unique_together = (('topic', 'news'),)


class SuperLandingSuggestProduct(models.Model):
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    enable = models.BooleanField()
    ordering = models.IntegerField(blank=True, null=True)
    is_important = models.BooleanField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    topic = models.ForeignKey('SuperLandingTopic', models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'super_landing_suggest_product'
        unique_together = (('topic', 'product'),)


class SuperLandingTopic(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    slug = models.CharField(unique=True, max_length=255)
    title = models.CharField(unique=True, max_length=150)
    navbar_title = models.CharField(max_length=70, blank=True, null=True)
    seo_title = models.CharField(unique=True, max_length=70, blank=True, null=True)
    seo_description = models.TextField(blank=True, null=True)
    seo_keywords = models.CharField(max_length=255, blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    product_topic_title = models.CharField(max_length=100)
    news_topic_title = models.CharField(max_length=100)
    exam_topic_title = models.CharField(max_length=100)
    product_suggest_title = models.CharField(max_length=100)
    news_suggest_title = models.CharField(max_length=100)
    exam_suggest_title = models.CharField(max_length=100)
    cover_alt_text = models.CharField(max_length=100)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    desktop_cover_image = models.ForeignKey(FilerImage, models.DO_NOTHING, related_name="+")
    mobile_cover_image = models.ForeignKey(FilerImage, models.DO_NOTHING, blank=True, null=True, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'super_landing_topic'


class TaggitTag(models.Model):
    name = models.CharField(unique=True, max_length=100)
    slug = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'taggit_tag'


class TaggitTaggeditem(models.Model):
    object_id = models.IntegerField()
    content_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING)
    tag = models.ForeignKey(TaggitTag, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'taggit_taggeditem'
        unique_together = (('content_type', 'object_id', 'tag'),)


class TokenBlacklistBlacklistedtoken(models.Model):
    blacklisted_at = models.DateTimeField()
    token = models.OneToOneField('TokenBlacklistOutstandingtoken', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'token_blacklist_blacklistedtoken'


class TokenBlacklistOutstandingtoken(models.Model):
    token = models.TextField()
    created_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField()
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    jti = models.CharField(unique=True, max_length=255)

    class Meta:
        managed = False
        db_table = 'token_blacklist_outstandingtoken'


class TransactionsEasySlipTransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    ref_id = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_date = models.DateTimeField(blank=True, null=True)
    slip_path = models.TextField()
    raw_response = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    error_text = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transactions_easy_slip_transaction'


class TransactionsOmiseCardTransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    net = models.DecimalField(max_digits=8, decimal_places=2)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    fee_vat = models.DecimalField(max_digits=8, decimal_places=2)
    interest = models.DecimalField(max_digits=8, decimal_places=2)
    interest_vat = models.DecimalField(max_digits=8, decimal_places=2)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)
    charge_id = models.CharField(max_length=255)
    card_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    bank = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    last_digits = models.CharField(max_length=4)
    expiration_month = models.IntegerField()
    expiration_year = models.IntegerField()
    failure_code = models.CharField(max_length=100, blank=True, null=True)
    failure_message = models.TextField(blank=True, null=True)
    authorize_uri = models.CharField(max_length=255, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'transactions_omise_card_transaction'


class TransactionsOmiseInstallmentTransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    net = models.DecimalField(max_digits=8, decimal_places=2)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    fee_vat = models.DecimalField(max_digits=8, decimal_places=2)
    interest = models.DecimalField(max_digits=8, decimal_places=2)
    interest_vat = models.DecimalField(max_digits=8, decimal_places=2)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)
    charge_id = models.CharField(max_length=100)
    source_id = models.CharField(max_length=100)
    source_type = models.CharField(max_length=50)
    failure_code = models.CharField(max_length=100, blank=True, null=True)
    failure_message = models.TextField(blank=True, null=True)
    installment_term = models.IntegerField()
    zero_interest_installments = models.BooleanField()
    authorize_uri = models.CharField(max_length=255, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'transactions_omise_installment_transaction'


class TransactionsOmiseInternetBankingTransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    net = models.DecimalField(max_digits=8, decimal_places=2)
    fee = models.DecimalField(max_digits=8, decimal_places=2)
    fee_vat = models.DecimalField(max_digits=8, decimal_places=2)
    interest = models.DecimalField(max_digits=8, decimal_places=2)
    interest_vat = models.DecimalField(max_digits=8, decimal_places=2)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)
    charge_id = models.CharField(max_length=100)
    source_id = models.CharField(max_length=100)
    source_type = models.CharField(max_length=50)
    failure_code = models.CharField(max_length=100, blank=True, null=True)
    failure_message = models.TextField(blank=True, null=True)
    authorize_uri = models.CharField(max_length=255, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    expires_at = models.DateTimeField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'transactions_omise_internet_banking_transaction'


class TransactionsScbQrPaymentTransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    qr_code = models.TextField(blank=True, null=True)
    status = models.SmallIntegerField()
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'transactions_scb_qr_payment_transaction'


class TransactionsTransfertransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    status = models.SmallIntegerField()
    total_revenue = models.IntegerField()
    transfer_at = models.DateTimeField()
    slip = models.CharField(max_length=100, blank=True, null=True)
    bank_account = models.ForeignKey(AccountingsBankaccount, models.DO_NOTHING)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'transactions_transfertransaction'


class TransactionsTwoctwopTransaction(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=20)
    invoice = models.CharField(max_length=255)
    card_id = models.CharField(max_length=255)
    bank = models.CharField(max_length=255, blank=True, null=True)
    channel = models.CharField(max_length=100, blank=True, null=True)
    brand = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, null=True)
    paid_at = models.DateTimeField(blank=True, null=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    tranref = models.CharField(db_column='tranRef', max_length=255, blank=True, null=True)  # Field name made lowercase.
    detail = models.TextField(blank=True, null=True)
    raw_data = models.TextField(blank=True, null=True)
    response_front = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    order = models.ForeignKey(OrdersOrder, models.DO_NOTHING)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'transactions_twoctwop_transaction'


class UserGenerateCreateEnrollmentLog(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    lifetime_limit = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enrollment = models.ForeignKey(EnrollmentsEnrollment, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    simulation_enrollment = models.ForeignKey(EnrollmentsSimulationEnrollment, models.DO_NOTHING, blank=True, null=True)
    simulation_package = models.ForeignKey(PricingsSimulationPackageList, models.DO_NOTHING, blank=True, null=True)
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'user_generate_create_enrollment_log'


class UsersAddress(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    default_address = models.BooleanField()
    invoice_address = models.BooleanField()
    name = models.TextField()
    address_name = models.TextField()
    province = models.IntegerField()
    zip_code = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'users_address'


class UsersAddressversiontwo(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    phone_number = models.CharField(max_length=30, blank=True, null=True)
    default_address = models.BooleanField()
    invoice_address = models.BooleanField()
    name = models.TextField()
    address_name = models.TextField()
    house_number = models.CharField(max_length=30, blank=True, null=True)
    road = models.CharField(max_length=255, blank=True, null=True)
    alley = models.CharField(max_length=255, blank=True, null=True)
    village = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=30, blank=True, null=True)
    sub_district = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=255, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, blank=True, null=True, related_name="+")
    place_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_addressversiontwo'


class UsersGenerateUserGenerateLog(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    purpose = models.IntegerField()
    pricing_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    enrollment = models.ForeignKey(EnrollmentsEnrollment, models.DO_NOTHING, blank=True, null=True)
    order = models.OneToOneField(OrdersOrder, models.DO_NOTHING, blank=True, null=True)
    pricing_type = models.ForeignKey(DjangoContentType, models.DO_NOTHING, blank=True, null=True)
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    promotion = models.ForeignKey(PromotionsPromotion, models.DO_NOTHING, blank=True, null=True)
    sale_agent = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    simulation_enrollment = models.ForeignKey(EnrollmentsSimulationEnrollment, models.DO_NOTHING, blank=True, null=True)
    skip_verify = models.BooleanField()
    actual_amount = models.IntegerField(blank=True, null=True)
    chat_link = models.CharField(max_length=255, blank=True, null=True)
    marketing_channel = models.ForeignKey(MarketingMarketingChannel, models.DO_NOTHING, blank=True, null=True)
    transaction_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_generate_user_generate_log'


class UsersInstructor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=255)
    avatar = models.CharField(max_length=100)
    education_info = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'users_instructor'


class UsersProfileimage(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    default_image = models.BooleanField()
    image = models.CharField(max_length=100, blank=True, null=True)
    social_image = models.TextField(blank=True, null=True)
    created_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")
    user = models.ForeignKey('UsersUser', models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'users_profileimage'


class UsersUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    is_instructor = models.BooleanField()
    education_info = models.TextField(blank=True, null=True)
    other = models.JSONField()

    class Meta:
        managed = False
        db_table = 'users_user'


class UsersUserGroups(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_groups'
        unique_together = (('user', 'group'),)


class UsersUserUserPermissions(models.Model):
    user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'users_user_user_permissions'
        unique_together = (('user', 'permission'),)


class WarehouseCostByOrder(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    order_id = models.CharField(max_length=255, blank=True, null=True)
    transfer = models.FloatField(blank=True, null=True)
    wage = models.FloatField(blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    interest = models.FloatField(blank=True, null=True)
    packing = models.FloatField(blank=True, null=True)
    storage = models.FloatField(blank=True, null=True)
    selling_product_id = models.CharField(max_length=255, blank=True, null=True)
    raw_data = models.JSONField(blank=True, null=True)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    raw_response = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_cost_by_order'


class WarehousePurchaseOrder(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    vender_name = models.CharField(max_length=255, blank=True, null=True)
    vender_address = models.CharField(max_length=255, blank=True, null=True)
    vender_tax = models.CharField(max_length=255, blank=True, null=True)
    order_deadline_date = models.CharField(max_length=255, blank=True, null=True)
    receipt_date = models.CharField(max_length=255, blank=True, null=True)
    payment_channel_id = models.CharField(max_length=255, blank=True, null=True)
    payment_channel = models.CharField(max_length=255, blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    vat = models.FloatField(blank=True, null=True)
    total_amount = models.FloatField(blank=True, null=True)
    discount = models.FloatField(blank=True, null=True)
    shipping_cost = models.FloatField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    product = models.JSONField(blank=True, null=True)
    raw_data = models.JSONField(blank=True, null=True)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    raw_response = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'warehouse_purchase_order'


class WarehouseStock(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    available_stock = models.DecimalField(max_digits=10, decimal_places=2)
    reserved_stock = models.DecimalField(max_digits=10, decimal_places=2)
    on_hand_stock = models.DecimalField(max_digits=10, decimal_places=2)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")

    class Meta:
        managed = False
        db_table = 'warehouse_stock'


class WikipediasRelateExercise(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    exercise = models.ForeignKey(ExaminationsExamexercise, models.DO_NOTHING)
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    wikipedia = models.ForeignKey('WikipediasWikipedia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wikipedias_relate_exercise'


class WikipediasRelateProduct(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    product = models.ForeignKey(ProductsProduct, models.DO_NOTHING)
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    wikipedia = models.ForeignKey('WikipediasWikipedia', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wikipedias_relate_product'


class WikipediasWikipedia(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    publish_state = models.CharField(max_length=20)
    published_at = models.DateTimeField(blank=True, null=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    advertising_enable = models.BooleanField()
    advertising_display = models.SmallIntegerField()
    name = models.CharField(max_length=255)
    slug = models.CharField(unique=True, max_length=255)
    synonym = models.TextField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    desktop_cover = models.CharField(max_length=100, blank=True, null=True)
    mobile_cover = models.CharField(max_length=100, blank=True, null=True)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    render_mathjax = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'wikipedias_wikipedia'


class WikipediasWikipediaAdvertisings(models.Model):
    wikipedia = models.ForeignKey(WikipediasWikipedia, models.DO_NOTHING)
    advertising = models.ForeignKey(AdvertisementsAdvertising, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wikipedias_wikipedia_advertisings'
        unique_together = (('wikipedia', 'advertising'),)


class WikipediasWikipediaAuthor(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    sequence = models.IntegerField(blank=True, null=True)
    uuid = models.UUIDField(unique=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    wikipedia = models.ForeignKey(WikipediasWikipedia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wikipedias_wikipedia_author'
        unique_together = (('wikipedia', 'user'),)


class WikipediasWikipediaClassification(models.Model):
    live = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    uuid = models.UUIDField(unique=True)
    ordering = models.IntegerField(blank=True, null=True)
    is_legacy = models.BooleanField()
    legacy_id = models.IntegerField(blank=True, null=True)
    classification = models.ForeignKey(PublicationsClassification, models.DO_NOTHING)
    created_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    updated_user = models.ForeignKey(UsersUser, models.DO_NOTHING, related_name="+")
    wikipedia = models.ForeignKey(WikipediasWikipedia, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'wikipedias_wikipedia_classification'
        unique_together = (('wikipedia', 'classification'),)
