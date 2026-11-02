# HTTP status codes

When a client sends an HTTP request, the server describes the outcome in its response. A three-digit **HTTP status code** gives the client a quick way to understand that outcome.

The code can indicate success, a problem with the request, or a server error. The client can use it to decide what to do next: display the returned data after `200`, for example, or show a “not found” message after `404`.

A successful response might begin like this:

```http
HTTP/1.1 200 OK
```

`200` is the status code. `OK` is a human-readable description of it.

## Status code categories {#status-code-categories}

The first digit places the code in one of five categories.

| Category | Meaning | Examples |
| --- | --- | --- |
| `1xx` | Informational response during processing | `101 Switching Protocols` |
| **`2xx`** | **Success** | `200 OK`, `201 Created` |
| `3xx` | Redirection or related response handling | `301 Moved Permanently` |
| **`4xx`** | **Client error** | `400 Bad Request`, `404 Not Found` |
| **`5xx`** | **Server error** | `500 Internal Server Error` |

Browsers and HTTP libraries often handle informational responses and redirects automatically. When building web APIs, you will most often explicitly work with `2xx`, `4xx`, and `5xx` codes.

## Common status codes {#common-status-codes}

| Status code | Meaning | Example |
| --- | --- | --- |
| <span class="http-status-code http-status-code--success"><code>200 OK</code></span> | The request succeeded. | Retrieve a list of posts or an individual post. |
| <span class="http-status-code http-status-code--success"><code>201 Created</code></span> | A new resource was created. | Create a post or a user account. |
| <span class="http-status-code http-status-code--success"><code>204 No Content</code></span> | The request succeeded with no response body. | Delete a post successfully. |
| <span class="http-status-code http-status-code--client-error"><code>400 Bad Request</code></span> | The request is malformed or invalid. | Send incorrectly formatted data. |
| <span class="http-status-code http-status-code--client-error"><code>401 Unauthorized</code></span> | Authentication is missing or invalid. | Call an authenticated API without valid credentials. |
| <span class="http-status-code http-status-code--client-error"><code>403 Forbidden</code></span> | The server refuses the operation, often because permission is missing. | A regular user calls an admin-only API. |
| <span class="http-status-code http-status-code--client-error"><code>404 Not Found</code></span> | The resource could not be found. | Request a nonexistent post. |
| <span class="http-status-code http-status-code--client-error"><code>422 Unprocessable Content</code></span> | The content is understood but fails semantic validation. | Submit a post without a required field. |
| <span class="http-status-code http-status-code--server-error"><code>500 Internal Server Error</code></span> | An unexpected server error occurred. | A bug prevents the server from completing a request. |
| <span class="http-status-code http-status-code--server-error"><code>502 Bad Gateway</code></span> | A gateway received an invalid response from an upstream server. | A proxy receives a malformed upstream response. |
| <span class="http-status-code http-status-code--server-error"><code>503 Service Unavailable</code></span> | The server is temporarily unable to handle the request. | Maintenance or excessive traffic. |

## Status codes in REST APIs {#rest-api-and-status-codes}

Returning an appropriate code helps the client understand the result without having to interpret the response body first.

| Request | Success code | Meaning |
| --- | --- | --- |
| `GET /posts` | `200 OK` | The list of posts was retrieved. |
| `GET /posts/1` | `200 OK` | Post 1 was retrieved. |
| `POST /posts` | `201 Created` | A new post was created. |
| `DELETE /posts/1` | `204 No Content` | Post 1 was deleted. |

By contrast, `GET /posts/999` might return `404 Not Found` if that post does not exist.

## :material-pencil: Exercises {#exercises}

Decide whether each statement is **True** or **False**.

1. `200 OK` means the server handled the request successfully.
2. `404 Not Found` means an unexpected internal server error occurred.
3. `401 Unauthorized` means the user is authenticated but lacks permission for the action.

??? success "Answers and explanations"
    1. **True** — `200 OK` indicates a successful request.
    2. **False** — `404` means the requested resource was not found. Unexpected internal errors usually use `500`.
    3. **False** — `401` means authentication is missing or invalid. An authenticated user lacking permission typically receives `403 Forbidden`.
