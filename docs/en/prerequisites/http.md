# HTTP

Clients and servers exchange data, but they cannot communicate effectively if they each use a different message format. A client might be an iOS or Android app, while the server runs Python or Java on Linux.

To exchange data across these different systems and languages, they need shared rules for formatting requests and responses.

## What is HTTP? {#what-is-http}

**HTTP (HyperText Transfer Protocol)** defines **rules for exchanging data between clients and servers on the web**. When they format their requests and responses according to those rules, we say they are communicating over HTTP.

## Browsers and HTTP {#browser-and-http}

You are already using HTTP. The page you are reading appeared because your browser requested it from a server and displayed the response. Copy its address and inspect it: it starts with something like `https://ai.qu3vipon.com/...`. The `https://` prefix means the browser is communicating over HTTPS.

!!! info "HTTPS"
    HTTPS adds a security protocol called TLS to HTTP. It encrypts the data in transit, while keeping the same basic request-response model. The HTTP concepts in this guide also apply to HTTPS. We explain the security features in [HTTPS](https.md).

## Making an HTTP request {#make-http-request}

Open a new browser window and enter `http://example.com`. A simple web page appears. You only entered an address, but your browser sent an HTTP request to the `example.com` server and displayed its response.

<img src="../assets/images/prerequisites/07-exampledotcom.png" alt="The Example Domain page open in a browser" class="example-domain-image">

A web browser is a client program that sends HTTP requests and displays responses **so that people can use web services easily**. That is why you have been able to use the web without thinking about its communication rules.

## Making a request from the terminal {#make-http-request-in-terminal}

Now request the same address from the terminal. **curl** is a command-line client that sends HTTP requests and receives responses.

=== "macOS"

    ```shell
    curl example.com
    ```

=== "Windows PowerShell"

    ```powershell
    curl.exe example.com
    ```

<img src="../assets/images/prerequisites/07-curl.png" alt="Running curl example.com in a terminal" class="terminal-image">

The terminal prints a long block of unfamiliar text. This is the source of the page you just saw in the browser. Look closely and you will find `Example Domain` in it. We will explore what this text means next.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. Programs written in different languages and running on different operating systems cannot exchange data.
2. HTTPS works so differently from HTTP that the HTTP request-response model does not apply.
3. Both a browser and `curl` can send HTTP requests to a server.

??? success "Answers and explanations"
    1. **False** — Shared rules such as HTTP allow different programs and operating systems to communicate.
    2. **False** — HTTPS adds TLS security to HTTP while retaining its request-response model.
    3. **True** — Both are client programs that send requests and receive responses.
