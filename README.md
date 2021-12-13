
# Flask Social Networking App
A Social networking app which connects user based on their interest


## Run Locally

Clone the project

```bash
    git clone https://github.com/Shikhar-SRJ/flask_social_media_app.git
```

Create a virtual environment. ( if using linux then use)

```bash
    python3 -m venv venv
```
Activate virtual environment
```bash
    source venv/bin/activate
```
Install dependencies

```bash
    pip install -r requirements.txt
```

Export Flask app and environment

```bash
    export FLASK_APP=manage.py
    export FLASK_ENV=development

```

Setup Database

```bash
    flask db init
    flask db migrate -m "<optional-message>"
    flask db upgrade
  
```
Run the Server
```bash
    flask run
```


## Features

- User Registration
- Forgot password
- User(CRUD)
- User profile updation
- Post(CRUD)
- Follow - Unfollow other users
- Customize user interests and finding users with common interests
- Last Seen (for users)
- Explore (Shows all public posts)
- Email Verification: Sending Email verification through SMTP to verify the e-mail id of other users.
- Profile Settings: Editing profile settings and making changes to the info.


## Relational Schema
- User(id,username,email,password,post,aboutme,last_seen,followed)
- Post(id, caption,body,timestamp, user_id)
- Interests(id,music,tech,sports,local_news,international_news,politics)
- followers [Auxilliary table]  which maps followed users to following users
## Screenshots
User sign in page

![1](https://user-images.githubusercontent.com/80159535/145722439-f8f876a4-3e09-482d-8714-5ad47d393620.png)

Home page

![2](https://user-images.githubusercontent.com/80159535/145722452-7db0391a-b393-408f-a490-c491ca94ee2f.png)

User post 

![3](https://user-images.githubusercontent.com/80159535/145722494-0b111287-1746-4095-8cf6-7a186b28951c.png)

Profile 

![7](https://user-images.githubusercontent.com/80159535/145722519-b33ae9dd-9c2e-4d25-b699-4586027f1e47.png)

Customize interests

![5](https://user-images.githubusercontent.com/80159535/145722536-39767f72-ecc1-449b-a06b-2121847d5835.png)


Explore page where user can see all the posts

![6](https://user-images.githubusercontent.com/80159535/145722551-0dd32b00-7856-4b7c-9316-2848ff995a77.png)

Users with similar interests
![9](https://user-images.githubusercontent.com/80159535/145722571-59523591-4a3e-4135-a1c8-73b46f7f87ac.png)

![10](https://user-images.githubusercontent.com/80159535/145722598-17a5906a-550a-4c49-b24e-67c2384f65b3.png)

Follow and Unfollow

![4](https://user-images.githubusercontent.com/80159535/145722650-f220c4b2-676b-4ed8-8b40-5e35061c2128.png)



