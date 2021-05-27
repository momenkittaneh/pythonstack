from django.db import models
class UserModels(models.Manager):
    def register_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors["first_name"] = "first name should be at least 2 characters and contains only characters"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors["last_name"] = "last name should be at least 2 characters and contains only characters"
        if len(postData['password']) < 8:
            errors["password"] = "password should be more than 8 characters atleast"
        EMAIL_REGEX = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(postData['email']):
            errors['email'] = "Invalid email address!"
        return errors

class user(models.Model):
    first_name= models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


def create_user(first_name,last_name,email,passwd):
    return user.objects.create(first_name=first_name,last_name=last_name,email=email,password=passwd)

def get_user(email,passwd):
    users=user.objects.filter(email=email,password=passwd)
    #[0] to select only one user for the email and password
    if len(users) > 0:
        return users[0]
    return False







