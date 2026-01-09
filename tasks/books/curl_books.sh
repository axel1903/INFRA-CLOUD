#!/bin/bash

# Get all books
curl http://localhost:5000/books

# Add a new book
curl -X POST http://localhost:5000/books \
-H "Content-Type: application/json" \
-d '{"title":"DevASC Book","author":"Cisco"}'

# Delete a book (example id)
curl -X DELETE http://localhost:5000/books/1
