from django.shortcuts import render
from django.http import HttpResponse
from TestModel.models import Test
# Create your views here.

def add_testdb(request):
        test1 = Test(name='w3schools.cc')
        test1.save()
        return HttpResponse("<p>database add success!!</p>")

def get_testdb(request):
    #initialize
        response = ""
        response1 = ""

    #select * from
        list = Test.objects.all()

    #filter with condition
        response2 = Test.objects.filter(id=1)

    #get single object
        response3 = Test.objects.get(id=1)

    #limit return data
        Test.objects.order_by('name')[0:2]

        Test.objects.order_by("id")

    #output all data
        for var in list:
                response1 += var.name + ""
        response = response1

        return HttpResponse("<p>" + response + "</p>")

def update_testdb(request):
    #update the name field of id=1,then save, is equal to UPDATE
        test1 = Test.objects.get(id=1)
        test1.name = 'w3cschool tutorial'
        test1.save()

    #another way to update
    #   Test.objects.filter(id=1).update(name='w3cschool tutorial')

    #update all column
    #   Test.objects.all().update(name='w3cschool green hand tutorial')

        return HttpResponse("<p>Update successfully!!</p>")

def delete_testdb(request):
        test1 = Test.objects.get(id=1)
        test1.delete()

    #another way to delete
    #    Test.objects.filter(id=1).delete()

    #delete all data
    #    Test.objects.all().delete()

        return HttpResponse("<p>Delete Success!</p>")
