# HTTP 상태 코드

클라이언트가 서버에 HTTP 요청을 보내면, 서버는 응답 메시지로 처리 결과를 알려 줍니다. 이때 서버는 요청의 처리 결과를 쉽게 알 수 있도록 세 자리 숫자 코드를 함께 반환합니다. 이를 **HTTP 상태 코드(Status Code)**라고 합니다. 

상태 코드는 요청이 성공했는지, 클라이언트의 요청에 문제가 있었는지, 서버에서 오류가 발생했는지 등을 나타냅니다. 클라이언트는 상태 코드를 보고 다음 동작을 결정할 수 있습니다. 예를 들어 `200`을 받으면 응답 데이터를 화면에 보여 주고, `404`를 받으면 요청한 데이터를 찾을 수 없다는 안내를 표시할 수 있습니다.

예를 들어 서버가 요청을 성공적으로 처리했다면 응답 메시지의 시작 줄은 아래처럼 시작합니다.

```http
HTTP/1.1 200 OK
```

여기서 `200`이 상태 코드이고, `OK`는 그 의미를 사람이 읽기 쉽게 나타낸 상태 메시지입니다.

## 상태 코드 분류 {#status-code-categories}

HTTP 상태 코드는 첫 번째 숫자에 따라 크게 다섯 가지 범주로 나뉩니다.

| 범주 | 의미 | 예시 |
| --- | --- | --- |
| `1xx` | 요청 처리 중 보내는 임시 정보 | `101 Switching Protocols` |
| **`2xx`** | **요청 처리 성공** | `200 OK`, `201 Created` |
| `3xx` | 다른 주소로 이동 | `301 Moved Permanently` |
| **`4xx`** | **클라이언트 요청에 문제가 있음** | `400 Bad Request`, `404 Not Found` |
| **`5xx`** | **서버 오류** | `500 Internal Server Error` |

`1xx`와 `3xx` 상태 코드는 연결 과정이나 다른 주소로의 이동에 주로 사용되며, 웹 브라우저나 HTTP 클라이언트 라이브러리가 자동으로 처리하는 경우가 많습니다. 따라서 웹 API를 만들 때는 주로 `2xx`, `4xx`, `5xx` 상태 코드를 직접 다루게 됩니다.

## 자주 사용하는 상태 코드 {#common-status-codes}

| 상태 코드 | 의미 | 사용 예시 |
| --- | --- | --- |
| <span class="http-status-code http-status-code--success"><code>200 OK</code></span> | 요청을 성공적으로 처리함 | 게시글 목록 또는 특정 게시글 조회 |
| <span class="http-status-code http-status-code--success"><code>201 Created</code></span> | 새로운 자원을 성공적으로 생성함 | 새 게시글 또는 회원 가입 생성 |
| <span class="http-status-code http-status-code--success"><code>204 No Content</code></span> | 요청은 성공했지만 응답 본문이 없음 | 게시글 삭제 성공 |
| <span class="http-status-code http-status-code--client-error"><code>400 Bad Request</code></span> | 요청 형식이나 값이 올바르지 않음 | 잘못된 형식의 데이터를 전송 |
| <span class="http-status-code http-status-code--client-error"><code>401 Unauthorized</code></span> | 인증 정보가 없거나 올바르지 않음 | 로그인하지 않은 사용자가 인증이 필요한 API 요청 |
| <span class="http-status-code http-status-code--client-error"><code>403 Forbidden</code></span> | 인증은 되었지만 권한이 없음 | 일반 사용자가 관리자 전용 API 요청 |
| <span class="http-status-code http-status-code--client-error"><code>404 Not Found</code></span> | 요청한 자원을 찾을 수 없음 | 존재하지 않는 게시글 조회 |
| <span class="http-status-code http-status-code--client-error"><code>422 Unprocessable Content</code></span> | 요청 형식은 맞지만 데이터 검증에 실패함 | 필수 값이 빠진 게시글 생성 요청 |
| <span class="http-status-code http-status-code--server-error"><code>500 Internal Server Error</code></span> | 서버가 요청을 처리하는 중 예상하지 못한 오류가 발생함 | 서버 코드의 오류 또는 처리 실패 |
| <span class="http-status-code http-status-code--server-error"><code>502 Bad Gateway</code></span> | 서버가 다른 서버로부터 올바른 응답을 받지 못함 | 프록시 서버가 뒤쪽 서비스와 통신 실패 |
| <span class="http-status-code http-status-code--server-error"><code>503 Service Unavailable</code></span> | 서버가 일시적으로 요청을 처리할 수 없음 | 서버 점검 또는 과도한 트래픽 |

## REST API 상태 코드 {#rest-api-and-status-codes}

REST API에서는 요청 결과에 맞는 상태 코드를 응답하는 것도 중요합니다. 상태 코드만 보아도 클라이언트가 요청 결과를 빠르게 파악할 수 있기 때문입니다.

| HTTP 요청 | 성공 상태 코드 | 의미 |
| --- | --- | --- |
| `GET /posts` | `200 OK` | 게시글 목록을 성공적으로 조회함 |
| `GET /posts/1` | `200 OK` | 1번 게시글을 성공적으로 조회함 |
| `POST /posts` | `201 Created` | 새 게시글을 성공적으로 생성함 |
| `DELETE /posts/1` | `204 No Content` | 1번 게시글을 성공적으로 삭제함 |

반대로 존재하지 않는 게시글에 `GET /posts/999` 요청을 보내면 서버는 `404 Not Found`를 응답할 수 있습니다.

## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. `200 OK`는 서버가 요청을 성공적으로 처리했다는 뜻이다.
2. `404 Not Found`는 서버 내부에서 예상하지 못한 오류가 발생했다는 뜻이다.
3. `401 Unauthorized`는 사용자가 인증되었지만 해당 작업의 권한이 없다는 뜻이다.

??? success "정답·해설"
    1. **O** — `200 OK`는 요청이 성공적으로 처리되었음을 나타냅니다.
    2. **X** — `404 Not Found`는 요청한 자원을 찾을 수 없다는 뜻입니다. 서버 내부의 예상하지 못한 오류는 보통 `500 Internal Server Error`를 사용합니다.
    3. **X** — `401 Unauthorized`는 인증 정보가 없거나 올바르지 않은 경우입니다. 인증은 되었지만 권한이 없는 경우는 `403 Forbidden`을 사용합니다.
