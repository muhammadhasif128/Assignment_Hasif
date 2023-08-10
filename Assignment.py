# Name: Muhammad Hasif Bin Muhammad Imran
# Admin No: 224493J
# Class: CS2202

import sys  # program exits properly, instead if break
import datetime
from tabulate import tabulate

Book_Store = {}
customer_details = {}
customer_id_list = []
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


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index][1][3] < right[right_index][1][3]:  # flip the sign to change it to descending, year published
            merged.append(left[left_index])
            left_index += 1
        elif left[left_index][1][3] > right[right_index][1][3]:
            merged.append(right[right_index])
            right_index += 1
        else:
            if left[left_index][0] <= right[right_index][0]:  # flip the sign to change it to descending, ISBN
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


def SequentialSearch(theValues, target):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
    return False

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


class Queue:
    def __init__(self):
        self._qlist = list()

    def get_qlist(self):
        return self._qlist

    def isEmpty(self):
        return len(self._qlist) == 0

    def __len__(self):
        return len(self._qlist)

    def enqueue(self, item):
        self._qlist.append(item)

    def dequeue(self):
        assert not self.isEmpty()
        return self._qlist.pop(0)

    queue_count = 0


class Customer_Request:
    def __init__(self, customer_id, name, email, tier, points):
        self.__customer_id = customer_id
        self.__name = name
        self.__email = email
        self.__tier = tier
        self.__points = points
        self.__get_req = None

    def get_customer_id(self):
        return self.__customer_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_tier(self):
        return self.__tier

    def get_points(self):
        return self.__points

    def get_get_req(self):
        return self.__get_req


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

    elif input_option == '6':
        book_list = list(Book_Store.items())
        Book_Store = dict(merge_sort(book_list))

        for i in Book_Store:
            table = [['Year Published: ', Book_Store[i][3]], ['ISBN: ', i], ['Title: ', Book_Store[i][0]], ['Publisher: ', Book_Store[i][2]], ['Category: ', Book_Store[i][1]]]
            print('\n')
            print(tabulate(table))
            print('\n')

    elif input_option == '7':
        myQueue = Queue()
        while True:
            print('')
            print('Customer Request Page: ')
            print('1. Input customer request')
            print('2. View number of request')
            print('3. Service next request in Queue')
            print('0. Return to Main Menu')
            options = input('Please select one: ')

            if options == '1':
                customer_id = input('Enter Customer ID: ')
                if len(customer_id) == 0: # space checker
                    print('Invalid Input. No empty inputs are allowed.')
                    customer_id = input('Enter Customer ID: ')
                if SequentialSearch(customer_id_list, customer_id.upper()):
                    customer_request = input('Enter Customers request: ')
                    customer_details[customer_id.upper()][4] = customer_request
                    myQueue.enqueue([customer_id.upper()] + customer_details[customer_id.upper()])
                    Queue.queue_count += 1
                else:
                    print('Customer request is invalid.')
                    customer_id = input('Enter Customer ID: ')
                print('')
                print('Pending Request') # pending request
                table = [['Customer ID: ', customer_details[customer_id.upper()][0]], ['Email: ', customer_details[customer_id.upper()][1]], ['Tier: ', customer_details[customer_id.upper()][2]], ['Points: ', customer_details[customer_id.upper()][3]], ['Request: ', customer_details[customer_id.upper()][4]]]
                print(tabulate(table))
                print('')
                print('Customers request added successfully!')
                print('')

            elif options == '2':
                print('')
                print(f'Number of request: {Queue.queue_count}')

            elif options == '3':
                print('')
                print('Customer Request Details:')
                print('')
                ct = datetime.datetime.now()
                print(f'Current time: {ct}')
                table = [['Customer ID: ', myQueue.get_qlist()[0][0]], ['Name: ', myQueue.get_qlist()[0][1]], ['Email: ',  myQueue.get_qlist()[0][2]], ['Tier: ', myQueue.get_qlist()[0][3]], ['Points: ', myQueue.get_qlist()[0][4]], ['Request: ', myQueue.get_qlist()[0][5]]]
                print(tabulate(table))
                myQueue.dequeue()
                Queue.queue_count -= 1
                print(f'Remaining request: {Queue.queue_count}')

            elif options == '0':
                break

    elif input_option == '8':
        Book_Store['9781449340377'] = ["PYTHON COOKBOOK", "EDUCATION", "OREILLY", 2014]
        Book_Store['9723418961798'] = ["I LOVE DSA", "STUDIES", "MARK", 2019]
        Book_Store['9781449342777'] = ['PYTHON COOKING', 'EDUCATION', 'OREILLY', 2015]
        Book_Store['8978111895178'] = ['ADVENTURES IN PYTHON', 'ADVENTURE', 'WILEY', 2015]

        customer_1 = Customer_Request('S111', 'John TaY', 'jtay@yahoo.com', 'C', 2000)
        customer_2 = Customer_Request('S112', 'Bob Tan', 'bob@yahoo.com', 'B', 3000)
        customer_3 = Customer_Request('S113', 'Tommy Toh', 'tommy@yahoo.com', 'D', 4000)

        customer_details[customer_1.get_customer_id()] = [customer_1.get_name(), customer_1.get_email(), customer_1.get_tier(), customer_1.get_points(), customer_1.get_get_req()]
        customer_details[customer_2.get_customer_id()] = [customer_2.get_name(), customer_2.get_email(), customer_2.get_tier(), customer_2.get_points(), customer_2.get_get_req()]
        customer_details[customer_3.get_customer_id()] = [customer_3.get_name(), customer_3.get_email(), customer_3.get_tier(), customer_3.get_points(), customer_3.get_get_req()]
        for i in customer_details:  # to get the key in the dictionary and append it into the list
            customer_id_list.append(i)

    elif input_option == '0':
        sys.exit()
    else:
        print('Error')


# tabulate is a feature, formatting feature
