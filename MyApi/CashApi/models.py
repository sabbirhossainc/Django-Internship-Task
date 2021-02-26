from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AccountHead(models.Model):
    # id = models.AutoField(Primary_key=True)
    user = models.OneToOneField(User, related_name='acc_head', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class AccountType(models.Model):
    # id = models.AutoField(Primary_key=True)
    acc_type_name = models.CharField(max_length=255)
    acc_head = models.ForeignKey(AccountHead, on_delete=models.CASCADE)

    def __str__(self):
        return self.acc_type_name

class AccountName(models.Model):
    # id = models.AutoField(Primary_key=True)
    acc_name = models.CharField(max_length=255)
    type_of_acc = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    opening_balance = models.FloatField(null=True, blank=True)
    closing_balance = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.acc_name

class JournalLog(models.Model):
    # id = models.AutoField(Primary_key=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    reference_no = models.CharField(max_length=255)

    def __str__(self):
        return self.reference_no

class JournalLogDetail(models.Model):
    # id = models.AutoField(Primary_key=True)
    journal_log = models.ForeignKey(JournalLog, on_delete=models.CASCADE)
    account_name = models.ForeignKey(AccountName, on_delete=models.CASCADE)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.journal_log.reference_no

class CashFlow(models.Model):
    user = models.ForeignKey(AccountHead, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    cash = models.IntegerField(default=0)
