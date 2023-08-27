Consider this Python dictionary

{
    "menu": {
        "title": [
            "Shrinking World",
            "/"
        ],
        "items": [
            [
                "Textbooks",
                "/pubs/textbook"
            ],
            [
                "Books",
                "/pubs/book"
            ],
            [
                "Blogs",
                "/pubs/blog"
            ],
            [
                "Unpublished",
                "/pubs/private"
            ],
            [
                "Edit Content",
                "/writer/"
            ],
            [
                "Mark Seaman",
                "/marks/contact"
            ]
        ]
    }
}

Write a function that will remove the Unpublished item when "is_local_host" is false.

