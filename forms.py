from django.forms import ModelForm
from .models import *
from django import forms

class PurchageForm(ModelForm):
    class Meta:
        model=Purchagemaster
        fields = '__all__'

class customerform(ModelForm):
    class Meta:
        model=customer
        fields = '__all__'

class Nurseryform(ModelForm):
    class Meta:
        model=Nurserymaster
        fields = '__all__'

class Partylistform(ModelForm):
    class Meta:
        model=PartylistMaster
        fields = '__all__'

class PartylistdeleteMasterform(ModelForm):
    class Meta:
        model=PartylistdeleteMaster
        fields = '__all__'

class PBcustomerform(ModelForm):
    class Meta:
        model=PBcustomerMaster
        fields='__all__'

class Pbsugarcaneform(ModelForm):
    class Meta:
        model=PbsugarcaneMaster
        fields='__all__'

class addpureform(ModelForm):
    class Meta:
        model=addpureMaster
        fields='__all__'

class Sbcustomerform(ModelForm):
    class Meta:
        model=SBcustomerMaster
        fields='__all__'

class sugarcanesbform(ModelForm):
    class Meta:
        model=SbsugarMaster
        fields='__all__'

class labourform(ModelForm):
    class Meta:
        model=LabourMaster
        fields="__all__"

class sclabourform(ModelForm):
    class Meta:
        model=sclabourMaster
        fields="__all__"

class inCustForm(ModelForm):
    class Meta:
        model=incustMaster
        fields="__all__"

class inlistform(ModelForm):
    class Meta:
        model=inlistMaster
        fields="__all__"