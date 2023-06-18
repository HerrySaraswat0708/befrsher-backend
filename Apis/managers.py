from django.contrib.auth.base_user import BaseUserManager

class CustomManager(BaseUserManager):
    def create_place(self,name,address):
        place=self.model(name=name,address=address)
        place.save()
        return place