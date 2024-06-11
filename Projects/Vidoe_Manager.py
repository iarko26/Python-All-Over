import json
def read_all_videos():
    try:
        with open("Vidoes.txt",'r') as file:
            testvidoe=json.load(file)
            return testvidoe
    except FileNotFoundError:
        return []

def write_all_videos(vidoes):
    with open("Vidoes.txt",'w') as file:
        json.dump(vidoes,file)
# using lamda
def list_vidoes(vidoes):
    print("List of all the vidoes")
    for ele,vidoes in enumerate(vidoes,start=1):
        print(f"{ele}.{vidoes['title'] }  - URL: {vidoes['url']} - Duration: {vidoes['duration']}")
    print("\n\n")
        

def add_video(vidoes):

    title=input("Enter the name of the video: ")
    url=input("Enter the url of the video: ")
    duration=input("Enter the duration of the video: ")
    vidoes.append(
        {
            'title':title,
            'url':url,
            'duration':duration
        }
    )
    write_all_videos(vidoes)
    print("Video added successfully")



def update_video(vidoes):
    list_vidoes(vidoes)
    ele=int(input("Enter the number of the video you want to update: "))
    if 1<=ele<=len(vidoes):
        title=input("Enter the name of the video: ")
        url=input("Enter the url of the video: ")
        duration=input("Enter the duration of the video: ")
        vidoes[ele-1]={"title":title,"url":url,"duration":duration}

        write_all_videos(vidoes)
        print("Video updated successfully")
    else:
        print("This vidoe does not update")
        
    
def delete_video(vidoes):
    list_vidoes(vidoes)
    ele=int(input("Enter the number of the video you want to delete: "))
    if 1<=ele<=len(vidoes):
        del vidoes[ele-1]
        write_all_videos(vidoes)
        print("Video deleted successfully")
    else:
        print("This vidoe does not deleteted")
def search_video(vidoes):
    searchterm=input("Enter the name of the video you want to search: ")
    vidoe_found=False
    for ele,vidoes in enumerate(vidoes,start=1):
        if searchterm.lower() in vidoes['title'].lower():
            print(f"{ele}.{vidoes['title'] }  - URL: {vidoes['url']} - Duration: {vidoes['duration']}")
            vidoe_found=True
    if not vidoe_found:
        print("No video found with the search term")



# enter your choices
def main():

    vidoes=read_all_videos()
    while True:
        print("Welcome to the Video Manager")
        print("1. List all videos")
        print("2. Add new video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Search a video")
        print("6. Exit")
        choices=input("Enter your choice: ")

        if choices == "1":
            list_vidoes(vidoes)
        elif choices == "2":
            add_video(vidoes)
        elif choices == "3":
            update_video(vidoes)
        elif choices == "4":
            delete_video(vidoes)
        elif choices == "5":
            search_video(vidoes)
        elif choices == "6":
            break

if __name__ == "__main__":
    main()



 

