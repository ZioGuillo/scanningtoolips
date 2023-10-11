# Server Scanning Tool and Root Directory Checker

This is a simple web application built with Flask that allows you to fetch the "Server" header from a website and check the status of its root directory. You can use it to inspect the server headers of a website and determine whether its root directory is accessible.

## Installation

To run this application, you need to have Python and Flask installed. If you don't have Flask installed, you can do so using `pip`. It's also recommended to set up a virtual environment to manage dependencies.

Clone or download the repository to your local machine.

   ```bash
   git clone https://github.com/yourusername/scanningtoolips.git

   ```

```cd scanningtoolips```

Create a virtual environment (optional but recommended).

```python -m venv venv```

Activate the virtual environment (Linux/Mac):

```source venv/bin/activate```

Activate the virtual environment (Windows):

```venv\Scripts\activate```

Install the required Python packages.

```pip install -r requirements.txt```

## Usage

Run the Flask application.

```python app.py```

Open your web browser and access the application at ```http://127.0.0.1:5000```

Enter a URL in the "Enter URL" input field.

Click the "Fetch Headers" button to retrieve the "Server" header from the specified URL.

The application will also display whether the root directory of the website is accessible or not.

![Alt text](<test_screen.png>)

### Example:

Here's an example of how to use the application:

Open your web browser.

Access the application at http://127.0.0.1:5000.

Enter the URL https://google.com in the "Enter URL" input field.

Click the "Fetch Headers" button.

The application will display the "Server" header and indicate whether the root directory is accessible.

![Alt text](<demo01.png>)

![Alt text](<demo02.png>)

## Dependencies
Flask
Requests
Beautiful Soup (for web scraping)

### Contributing
Contributions and improvements are welcome! Please fork this repository and submit a pull request with your changes.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy exploring server headers and root directories with this simple web application!