# REST API

앞에서 URL은 요청할 대상을, HTTP Method는 요청할 동작을 나타낸다고 배웠습니다. 이 두 가지를 조합하면 클라이언트와 서버가 데이터를 주고받기 위한 약속을 만들 수 있습니다. 이러한 약속을 **API**라고 합니다.

## API란? {#what-is-api}

API(Application Programming Interface)는 **서로 다른 프로그램끼리 데이터나 기능을 사용할 수 있도록 정해 둔 인터페이스**입니다.

!!! info "Interface"
    서로 다른 시스템이 데이터를 주고받거나 기능을 사용하기 위해 정해 둔 접점과 규칙을 인터페이스(Interface)라고 합니다.

    예를 들어 엘리베이터의 버튼과 표시등은 사람과 엘리베이터가 상호작용하기 위한 인터페이스입니다. 사람은 버튼을 눌러 원하는 층을 전달하고, 엘리베이터는 표시등과 문 열림으로 결과를 알려줍니다.

웹에서는 클라이언트가 서버가 미리 정해 둔 URL과 HTTP Method에 맞춰 HTTP 요청을 보내고, 서버는 약속된 형식으로 응답을 돌려주는 방식으로 API를 활용합니다.

```mermaid
flowchart LR
    client[클라이언트 앱] -.- api{{"API<br/>URL · Method · 데이터 형식"}}
    api -.- server[서버]

    classDef client fill:transparent,stroke:#8eb7c2,stroke-width:2px
    classDef server fill:transparent,stroke:#d0a476,stroke-width:2px
    classDef api fill:transparent,stroke:#9a7655,stroke-width:2px,color:#9a7655
    class client client
    class server server
    class api api
```

실제 서비스에서는 다음과 같은 방식으로 API를 활용합니다.

- 게시판 서비스: 클라이언트가 게시글 목록 API를 요청하면, 서버는 게시글 데이터를 응답합니다.
- 날씨 서비스: 날씨 앱이 현재 위치를 API로 전달하면, 날씨 서버는 해당 위치의 날씨 정보를 응답합니다.
- 쇼핑 서비스: 쇼핑 앱이 상품 목록이나 재고를 API로 요청하면, 서버는 상품 정보를 응답합니다.

## REST API {#what-is-rest-api}

API를 설계할 때는 URL과 HTTP Method를 일관된 기준으로 작성해야 합니다. 일관된 기준 없이 API를 생성한다면, API를 사용하는 클라이언트가 요청 방법을 예측하기 어렵고, 서버와의 약속도 복잡해지기 때문입니다.

그래서 웹 API를 일관되게 설계하기 위한 대표적인 방식으로 **REST(Representational State Transfer)**라는 방식이 주로 사용됩니다. REST는 엄격한 규칙은 아니고, API를 일관된 방식으로 설계하자는 일종의 제안에 가깝습니다.

### REST API 설계 원칙 {#rest-rules}

REST API를 설계할 때는 URL과 HTTP Method를 일관된 방식으로 작성하는 것이 좋습니다. 이를 위해 보통 아래와 같은 설계 원칙을 따릅니다.

1. **URL에는 자원을 나타내는 명사를 사용합니다.**

    URL에는 동작 대신 다루려는 자원의 이름을 사용합니다. 예를 들어 게시글을 다루는 API라면 `/posts`처럼 표현합니다. 생성·조회·수정·삭제 같은 동작은 URL이 아니라 HTTP Method로 표현합니다.

    - 좋은 예: `/posts`
    - 나쁜 예: `/create-post`, `/get-posts`

2. **목록을 나타내는 자원에는 복수형 명사를 사용합니다.**

    게시글 전체 목록은 `/posts`, 특정 게시글 하나는 `/posts/1`처럼 표현합니다.

3. **관련된 자원은 URL 계층으로 표현합니다.**

    특정 사용자가 작성한 게시글 목록은 `/users/1/posts`처럼 표현할 수 있습니다.

4. **HTTP Method는 동작을 나타냅니다.**

    같은 `/posts` 경로라도 `GET`은 조회, `POST`는 생성처럼 HTTP Method로 원하는 작업을 표현합니다.

5. **예외적으로 동작을 URL에 표현할 수 있습니다.**

    로그인이나 주문 취소처럼 생성·조회·수정·삭제만으로 자연스럽게 표현하기 어려운 기능도 있습니다. 이런 경우에는 `POST /auth/login`, `POST /orders/1/cancel`처럼 동작을 URL에 포함할 수 있습니다. 다만 동사를 URL에 넣는 방식은 필요한 경우에만 사용합니다.

## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. 웹 API는 클라이언트와 서버가 웹에서 데이터나 기능을 주고받기 위해 정해 둔 인터페이스다.
2. REST API에서는 URL에 `create-post`, `delete-post`처럼 수행할 동작을 반드시 포함해야 한다.
3. `GET /posts`와 `POST /posts`는 같은 경로를 사용하더라도 서로 다른 요청이다.

??? success "정답·해설"
    1. **O** — API는 한 프로그램이 다른 프로그램의 데이터나 기능을 사용할 수 있도록 정해 둔 인터페이스입니다.
    2. **X** — REST API에서는 보통 URL은 자원을 나타내고, 동작은 HTTP Method로 표현합니다.
    3. **O** — URL은 요청 대상, HTTP Method는 요청 동작을 나타내므로 같은 경로에서도 서로 다른 요청을 만들 수 있습니다.
