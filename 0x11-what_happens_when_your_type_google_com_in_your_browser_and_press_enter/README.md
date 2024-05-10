# What Happens When You Type "google.com" in Your Browser and Press Enter

## Introduction
This question is a classic and widely used interview question for many types of software engineering positions. It assesses a candidate’s general knowledge of how the web stack works on top of the internet. In this blog post, we'll dive into the various stages involved when you type "https://www.google.com" in your browser and press Enter.

### Overview
We'll cover the following aspects:
- DNS request
- TCP/IP
- Firewall
- HTTPS/SSL
- Load-balancer
- Web server
- Application server
- Database

## DNS Request
When you type "https://www.google.com" in your browser, the first step is the DNS (Domain Name System) resolution. Your browser sends a DNS request to a DNS server to resolve the domain name "www.google.com" into an IP address.

## TCP/IP
Once the DNS resolution is complete, your browser establishes a TCP (Transmission Control Protocol) connection with the IP address obtained from the DNS server. TCP is responsible for ensuring reliable communication between the client (your browser) and the server (Google's server).

## Firewall
The TCP connection passes through firewalls, which are network security devices that monitor and control incoming and outgoing network traffic based on predetermined security rules.

## HTTPS/SSL
Before any data is transmitted over the TCP connection, the browser and the server negotiate an HTTPS (Hypertext Transfer Protocol Secure) connection using SSL (Secure Sockets Layer) or its successor TLS (Transport Layer Security). This ensures that the data exchanged between the browser and the server is encrypted and secure from eavesdropping.

## Load-balancer
The HTTPS request may be directed to a load balancer, which distributes incoming traffic across multiple servers to ensure optimal resource utilization and high availability.

## Web Server
Once the request reaches the appropriate server, typically a web server like Apache or Nginx, it is processed. The web server retrieves the requested web page and any associated resources (such as HTML, CSS, JavaScript, images) from the file system or cache.

## Application Server
For dynamic content or functionality, the web server may forward the request to an application server. The application server executes code (e.g., Python, Ruby, PHP) to generate the web page dynamically based on the request parameters.

## Database
If the application server needs to retrieve or store data, it interacts with a database server (e.g., MySQL, PostgreSQL, MongoDB) to perform CRUD (Create, Read, Update, Delete) operations.

## Conclusion
In summary, when you type "https://www.google.com" in your browser and press Enter, a series of steps involving DNS resolution, TCP/IP connection establishment, firewall traversal, HTTPS negotiation, load balancing, web server processing, application server execution, and database interaction occur seamlessly to deliver the requested web page to your browser.

---

## Everything's Better with a Pretty Diagram
![Request Flow Diagram](https://example.com/request_flow_diagram.png)

---

## Contribute!
Folks on the Internet have been trying to put together a comprehensive answer to the question. You can contribute by submitting a pull request to the [What Happens When](https://github.com/alex/what-happens-when) repository on GitHub.

Pull Request: [Link to your Pull Request](https://github.com/alex/what-happens-when/pull/123)

---

## URLs
- **Blog Post:** [Medium](https://medium.com/your-blog-post)
- **Diagram Image:** [Request Flow Diagram](https://example.com/request_flow_diagram.png)
- **Contribution:** [Pull Request](https://github.com/alex/what-happens-when/pull/123)
