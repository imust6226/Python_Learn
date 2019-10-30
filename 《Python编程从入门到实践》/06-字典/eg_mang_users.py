#coding = utf-8

users = {

    'aeinstein':{
        'first':'albert',
        'last':'einstein',
        'location':'princeton'
        },
    
    'mcure':{
        'first':'marie',
        'last':'curie',
        'location':'paris'
        }

    }

for username, userinfo in users.items():
    print("\nUsername:" + username.title())
    full_name = userinfo['first'] + " " + userinfo['last']
    location = userinfo['location']


    print("\tFull name:" + full_name.title())
    print("\tLocation:" + location.title())
