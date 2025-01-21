# **Django Chat Application**

**Overview**
This project is a real-time chat application built using Django and WebSockets. It allows users to sign up, log in, and engage in one-on-one chats with other registered users. The application ensures efficient communication with a user-friendly interface.

## **Features**
- **User Authentication**: Sign up and log in functionality.
- **User Directory**: View all registered users in a collapsible left menu.
- **One-on-One Chat**: Initiate private chats with any registered user.
- **Message History**: Store and retrieve chat messages from the database.
- **Real-Time Communication**: Implemented using WebSockets.
- **Responsive UI**: A user-friendly chat interface for seamless interactions.

## **Technologies Used**
- **Backend**: Django, Django Channels
- **Frontend**: HTML, CSS, JavaScript (optional: Bootstrap)
- **Database**: SQLite (default Django database)
- **WebSockets**: Channels and Redis
- **Hosting**: PythonAnywhere

## **Setup Instructions**

### Prerequisites
- Python 3.8 or higher installed on your system.
- Virtual environment tools.
- Redis server installed and running.   

**Set Up a Virtual Environment**:
   python3 -m venv env
   env\Scripts\activate      # Windows

**Install Dependencies**:
   pip install -r requirements.txt

**Configure Redis**:
   - Ensure Redis is installed and running

**Run Migrations**:
   python manage.py makemigrations
   python manage.py migrate

**Run the Development Server**:
   python manage.py runserver

**How to Use**
1. Sign up or log in using your credentials.
2. View all registered users in the left menu.
3. Click on any user to start a chat.
4. View and send messages in real-time.
