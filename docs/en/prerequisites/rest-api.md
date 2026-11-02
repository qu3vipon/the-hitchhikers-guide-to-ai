# REST APIs

We have learned that a URL identifies a target and an HTTP method identifies an action. Together, they help define how a client can interact with a server. That interaction is part of an **API**.

## What is an API? {#what-is-api}

An **API (Application Programming Interface)** is **an interface that lets one program use another program’s data or functionality**.

!!! info "Interfaces"
    An **interface** is a set of interaction points and rules between systems.

    Think of an elevator’s buttons and indicator lights. You press a button to choose a floor, and the elevator communicates its state through the display and doors. These controls form an interface between you and the elevator.

For a web API, the client sends requests using URLs and methods defined by the server. The server responds in an agreed format.

```mermaid
flowchart LR
    client[Client app] -.- api{{"API<br/>URL · Method · Data format"}}
    api -.- server[Server]

    classDef client fill:transparent,stroke:#8eb7c2,stroke-width:2px
    classDef server fill:transparent,stroke:#d0a476,stroke-width:2px
    classDef api fill:transparent,stroke:#9a7655,stroke-width:2px,color:#9a7655
    class client client
    class server server
    class api api
```

Here are some everyday uses of APIs:

- **Discussion forum:** a client requests a list of posts, and the server returns post data.
- **Weather service:** an app sends a location, and the server returns the weather there.
- **Shopping service:** an app requests products or stock levels, and the server returns the relevant information.

## REST APIs {#what-is-rest-api}

Consistent URLs and HTTP methods make an API easier to use. Without consistent conventions, clients have to learn an unrelated set of rules for every operation.

**REST (Representational State Transfer)** is an architectural style for designing networked systems. Web APIs commonly borrow REST conventions to organize resources and interactions consistently. The naming guidelines below are useful conventions, rather than a complete definition of REST.

### REST API design guidelines {#rest-rules}

1. **Use nouns to identify resources in URLs.**

    Name the resource rather than the action. For posts, use `/posts`. Express actions such as creation, retrieval, updates, and deletion through HTTP methods.

    - Prefer: `/posts`
    - Avoid: `/create-post`, `/get-posts`

2. **Use plural nouns for collections.**

    Use `/posts` for the collection and `/posts/1` for an individual post.

3. **Represent relationships through URL hierarchy.**

    `/users/1/posts` can identify posts written by user 1.

4. **Use HTTP methods to express actions.**

    At `/posts`, `GET` retrieves posts while `POST` can create a new one.

5. **Use action names where a resource-based design would be awkward.**

    Operations such as signing in or canceling an order do not always fit naturally into basic CRUD. Pragmatic APIs may use paths such as `POST /auth/login` or `POST /orders/1/cancel`. Reserve action-oriented URLs for cases where they make the interface clearer.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. A web API defines how clients and servers exchange data or use functionality over the web.
2. REST-style URLs must include actions such as `create-post` and `delete-post`.
3. `GET /posts` and `POST /posts` are different requests even though they share a path.

??? success "Answers and explanations"
    1. **True** — An API defines how one program can use another’s data or functionality.
    2. **False** — URLs usually identify resources, while HTTP methods express actions.
    3. **True** — The target is the same, but the requested action differs.
