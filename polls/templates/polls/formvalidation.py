from django.contrib.auth import authenticate,User
from django.forms import ModelForm
from django.forms import forms


#Trying this code below..a form was designed manually...then wrote in django format at form
#Then process at views.

class userform(forms.ModelForm):
    username= forms.CharField(widget=forms.TextInput(
        attrs={'class': 'forms-control', 'placeholder': 'Enter username'}
    ), required=True, max_length=50)
    email = forms.CharField(widget=forms.EmailInput(
        attrs={'class': 'forms-control', 'placeholder': 'Enter email ID'}
    ), required=True, max_length=50)
    first_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'forms-control', 'placeholder': 'Enter  first name'}
    ), required=True, max_length=50)
    lastname = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'forms-control', 'placeholder': 'Enter last name'}
    ), required=True, max_length=50)
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'forms-control', 'placeholder': 'Enter password'}
    ), required=True, max_length=50)
    confirm_password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'forms-control', 'placeholder': 'Enter confirm password'}
    ), required=True, max_length=50)


    class Meta():
        model = User
        fields =['username','email','first_name','last_name','password','confirm_password']

            def clean_username(self):
                user=self.cleaned_data['username']
                try:
                    match = User.objects.get(username = user)
                except:
                    return self.cleaned_data['username'] #user
                raise forms.ValidationError("Username already exist")

            def clean_email(self):
                email = self.cleaned_data['email']
                try:
                    mt = validate_email(email)
                except:
                    return forms.ValidationError("Email is not in correct Format")
                return email


            def clean_confirm_password(self):
                pas = self.cleaned_data['password']
                cpas = self.cleaned_data['confirm_password']
                MIN_LENGTH = 8
                if pas and cpas:
                    if pas != cpas:
                        raise forms.ValidationError("password and confirm password not matched")
                    else:
                        if len(pas) < MIN_LENGTH:
                            raise forms.ValidationError("Password should have atleast %d character" %MIN_LENGTH)
                if pas.isdigit():
                    raise forms.ValidationError("Password should not all numeric")


        #The following code is under views...
    def student(request):
        obj1 = student.objects.all().order_by('-dat')

        if request.method =='POST':
            form = student_form(request.POST)
            if form.is_valid():
                # why is no return of cleaned_data here
                form.save()
                return HttpResponseRedirect('/studentform')
            else:
                form = student_form()
            return render(request, 'student.html', {'form': form, 'std':obj1})

    def registration(request):
        if request.method=='POST':
            form1 = userform(request.POST)
            if form1.is_valid():
                username = form1.cleaned_data['username']
                first_name = form1.cleaned_data['first_name']
                last_name = form1.cleaned_data['last_name']
                email = form1.cleaned_data['email']
                password = form1.cleaned_data['password']
                User.objects.create_user(username=username, first_name = first_name, last_name=last_name)
                messages.success(request,'user registration successful')
                usr = auth.autheticate(username=username, password= password)
                auth.login(request, usr)
                return render(request,'welcome.html')
        else:
            form1 = userform()
        return render(request, 'registration.html', {'frm':form1})

   def login(request):
       if request.method=='POST':
           username = request.POST['user']
           password = request.POST['pas']
           try:
               user = auth.autheticate(username=username, password=password)
               if user is not None:
                   auth.login(request, user)
               else:
                   messages.error(request, 'Username and password did not matched')
           except auth.ObjectsNotExist:
               print("invalid user")
        return render(request,'login.html')


    def logout(request):
        pass


































