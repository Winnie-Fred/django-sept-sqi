## Populate database for Book review Project

1. You need to make a small change to your review/models.py.
Add this function before the Book model:
```
def book_cover_upload_to(instance, filename):
    # Generate a shorter, more manageable file name
    _, ext = os.path.splitext(filename)
    return f"book_cover_images/{slugify(instance.title)}{ext}"
```

Then modify the Book model's cover_image field from
```
    cover_image = models.ImageField(upload_to="book_cover_images/")
```

to 
```
    cover_image = models.ImageField(upload_to=book_cover_upload_to)
```
We are doing this because the file names of the images are very long, so we want to shorten the names when saving them to the database.
2. Make sure you are in the book_review_resources directory in the terminal i.e. the same directory where this README.md file is contained. You may need to use the cd command.
3. Run the generate_db_population_code.py script i.e. `python generate_db_population_code.py`
4. Copy the content of the file that is generated i.e. populate_db.py
5. Go to your book_review Django project and enter the python shell with `python manage.py shell`.
6. Paste the copied content
7. Start the server and go to the admin and check the Book and Author models to confirm they have been populated with the data.
8. You can go ahead and use them in the project.