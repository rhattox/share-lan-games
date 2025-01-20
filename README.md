# share-lan-games
Little python script to share save lan games across friends


```
pip install -r requirements.txt
```


# Google Cloud 

1. Create a new IAM Account, it will create a new service account with a specific email, keep it in mind. -- Nothing special just the name and its ID.
2. Save the .json file as token.json 
3. Go to the Drive 
4. Create a folder
5. Copy its id, within the URL, it's the string after `folders/`
6. Share this new folder that you've create on step 4 with the service account email that you have create on step 1. 
7. Enable Google Drive API on cloud console.



# How to Use it?

1. Need the token.json file
tokne.json will have the information about the service account user created previously

2. Need .env file

.env file will have the parent folder ID, like so:

PARENT_FOLDER_ID="<string>"