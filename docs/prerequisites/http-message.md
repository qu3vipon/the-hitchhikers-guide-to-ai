# HTTP 메시지

웹 브라우저와 curl를 통해 HTTP 요청을 보내는 방법을 알아봤습니다. 그런데 이때 클라이언트와 서버는 실제로 어떤 모양의 데이터를 주고받을까요? HTTP 통신에서는 **HTTP 메시지**라는 일정한 형식으로 요청과 응답을 주고받습니다. HTTP 요청은 클라이언트가 HTTP 요청 메시지를 서버로 보내는 것이고, HTTP 응답은 서버가 처리 결과를 HTTP 응답 메시지에 담아 클라이언트로 돌려보내는 것입니다.

## HTTP 메시지 이해하기 {#understanding-http-messages}

HTTP 메시지는 편지를 보내는 과정과 비슷합니다. 편지를 보낼 때는 봉투에 보내는 사람과 받는 사람의 주소, 우편번호를 적고, 봉투 안에는 전달할 편지를 넣습니다. 받는 사람은 봉투의 정보를 보고 어디서 온 편지인지 확인한 뒤, 편지의 내용을 읽습니다.

HTTP 메시지도 마찬가지입니다. 서버가 **어떤 동작을 해야 하는지 알려 주는 정보와 추가 정보, 실제로 전달할 데이터**를 정해진 순서로 담아 보냅니다.

## HTTP 메시지의 구성 {#http-message-structure}

요청 메시지와 응답 메시지는 모두 크게 **시작줄, 헤더, 본문**으로 구성됩니다.

1. 시작줄(Start Line)

    메시지의 첫 줄입니다. 요청 메시지에는 어떤 동작을 원하는지와 대상 경로가, 응답 메시지에는 처리 결과를 나타내는 상태 코드가 들어갑니다.

2. 헤더(Headers)

    시작줄 아래에 이어지는 추가 정보입니다. 요청에서는 어느 서버에 보내는지, 어떤 클라이언트가 보냈는지 등을 알리고, 응답에서는 데이터의 형식이나 크기 등을 알려 줍니다.

3. 본문(Body)

    실제로 전달할 데이터가 담기는 부분입니다. HTML, JSON, 이미지처럼 서버가 보내려는 내용이 들어갑니다. 본문이 없는 메시지도 있습니다.

## 요청 메시지 {#request-message}

클라이언트가 서버에 보내는 메시지를 **HTTP 요청 메시지**라고 합니다. 아래는 `example.com`의 첫 화면을 요청할 때의 모습을 간단히 표현한 예시입니다.

```http
GET / HTTP/1.1
Host: example.com
User-Agent: curl/8.7.1
```

1. **시작줄**

    - `GET / HTTP/1.1`: 서버에게 `/` 경로의 내용을 달라고 요청하는 부분입니다.

2. **헤더**

    - `Host: example.com`: 요청을 받을 서버의 주소입니다.
    - `User-Agent: curl/8.0`: 요청을 보낸 클라이언트 프로그램의 정보입니다.

3. **본문**

    - 이 요청은 서버에서 데이터를 받기만 하므로 본문이 없습니다.

!!! info "`/` 경로 요청"
    웹 서버에서 `/`는 보통 웹 사이트의 가장 처음 화면을 뜻합니다. 대부분의 웹 사이트는 이 경로로 요청을 받으면 일반적으로 `index.html`을 반환하며, 이 화면을 보통 홈 화면이라고 부릅니다.

## 응답 메시지 {#response-message}

서버가 요청을 처리한 뒤 클라이언트에 돌려보내는 메시지를 **HTTP 응답 메시지**라고 합니다. 위 요청에 대한 응답은 아래처럼 표현할 수 있습니다.

```http
HTTP/1.1 200 OK         
Content-Type: text/html 
Content-Length: 1256    

<!doctype html>         
<html>
  <body>
    <h1>Example Domain</h1>
  </body>
</html>
```

1. **시작줄**

    - `HTTP/1.1 200 OK`는 HTTP 버전과 요청 처리 결과를 나타냅니다. `200 OK`는 요청이 정상적으로 처리되었다는 뜻입니다.

2. **헤더**

    - `Content-Type: text/html`: 본문이 HTML 형식이라는 정보입니다.
    - `Content-Length: 1256`: 본문의 데이터 크기입니다.

3. **본문**

    - `<!doctype html>...</html>`: 서버에서 응답하는 HTML입니다.

## HTTP 메시지 확인하기 {#inspect-http-messages}

HTTP 메시지를 `curl`로 직접 확인해 보겠습니다.

이전에 사용한 `curl example.com` 명령어는 서버가 보낸 응답 본문만 화면에 출력합니다. 그래서 HTML 코드는 볼 수 있었지만, 시작줄과 헤더는 확인할 수 없었습니다.

### 1. curl 요청 메시지 {#curl-request-message}

`-v` 옵션을 사용하면 `curl`이 요청과 응답에 관한 자세한 정보를 함께 출력합니다. 요청을 보낼 때는 아래 명령어를 실행하세요.

=== "macOS"

    ```shell
    curl -v example.com
    ```

=== "Windows PowerShell"

    ```powershell
    curl.exe -v example.com
    ```

출력 중 `>`로 시작하는 줄이 `curl`이 서버에 보낸 요청 메시지입니다.

```http
> GET / HTTP/1.1
> Host: example.com
> User-Agent: curl/8.7.1
```

앞의 `>` 표시는 `curl`이 출력에 덧붙인 구분 표시이며, 실제 HTTP 요청 메시지에는 포함되지 않습니다.

### 2. curl 응답 메시지 {#curl-response-message}

`-i` 옵션을 사용하면 응답 본문 앞에 서버가 보낸 시작줄과 헤더를 함께 출력합니다.

=== "macOS"

    ```shell
    curl -i example.com
    ```

=== "Windows PowerShell"

    ```powershell
    curl.exe -i example.com
    ```

출력의 앞부분에는 아래와 같은 응답 시작줄과 헤더가, 빈 줄 아래에는 HTML 본문이 표시됩니다.

```http
HTTP/1.1 200 OK
Content-Type: text/html

<!doctype html>
<html>
  ...
</html>
```

### 3. 웹 브라우저 요청·응답 메시지 {#browser-http-messages}

이번에는 웹 브라우저가 실제로 주고받는 HTTP 메시지를 확인해 보겠습니다. Chrome을 기준으로 설명합니다.

1. 웹 브라우저에서 `https://example.com`에 접속합니다.
2. 페이지에서 마우스 오른쪽 버튼을 클릭한 뒤 **검사**를 선택해 개발자 도구를 엽니다.

    - Windows·Linux에서는 `F12` 또는 `Ctrl` + `Shift` + `I`로 열 수 있습니다.
    - macOS에서는 `Command` + `Option` + `I`를 사용합니다.

3. 개발자 도구 상단에서 **Network** 탭을 선택한 다음, 페이지를 새로고침합니다.
4. Network 요청 목록에서 `example.com` 항목을 선택합니다. 창 크기에 따라 화면 아래 또는 오른쪽에 요청의 상세 정보가 표시됩니다.
5. **Headers** 탭에서 다음 항목을 확인합니다.

    - General: 요청 URL, 요청 방식, 응답 상태 코드를 확인할 수 있습니다.
    - Request Headers: 브라우저가 서버에 보낸 요청 헤더입니다.
    - Response Headers: 서버가 브라우저에 보낸 응답 헤더입니다.

응답 본문도 확인하고 싶다면 **Response** 탭을 선택하세요. 앞에서 `curl`로 보았던 HTML 원본이 표시됩니다.

<img src="../../assets/images/developertool.png" alt="Chrome 개발자 도구의 Network 탭에서 HTTP 요청 정보를 확인하는 화면" class="example-domain-image">

!!! info "HTML 원본 바로 보기"
    Chrome에서 페이지를 마우스 오른쪽 버튼으로 클릭한 뒤 **페이지 소스 보기**를 선택하면, 브라우저가 서버에서 받은 HTML 원본을 바로 확인할 수 있습니다.

## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. HTTP 요청과 응답은 HTTP 메시지라는 일정한 형식으로 데이터를 주고받는다.
2. HTTP 메시지의 헤더에는 실제로 전달할 데이터만 담긴다.
3. 모든 HTTP 요청 메시지에는 반드시 본문이 있어야 한다.

??? success "정답·해설"
    1. **O** — 클라이언트와 서버는 HTTP 메시지 형식에 맞춰 요청과 응답을 주고받습니다.
    2. **X** — 헤더에는 데이터의 형식, 크기, 보내는 대상처럼 메시지를 이해하는 데 필요한 추가 정보가 담깁니다. 실제 데이터는 본문에 담깁니다.
    3. **X** — 본문 없이 정보를 요청하는 HTTP 메시지도 있습니다.
