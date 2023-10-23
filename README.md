<p align="center">
  <img width="300px" src="https://img.freepik.com/free-vector/hand-drawn-flat-design-stack-books-illustration_23-2149341898.jpg?w=740&t=st=1698066384~exp=1698066984~hmac=7204140b45fec26f45d3497c087bacdb74f9447f18b168abb953ed8cd9072fff" align="center" alt="GitHub Readme Stats" />

 <h1 align="center">Boi Bondhu</h2>
 <p align="center">“Boi-Bondhu”. A platform to share and recieve old bookswithin your community!</p>
</p>

## Team Members:

- Ashfaqur Rahman Adib- 1804055
- Tahlil Abrar- 1804056
- Zerin Shaima Meem- 1804057

## Contents:

- [Required Technologies](#Required-Technologies)
- [Data Base Sesign](#Data-Base-Design)
- [Book State Diagram](#Book-State-Diagram)
- [User interface](#User-Interface)
  - [Home Page](#Home-Page)
  - [How to Swap](#How-to-swap)
  - [Browse](#Browse)
  - [Blogs](#Blogs)
  - [About Us](#About-Us)
  - [Pricing Plan](#Pricing-Plan)
  - [Profile](#Profile)
  - [My Books](#My-Books)
- [Features](#Features)
  - [Sign-up](#sign-up)
  - [Log-in](#Log-in)
  - [Notification alert](#Notification-alert)
  - [Button Disable](#Button-Disable)
  - [Coupons](#Coupons)
  - [Coin Shortage](#Coin-Shortage)

## Required Technologies

- HTML
- CSS
- SASS
- JavaScript
- JQuery
- Swiper JS
- Bootstrap
- Django Python with SQLite

## Data Base Design

We used a relational database SQLite for the backend of our web application. The database
design of the website took 8 entities with their appropriate attributes. The following is the
diagram of our web application:
![Database Schema](readmeImages/DatabaseSchema.jpg)

## Book State Diagram
When a user add books as posts it has many stages which we describe in Fig 2.2 as states. This state diagram helps us to design books/user interaction. Those states are given here in the following state diagram:

![Books State Diagram](readmeImages/BooksStateDiagram.jpg)

## User interface
### Home Page
Before signup, this page will give a brief introduction about the application. When a user signs up for the first time he would be given 500 coins as a sign-up bonus.
#### Before Sign-Up
![Homepage Before Sign-Up ](readmeImages/HomePageBeforeSignup.jpg)
After Sign-Up, it will give a welcome message.
#### After Sign-Up
![Home Page After Sign-Up ](readmeImages/HomePageAfterSignUp.jpg)

### How to Swap

This page gives the brief idea of using the web application step by step. The page is divided
into 4 sections describing 4 steps of understanding to use the web application.
![How to swap page](readmeImages/HowtoSwapPage.jpg)

### Browse

This page is visible after the user creates an account. He can scroll through all available
books from the browsing page and send requests for any of them.
![Browse Page Containing All Books](readmeImages/browsePageContainingAllBooks.jpg)

#### Read More

This is a subpage of every book card. Here user can find all information about a book, its
provider or receiver. Here user can give a rating to that book.
![ Read More Containing Book Information ](readmeImages/ReadMoreContainingBookInformation.jpg)

### Blogs

This page comes with some handpicked blogs from different writers. Those blogs are selected by our editors. Those blogs are given with the intention to inspire our users into book reading.
![Blog page](readmeImages/blogPage.jpg)

### About Us

This is a page where users can learn about our goals and us, the creators of this application.
![About US Page With Developer Information](readmeImages/aboutUS.jpg)

### Pricing Plan

This page shows our pricing plans and one can submit coupons here, to buy coins. Users can
enter coupons to redeem coins which are given in many special offers.
![Pricing Plan for Different Plans.](readmeImages/PricingPlanForDifferentPlans.jpg)

### Profile

In this page all the information about the user is shown. Also, users can see how many coins
they got, the number of books received and the number of books shared. On the lower right
corner there is a button for adding books for sharing.

![User Profile Page ](readmeImages/UserProfilePage.jpg)

### Add Books

A form to upload books into the database.

![Add books Form](readmeImages/addBooksForm.jpg)

### My Books

This page holds 7 child pages. Each of those pages are given for users to keep track of their
activity with other users and different books.

#### Books Received

Shows list of books that the user received successfully already.

![The Books Received by User ](readmeImages/TheBooksReceivedbyUser.jpg)

#### Books Giveaway
Shows list of books that the user has shared till date.

![The Books Giveaway by User](readmeImages/TheBooksGiveawaybyUser.jpg)

#### My Request
Shows list of books that user have sent request for, but still isn’t accepted.
![The Books Request to Acquire by User](readmeImages/TheBooksRequesttoAcquirebyUser.jpg)

#### New Request
Shows list of books that users have received requests for, but haven’t accepted or declined yet. Users can also see who has requested that book.

![New Request of Books ](readmeImages/NewRequestofBooks.jpg)

#### Pending
Shows list of books that users have sent requests for and is accepted, but yet not received by
the user that requested.

![Pending Requests](readmeImages/PendingRequests.jpg)

#### Waiting
Shows list of books that users have been waiting for. A confirmation button is given for making sure they received the book.

![Waiting Lists of User](readmeImages/WaitingListsofUser.jpg)

#### My Posts
Shows list of books that have been posted. Users can delete them if they want to.

![Books Lists of Uploaded Books](readmeImages/booksListsOfUploadedBooks.jpg)

## Features
### Sign-Up
#### Empty Form
A new user can not submit an empty form. Every filed in the form has to be filled up. Otherwise this following pop up message will be shown.

![Sign-Up Empty Form Verdict](readmeImages/SignUpEmptyFormVerdict.jpg)

#### Existing Username

When a user inputs a username that is already in the database for other profile there will be an alert message. So, every username must be unique.

![Sign-Up Existing Username](readmeImages/SignUpExistingUsername.jpg)

#### Incorrect Password
When the password fields do not match with each other there would be shown an error message in the homepage.

![Incorrect Password Verdict](readmeImages/IncorrectUsernameorPassword.jpg)

#### Password Too Short
If the password match and then the password length is less than 8 characters this error message would be shown.

![Too Short Password](readmeImages/TooShortPassword.jpg)

### Log-In
If an existing user incorrectly enter his username or password this verdict will be shown.

![Incorrect Username or Password](readmeImages/IncorrectUsernameorPassword.jpg)

### SEARCH RESULT
#### Keyword Searching
A user can search for different types of books by entering keywords in the search bar. The books with that keyword in their title will be shown.

![Keyword Search Result](readmeImages/KeywordSearchResult.jpg)

#### No Result found
If a user enters a keyword that doesn’t match with any of the books in database than their will be shown “No Result Found”.

![No result found](readmeImages/NoResultFound.jpg)

### Notification Alert
For a book request from other users a notification will be shown in top of the page.

![Notification Alert](readmeImages/NotificationAlert.jpg)

### Button Disable
When a user tries to request any books from browsing page without logged in, they can’t do it. The buttons will be disable for them. Similar thing happened when an owner also tries to request his own book.

![Button Disable](readmeImages/ButtonDisable.jpg)

### Cupons
#### Coin Addition
When a user input correct coupon then the user will get his confirmation message. An automatically coin will be added in their vault.

![Confirmation of Purchase](readmeImages/ConfirmationofPurchase.jpg)

#### Incorrect Coupon
When a user adds incorrect coupon in the coupon bar then an error message indicate that the coupon is not currently available.

![Coupon Unavailable](readmeImages/CouponUnavailable.jpg)

### Coin Shortage
When a user tries to request a book whose coin price is greater than his currently held coins than the request wouldn’t be performed and the following verdict will be shown.

![Shortage of Coins](readmeImages/ShortageofCoins.jpg)
