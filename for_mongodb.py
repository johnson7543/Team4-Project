# -*- coding: utf-8 -*-
"""
Created on Wed Jul 29 17:06:42 2020

@author: User
"""
import pymongo
import json

client = pymongo.MongoClient("mongodb+srv://Jerry_Chang:jerry123@cluster0.mmp88.mongodb.net/Jerry_Chang?retryWrites=true&w=majority")

# print(client.list_database_names())
scholarship_json = { "Item_name": "jim" , "End_date": 25, "Money":"Taiwan", "Grade" : 80, "Sport_Grade" : 80, "Apply" : "blahblahblah" }
db = client.blog

"""db.posts.insert_one( {"title": "My first post", "body": "This is the body of my first blog post", "slug": "first-post"} )
db.posts.insert_one({"title": "Another post", "body": "Let's try another post", "slug": "another-post", "extra-data": "something"})
db.posts.insert_one({"title": "Blog Post III", "body": "The blog post is back in another summer blockbuster", "slug": "yet-another-post", "author": "John Smith"})

db.posts.insert_one(scholarship_json)"""

db.posts.delete_many( {} )



for post in client.blog.posts.find():
    print(post) 

"""for post in client.blog.posts.find({"title": {"$eq": "Another post"}}):
    print(post["body"])"""
	
# ggg