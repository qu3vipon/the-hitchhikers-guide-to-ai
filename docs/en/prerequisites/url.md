# URLs

Before sending an HTTP request, a client must decide **where to send it**. It might request the home page of `example.com`, a specific post, or information about a user.

An address identifying a server and a resource on the internet is called a **URL (Uniform Resource Locator)**. Just as you enter a URL in a browser’s address bar, an HTTP client uses it to identify the target of its request.

The `/` in our earlier `GET / HTTP/1.1` example is part of a URL. Let’s see how URLs are structured and how they fit into HTTP requests.

!!! info "Resources"
    A **resource** is something that can be identified by a URL and requested. It might be a web page, an image, a post, or another kind of data provided by a server.

## Paths {#path}

The **path** is the part of a URL beginning with `/` after the domain. It identifies the page or data you want to request.

```text
https://example.com/          → /
https://example.com/posts     → /posts
https://example.com/posts/1   → /posts/1
```

Requesting `https://example.com/` uses the `/` path, usually the home page. Requesting `/posts` might retrieve data or functionality related to posts.

## Query parameters {#query-parameters}

Sometimes a client needs to provide **additional conditions** along with a path. When requesting a list of posts, for example, it might specify a page number, sort order, or search term.

These additional values are called **query parameters**. They begin after `?` and use the form `key=value`.

<div class="url-example"><code>https://example.com/posts<span class="url-query">?page=2&amp;sort=latest</span></code></div>

Here, the path is `/posts`, and the parameters are `page=2` and `sort=latest`. An `&` separates multiple parameters.

- `page=2` requests the second page of posts.
- `sort=latest` asks for the posts in newest-first order.

Sending a parameter does not guarantee that the server will use it. The server decides which parameters it supports and how to interpret them.

!!! info "Queries"
    A **query** asks for information or retrieves data. You will also hear the term when working with databases.

## URLs in HTTP request messages {#url-in-http-request}

You normally enter a complete URL in the browser:

```text
https://example.com/posts?page=2&sort=latest
```

In a typical HTTP/1.1 request, the path and query appear in the start line, while the domain appears in the `Host` header:

```http
GET /posts?page=2&sort=latest HTTP/1.1
Host: example.com
```

- **Start line**
    - Path: `/posts`
    - Query parameters: `page=2`, `sort=latest`
- **Header**
    - Server domain: `Host: example.com`

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. A URL path identifies which page or data to request from a server.
2. A server must apply every query parameter a client sends.
3. In a typical HTTP/1.1 request, the path and query go in the start line, while the domain goes in the `Host` header.

??? success "Answers and explanations"
    1. **True** — The path identifies the requested resource or functionality.
    2. **False** — The server decides which parameters it supports and how to handle them.
    3. **True** — These parts of the URL appear in different parts of the request message.
