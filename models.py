# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    password = models.CharField(max_length=15)

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Bill(models.Model):
    bill_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Patients', models.DO_NOTHING, blank=True, null=True)
    bill_name = models.CharField(max_length=120)
    bil_refer_by_dr = models.CharField(max_length=120)
    total = models.IntegerField()
    advance = models.IntegerField()
    balance = models.IntegerField()
    bill_date = models.DateField()
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bill'


class BillDetails(models.Model):
    det_id = models.AutoField(primary_key=True)
    det_bill = models.ForeignKey(Bill, models.DO_NOTHING)
    det_test = models.CharField(max_length=80)
    det_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'bill_details'


class Biochemistry(models.Model):
    b_id = models.AutoField(primary_key=True)
    p = models.ForeignKey('Patients', models.DO_NOTHING)
    p_name = models.CharField(max_length=25, db_collation='latin1_swedish_ci')
    referbydr = models.CharField(max_length=25, db_collation='latin1_swedish_ci')
    date_report = models.DateTimeField()
    fbs = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    ppbs = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    rbs = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    chl = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    hdl = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    tri = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    ldl = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    vldl = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    sur = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    sua = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    cre = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    sbt = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    dir = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    indir = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    stp = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    alb = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    glob = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    sgpt = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    sgot = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    scal = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    sod = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    spot = models.CharField(max_length=10, db_collation='latin1_swedish_ci')
    schl = models.CharField(max_length=10, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'biochemistry'


class Book(models.Model):
    book_id = models.IntegerField(primary_key=True)
    pat_id = models.IntegerField(blank=True, null=True)
    b_date = models.DateTimeField(blank=True, null=True)
    booking_status = models.IntegerField(blank=True, null=True)
    test_name = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class BookedTest(models.Model):
    book_id = models.AutoField(primary_key=True)
    p_id= models.ForeignKey('Patients', models.DO_NOTHING)
    b_date = models.DateTimeField()
    tests = models.CharField(max_length=25)
    booking_status = models.CharField(max_length=40)  #chanded it to charfield 

    # class Meta:
    #     managed = False
    #     db_table = 'booked_test'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
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


class Haematology(models.Model):
    ha_id = models.AutoField(primary_key=True)
    referby = models.CharField(max_length=25, db_collation='latin1_swedish_ci')
    p = models.ForeignKey('Patients', models.DO_NOTHING)
    p_name = models.CharField(max_length=40)
    date_report = models.DateTimeField()
    haemoglobin = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    wbc = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    haematocrit = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    rbc = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    neutrophils = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    eosinophils = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    basophilis = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    lymphocyes = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    monocytes = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    esr = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    bmin = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    clomin = models.CharField(max_length=20, db_collation='latin1_swedish_ci')
    placount = models.CharField(max_length=20, db_collation='latin1_swedish_ci')

    class Meta:
        managed = False
        db_table = 'haematology'


class LabTest(models.Model):
    test_id = models.AutoField(primary_key=True)
    test_name = models.CharField(max_length=191)
    test_cost = models.CharField(max_length=191)
    lab_test_image = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lab_test'


class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    patient_name = models.CharField(unique=True, max_length=255)
    patient_email = models.CharField(unique=True, max_length=255)
    patient_password = models.CharField(max_length=255)
    patient_dob = models.DateField(blank=True, null=True)
    patient_gender = models.CharField(max_length=45, blank=True, null=True)
    patient_status = models.IntegerField(blank=True, null=True)
    patient_phone_number = models.CharField(unique=True, max_length=12, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'patients'
