# Software Engineering Book Cover

## Request 

create the HTML for a book cover that is responsive 

    Title: Genetics is Amazing
    Author: Josiah Seaman and Chet Gupta
    Tag line: Enter the wonderful world of life encoding
    Cover Image: https://seamanslog.com/static/images/CoverArtwork/tech.jpg

use an overlay for text

## Response

In this code, we use CSS to make the book cover responsive by setting the maximum width to 400px and using a percentage value for the image width. We also use the viewport meta tag to ensure that the page adapts to different screen sizes. The margin property centers the book cover horizontally on the page.

We use img tag to insert the book cover image and h1, h2, and p tags to display the title, author, and tagline respectively. We also use CSS to style the different elements and set the font sizes and margins appropriately.


    <!DOCTYPE html>
    <html>
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        .book-cover {
            width: 100%;
            max-width: 400px;
            margin: 0 auto;
            text-align: center;
        }
        .book-cover img {
            width: 100%;
            height: auto;
        }
        .book-title {
            font-size: 2rem;
            font-weight: bold;
            margin-top: 1rem;
            margin-bottom: 0.5rem;
        }
        .book-author {
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
        }
        .book-tagline {
            font-size: 1.2rem;
            margin-bottom: 1rem;
        }
        </style>
    </head>
    <body>
        <div class="book-cover">
        <img src="https://seamanslog.com/static/images/CoverArtwork/tech.jpg" alt="Genetics is Amazing">
        <h1 class="book-title">Genetics is Amazing</h1>
        <h2 class="book-author">by Josiah Seaman and Chet Gupta</h2>
        <p class="book-tagline">Enter the wonderful world of life encoding</p>
        </div>
    </body>
    </html>
