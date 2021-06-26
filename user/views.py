from django.shortcuts import render
from rest_framework import generics
from .models import *
from rest_framework.views import APIView
from .serializers import *
from .forms import *
from rest_framework.response import Response
from user.models import *
from user.serializers import *
from django.db.models import Q
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate, logout, login
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .pagination import CustomPagination
from rest_framework.pagination import PageNumberPagination
# Create your views here.
class CreatePost(generics.CreateAPIView):
    """
        View for post creation
    """
    def post(self,request):
        data=request.data
        img=request.FILES.getlist('images') #getting images
        image=len(img)
        form=StoryForm(request.POST)  # posting data into the form
        if form.is_valid():
            task=form.save() #saving form
            id=task.id #getting id of the form
            if(image > 0):
                print(img)
                for i in img:
                    print(i) # getting images 
                    PostImage.objects.create(story_id=id,images=i) #creating object with story_id as id which is foreign key and images which is uploaded by user
                return Response("success")
        else:
            return Response("fail")


class StoryStatusCountAPIView(APIView):
    """
        View for getting count for liked and disliked
    """
    def get(self, *args, **kwargs):
        count = {}
        data = PostStatus.objects.filter(story_id=self.kwargs.get('pk'))
        count["liked_count"] = data.filter(status="like").count() #getting the count who liked the post
        count["disliked_count"] = data.filter(status="dislike").count() #getting the count who dislike the post
        return Response({"response":count}) 

class StoryListAPIView(APIView):
    """
        API that returns a list of posts
    """
    pagination_class = PageNumberPagination
    def get(self,*args, **kwargs):  # id which is pass through url pk is user id who is logged in
        obj = Story.objects.order_by('-weight')
        a=[]
        for i in obj:
            data={}
            print(i.id) #getting story id
            obj1=Story.objects.filter(id=i.id)
            serializer=PostSerializer(obj1,many=True)
            data["story"]=serializer.data  #getting data of corresponding story and appending to list
            obj2=PostImage.objects.filter(story_id=i.id)
            serializer2=PostimageSerializer(obj2,many=True)
            data["images"]=serializer2.data #getting images of corresponding story
            obj3=PostStatus.objects.filter(story_id=i.id).filter(user_id=self.kwargs.get('pk')).exists()
            obj4 = PostStatus.objects.filter(story_id=i.id)
            data["liked_count"] = obj4.filter(status="like").count() #getting the count who liked the post
            data["disliked_count"] = obj4.filter(status="dislike").count() #getting the count who dislike the post
            if(obj3==True):
                user=PostStatus.objects.filter(story_id=i.id).filter(user_id=self.kwargs.get('pk'))
                serializer4=PoststatusSerializer(user,many=True)
                data["current_user_status"]=serializer4.data[0]['status'] #current status of user to the post
                a.append(data)
            else:
                data["current_user_status"]="dislike"
                a.append(data)
        return Response({"response":a})


class StatusUpdateAPIView(APIView):
    """
        API for like and dislike a post
    """

    def get(self,*args, **kwargs): # id which is pass through url pk is story id and userid is id for user who is loggedin 
        data = PostStatus.objects.filter(story_id=self.kwargs.get('pk')).filter(user_id=self.kwargs.get('userid')) #checking whether the corresponding user have object with status for a particular post
        len_data=len(data)
        if(len_data>0):
            for  i in data:
                if(i.status=="like"): #current status checking
                    update=PostStatus.objects.get(id=i.id)
                    update.status="dislike" #updating status
                    update.save()
                    return Response("Status updated successfully!!")
                else:
                    update=PostStatus.objects.get(id=i.id)
                    update.status="like" #updating status
                    update.save()
                    return Response("Status updated successfully")
        else:
            return Response("No Data")


class UserListLikedPostAPIView(APIView):
    """
        API for like post by userslist
    """

    def get(self,*args, **kwargs):  # id which is pass through url pk is story id
        data = PostStatus.objects.filter(story_id=self.kwargs.get('pk')).filter(status="like") #filter the a particular post which have status liked
        a=[] #define an array
        for i in data:
            username=i.user_id.username #finding corresponding username who liked post
            a.append(username) #appending to an array
        return Response({"user_list":a})