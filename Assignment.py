# Name: Muhammad Hasif Bin Muhammad Imran
# Admin No: 224493J
# Class: CS2202

import sys  # program exits properly, instead if break
from tabulate import tabulate

Book_Store = {'9781449340377': ["Python Cookbook", "Education", "Oreilly", 2013], '9781118951798': ["Adventures in Python", "Adventure", "Wiley", 2015], '9723428951798': ["I love DSA", "Studies", "Mark", 2019]}

# first list, is the list, value of the list
# key, value

# 2 sorting functions


def ascending_bubble(theSeq):
    n = len(theSeq)
    for i in range(n - 1, 0, -1):  # all the ranges are for counting the index, start(reverse, from the back), stop(0, go from back to front), step(go backwards)
        for j in range(i):
            if theSeq[j][1][1] > theSeq[j + 1][1][1]:  # [] dictionary list, next one index of the list, if want to change to descending just flip the sign
                tmp = theSeq[j]
                theSeq[j] = theSeq[j+1]
                theSeq[j + 1] = tmp  # tmp = temporary


def descending_selection(theSeq):
    n = len(theSeq)
    for i in range(n - 1):
        highNdx = i  # highNdx = high index
        for j in range(i+1, n):
            if theSeq[j][1][2] > theSeq[highNdx][1][2]:
                highNdx = j
        if highNdx != i:  # swapping of indexes
            tmp = theSeq[i]
            theSeq[i] = theSeq[highNdx]
            theSeq[highNdx] = tmp


def insertion_sort(theSeq):
    n = len(theSeq)
    for i in range(1, n):
        value = theSeq[i][1][0]

        pos = i
        while pos > 0 and value < theSeq[pos - 1][1][0]:
            theSeq[pos][1][0] = theSeq[pos - 1][1][0]
            pos -= 1

        theSeq[pos][1][0] = value



# Class Creation
class Book:

    def __init__(self, ISBN, Title, Category, Publisher, Year_Published):
        self.__ISBN = ISBN
        self.__Title = Title
        self.__Category = Category
        self.__Publisher = Publisher
        self.__Year_Published = Year_Published

    def get_isbn(self):
        return self.__ISBN

    def get_title(self):
        return self.__Title

    def get_category(self):
        return self.__Category

    def get_publisher(self):
        return self.__Publisher

    def get__year_published(self):
        return self.__Year_Published


while True:
    print("Welcome to Books!\nA retail store that sells books.\nWe will help keep track of your books with our Book Management System.\nKindly choose your option below:\n")
    print("[1] ----- Displaying all your books ----- ")
    print("[2] ----- Adding new books ----- ")
    print("[3] ----- Sort books by category in ascending order using ONLY bubble sort and display the outcome ----- ")
    print("[4] ----- Sort the publisher in descending order using ONLY selection sort and display the outcome ----- ")
    print("[5] ----- Sort books by Title in ascending order using insertion sort and display ----- ")
    print("[6] ----- Sort books by Year published and then ISBN in ascending order using Merge sort and display ----- ")
    print("[7] ----- Manage customer request")
    print("[8] ----- Populate data")
    print("[0] ----- Exit Book Management System ----- \n")
    input_option = input("Please enter your option :) \n[1]-[9] and [0]: ")

    if input_option == '1':
        for keys in Book_Store:
            print(f"ISBN: {keys}")
            print(f"Title: {Book_Store[keys][0]}")
            print(f"Category: {Book_Store[keys][1]}")
            print(f"Publisher: {Book_Store[keys][2]}")
            print(f"Year Published:{Book_Store[keys][3]}\n")

    elif input_option == '2':
            ISBN = input("Enter book ISBN: ")
            while True:
                if ISBN in Book_Store or len(ISBN) != 13:
                    print("Duplicate entries OR less than 13 characters\nEnter Again.")
                    ISBN = input("Enter book ISBN: ")
                else:
                    break

            title = input("Enter book title: ")
            while True:
                if len(title) == 0:
                     print("Title should be in Words. Enter Again\n")
                     title = input("Enter book title: ")
                else:
                    break

            category = input("Enter book category: ")
            while True:
                if len(category) == 0:
                    print("Category should be in Words. Enter Again\n")
                    category = input("Enter book category: ")
                else:
                    break

            publisher = input("Enter book publisher: ")
            while True:
                if len(publisher) == 0:
                    print("Publisher should be in Words. Enter Again\n")
                    publisher = input("Enter book publisher: ")
                else:
                    break

            while True:
                year_published = input("Enter book's year of published: ")
                if not year_published.isdigit() or not 1900 <= int(year_published) <= 2023:
                    print("Year published doesn't exist/invalid year format!\nKey in again\n")
                else:
                    break

            book_ISBN = Book(ISBN, title, category, publisher, year_published)
            Book_Store[book_ISBN.get_isbn()] = [book_ISBN.get_title(), book_ISBN.get_category(), book_ISBN.get_publisher(), book_ISBN.get__year_published()]

    elif input_option == '3':  # category, ascending, small to big
        book_list = list(Book_Store.items())  # ask dong en
        ascending_bubble(book_list)
        Book_Store = dict(book_list)

        for i in Book_Store:
            print(f"Category: {Book_Store[i][1]}")
            print(f"ISBN: {i}")
            print(f"Title: {Book_Store[i][0]}")
            print(f"Publisher: {Book_Store[i][2]}")
            print(f"Year Published:{Book_Store[i][3]}\n")

    elif input_option == '4':  # publisher, descending, big to small
        book_list = list(Book_Store.items())
        descending_selection(book_list)
        Book_Store = dict(book_list)

        for i in Book_Store:
            print(f"Publisher: {Book_Store[i][2]}")
            print(f"ISBN: {i}")
            print(f"Title: {Book_Store[i][0]}")
            print(f"Category: {Book_Store[i][1]}")
            print(f"Year Published: {Book_Store[i][3]}\n")

    elif input_option == '5': # sort by title in ascending order, small to big, using insertion sort
        book_list = list(Book_Store.items())
        insertion_sort(book_list)
        Book_Store = dict(book_list)

        for i in Book_Store:
            table = [Book_Store[i][0], Book_Store[i][2], Book_Store[i][1], i, Book_Store[i][3]],
            print("\n")
            print(tabulate(table, headers=["Title", "Publisher", "Category", "ISBN", "Year Published"]))
            print("\n")

    elif input_option == '0':
        sys.exit()
    else:
        print('Error')
