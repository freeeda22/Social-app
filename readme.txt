**How to run the project :
 1. install requirements.txt 
 2. create-post url testing using Postman

**url description**
 1. create-post :
    input-fields :["name","description","tag","weight","images"] all fields are required

2. story-status-count/<int:pk>/:
    passing a particular post id through url

3.list-story/<int:pk>/:
    passing a user id through url

4. post-like-dislike/<int:pk>/<int:userid>/:
    passing a post id and user id through url

5. post-user-liked/<int:pk>/:
    passing a post id through url