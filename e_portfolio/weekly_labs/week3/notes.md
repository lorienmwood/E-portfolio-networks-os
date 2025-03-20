# Networks and Operating Systems - Application Layer in Networks 

## Notes
- This Lab we looked at the application layer and how to implement basic network applications. 

### 1. Introduction to the Application Layer 
- The application layer is the top layer of the TCP/IP model.
- The application layer manages communication between applications e.g. HTTP 
- Uses the client-server model for network interactions.

### 2. Basic Python socket examples
- To find a website IP we use socket.gethostbyname()
- Tracert (short for "trace route") is a command-line utility used to check network paths. 
- Tracert helps identify bottlenecks and network delays.

### 3. Building a Simple HTTP Client
- Uses sockets to send an HTTP GET request to a server.
- Receives and prints the response (HTML content).

### 4. Python Requests Library
- The requests library makes web requests simpler than raw sockets.
- They handle headers, cookies, and HTTPS automatically.

### 5. HTTP Request Types
- The HTTP requests types are: 
    - GET: Fetch data. e.g loading a page 
    - POST: Send data (e.g., form submission). e.g. submitting a form 
    - PUT: Update existing data. e.g. editing a blog post
    - DELETE: Remove data. e.g. deleting a user account

## Exercises
- Exercise 1: Try 3 websites and report their IP addresses.
- Exercise 2: Experiment with 3 different domain names and IP addresses to see the trace route information.
- Exercise 3: Analyse the output of tracert.
- Exercise 4: Identify potential bottlenecks or slow points in the network path for each domain.
- Exercise 5: Experiment trace routes to the same domain from different locations (if possible) to see how the paths might vary.

 
