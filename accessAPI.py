import requests
import json


base_url = 'https://openscriptureapi.org/api/scriptures/v1/lds/en/volume/bookofmormon/'

# Function to get the summary of a specified chapter from the Book of Mormon
def get_chapter_summary(book, chapter):
    try:
        url = f"{base_url}{book}/{chapter}"
        response = requests.get(url)
        data = response.json()
        
        if response.status_code == 200 and 'summary' in data:
            return data['summary']
        else:
            return "Summary not available."
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    print("Welcome to the Book of Mormon Summary Tool!")
    
    while True:
        # Ask the user for the book and chapter
        book = input("Which book of the Book of Mormon would you like? ").replace(" ", "-").lower()
        chapter = input(f"Which chapter of {book.replace('-', ' ').title()} are you interested in? ")
        
        # Get and print the summary
        summary = get_chapter_summary(book, chapter)
        print(f"Summary of {book.replace('-', ' ').title()} chapter {chapter}:")
        print(summary)
        
        # Ask if the user wants to view another summary
        another = input("Would you like to view another (Y/N)? ").strip().upper()
        if another != 'Y':
            print("Thank you for using Book of Mormon Summary Tool!")
            break

if __name__ == "__main__":
    main()
