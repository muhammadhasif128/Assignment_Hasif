import sys  # program exits properly, instead if break

Book_Store = {'9781449340377': ["Python Cookbook", "Education", "Oreilly", 2013], '9781118951798': ["Adventures in Python", "Adventure", "Wiley", 2015]}

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
        smallNdx = i  # smallNdx = small index
        for j in range(i+1, n):
            if theSeq[j][1][2] > theSeq[smallNdx][1][2]:
                smallNdx = j
        if smallNdx != i:  # swapping of indexes
            tmp = theSeq[i]
            theSeq[i] = theSeq[smallNdx]
            theSeq[smallNdx] = tmp


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
    print("[5] ----- Exit Book Management System ----- \n")
    input_option = input("Please enter your option :) \n[1]-[5]: ")

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
                    print("Duplicate entries.\nEnter Again.")
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

            year_published = int(input("Enter book's year of published: "))
            while True:
                if year_published < 1900 or len(str(year_published)):
                    print("Year published doesn't exist/invalid year format!\nKey in again\n")
                    year_published = input("Enter book's year of published: ")
                else:
                    break

            book_ISBN = Book(ISBN, title, category, publisher, year_published)
            Book_Store[book_ISBN.get_isbn()] = [book_ISBN.get_title(), book_ISBN.get_category(), book_ISBN.get_publisher(), book_ISBN.get__year_published()]
            break

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

    elif input_option == '5':
        sys.exit()
    else:
        print('Error')
