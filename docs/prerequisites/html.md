# HTML

앞에서 `curl`로 `example.com`에 요청을 보냈을 때, 터미널에 긴 텍스트가 출력되었습니다. 이 텍스트를 보기 좋게 다시 정리하면 아래와 같습니다.

```html hl_lines="31-33"
<!doctype html>
<html lang="en">
<head>
  <title>Example Domain</title>
  <link rel="icon" href="data:,">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      background: #eee;
      width: 60vw;
      margin: 15vh auto;
      font-family: system-ui, sans-serif;
    }

    h1 {
      font-size: 1.5em;
    }

    div {
      opacity: 0.8;
    }

    a:link,
    a:visited {
      color: #348;
    }
  </style>
</head>
<body>
  <div>
    <h1>Example Domain</h1>
    <p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p>
    <p><a href="https://iana.org/domains/example">Learn more</a></p>
  </div>
</body>
</html>
```

## HTML이란? {#what-is-html}


이런 문서 형식을 HTML(HyperText Markup Language)이라고 부릅니다. HTML은 미리 정해진 규칙에 따라 **웹 페이지의 구조와 내용**을 표현하는 마크업 언어입니다. 여기서 `<h1>`은 제목, `<p>`는 문단, `<a>`는 링크를 나타내며, 각각 화면에 보이는 제목, 설명 문장, Learn more 링크에 대응합니다.

<img src="../../assets/images/exampledotcom_highlight.png" alt="HTML을 렌더링한 Example Domain 화면" class="example-domain-image">

!!! info "HTML 문법 더 알아보기"
    이 과정에서는 HTML 문법을 하나씩 자세히 다루지 않습니다. HTML 문법이 궁금하다면 [MDN의 HTML 시작하기](https://developer.mozilla.org/ko/docs/Learn_web_development/Core/Structuring_content/Basic_HTML_syntax)를 참고해 보세요.

## HTML 렌더링 {#html-rendering}

그런데 웹 브라우저에는 왜 HTML 코드 대신 우리가 익숙한 웹 페이지 화면이 보일까요? 그건 브라우저가 HTML을 읽고 사용자가 보기 편한 화면으로 렌더링(rendering)하기 때문입니다. 이 방식의 장점은 HTML이 사용자의 화면 크기와 기기 환경에 맞게 웹 페이지를 그리기 때문에, 같은 문서를 어디서나 읽기 편한 화면으로 볼 수 있다는 점입니다.

우리가 naver.com에 접속해 네이버 홈 화면을 보는 것도 같은 방식입니다. 웹 브라우저가 네이버 서버에 HTTP 요청을 보내면, 홈 화면 이미지를 통째로 받아오는 것이 아니라 홈 화면을 그릴 수 있는 HTML을 받아옵니다. 브라우저는 이를 해석하고, 사람이 읽기 쉬운 화면으로 렌더링해 보여 줍니다.

## Content-Type {#content-type}

그런데 HTTP 통신에 반드시 HTML만 사용하는 것은 아닙니다. 클라이언트와 서버는 이미지, JSON, 동영상처럼 여러 형식의 데이터를 주고받을 수 있습니다. HTTP에서는 `Content-Type`이라는 값을 통해 서버가 응답 데이터의 형식을 클라이언트에게 알려 줍니다.

예를 들어 HTML 문서는 `text/html`, JSON 데이터는 `application/json`처럼 표현합니다. 웹 페이지에 표시할 사진이나 동영상도 HTTP를 통해 전달되며, 각각의 데이터 형식에 맞는 `Content-Type` 값이 함께 전달됩니다.


!!! info "JSON"
    JSON(JavaScript Object Notation)은 데이터를 `키: 값` 형태로 정리해 표현하는 형식입니다. 예를 들어 alex라는 사람의 데이터를 아래와 같이 표현할 수 있습니다.

    ```json
    {
      "name": "alex",
      "age": 30,
      "email": "alex@example.com"
    }
    ```

    대부분의 프로그래밍 언어와 시스템은 JSON을 지원합니다. 그래서 서로 다른 프로그램끼리 데이터를 주고받을 때 널리 사용하는 표준 데이터 형식입니다.


## :material-pencil: 실습 과제 {#exercises}

다음 문장이 맞으면 O, 틀리면 X를 선택하세요.

1. 웹 브라우저는 서버에서 받은 HTML을 해석하고 렌더링해 웹 페이지 화면으로 보여 준다.
2. HTTP 통신에서는 HTML 데이터만 주고받을 수 있다.
3. `Content-Type`은 서버가 응답 데이터의 형식을 클라이언트에게 알려 주는 값이다.

??? success "정답·해설"
    1. **O** — 브라우저는 HTML을 해석해 사람이 읽기 쉬운 화면으로 렌더링합니다.
    2. **X** — HTTP로는 HTML뿐 아니라 JSON, 이미지, 동영상 등 다양한 형식의 데이터를 주고받을 수 있습니다.
    3. **O** — 서버는 `Content-Type`을 통해 HTML, JSON 등 응답 데이터의 형식을 알려 줍니다.
