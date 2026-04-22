authors_books = {
    'William Shakespeare': ['Hamlet', 'Macbeth', 'Romeo and Juliet', 'Othello'],
    'J.K. Rowling': [
        'Harry Potter and the Sorcerer\'s Stone',
        'Harry Potter and the Chamber of Secrets',
        'Harry Potter and the Prisoner of Azkaban',
        'Harry Potter and the Goblet of Fire'
    ],
    'George Orwell': ['1984', 'Animal Farm', 'Coming Up for Air'],
    'Stephen King': ['It', 'The Shining', 'Carrie', 'Misery'],
    'Agatha Christie': [
        'Murder on the Orient Express',
        'The Murder of Roger Ackroyd',
        'And Then There Were None',
        'Death on the Nile'
    ]
}

# 9. use the correct dictionary name
keys = authors_books.keys()

# 11. initialize empty list
all_books = []

# 13–15. iterate using the same loop variable
for author in keys:
    for book in authors_books[author]:
        all_books.append(book)

# 18. Testing
print("The list of all books in the library:", all_books)