# HTTP methods

Once a URL identifies **where** to send a request, we must decide **what to do** there. At the same `/posts` path, a client might want to retrieve a list of posts or create a new one.

An **HTTP method** tells the server which action the client wants. It appears at the beginning of the request’s start line.

```http
GET /posts HTTP/1.1
```

Here, `GET` is the method. The server uses `GET` together with `/posts` to identify a request for the list of posts.

## CRUD {#crud}

Web services frequently create, retrieve, change, and delete data. These four basic operations are called **CRUD**:

- **C**reate: add new data.
- **R**ead: retrieve data.
- **U**pdate: change existing data.
- **D**elete: remove data.

In a discussion forum, writing a post, reading it, editing it, and deleting it are examples of CRUD operations. HTTP methods help express these operations in requests.

CRUD describes the operation on the data. An HTTP method is the value used to express the intended action in an HTTP message.

## Common HTTP methods {#common-http-methods}

| Method | Meaning | Example |
| --- | --- | --- |
| `GET` | Retrieve data. | List posts. |
| `POST` | Create data or submit an operation for processing. | Create a post. |
| `PUT` | Replace a resource’s representation. | Replace the contents of a post. |
| `PATCH` | Change part of a resource. | Update only a post’s title. |
| `DELETE` | Delete a resource. | Delete a post. |

Different methods at the same path can identify different operations:

- `GET /posts/1` → retrieve post 1.
- `PATCH /posts/1` → update part of post 1.
- `DELETE /posts/1` → delete post 1.

## URLs and HTTP methods {#url-and-http-method}

A URL identifies **the target**, and the method identifies **the action**. An HTTP request normally combines both:

- Where should the request go? → the URL path.
- What should happen there? → the HTTP method.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. An HTTP method tells the server which action the client wants.
2. Requests to the same URL can perform different operations when their HTTP methods differ.
3. `PATCH /posts/1` can represent a request to update part of post 1.

??? success "Answers and explanations"
    1. **True** — Methods express actions such as retrieval, creation, modification, and deletion.
    2. **True** — The URL identifies the target, while the method identifies the action.
    3. **True** — `PATCH` is commonly used for partial updates.
