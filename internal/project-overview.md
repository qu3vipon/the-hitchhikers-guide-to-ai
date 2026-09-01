# FastAPI 전자책 프로젝트 개요

## 프로젝트 목표

이 전자책의 최종 목표는 **FastAPI를 활용한 AI Agent 개발**이다.

학습자는 FastAPI의 기초를 익힌 뒤 비동기 처리, AI 모델 서빙, LangChain과 LangGraph를 차례로 학습한다. 마지막에는 학습한 내용을 바탕으로 AI Agent를 개발하고 운영하는 단계까지 나아간다.

## 주요 독자

Python 기초 문법을 학습했고, FastAPI를 배워 앞으로 AI Agent를 만들고 싶은 사람을 대상으로 한다.

## 콘텐츠 학습 방식

각 절은 설명과 따라 하기로 끝나지 않는다. 절을 마칠 때마다 학습 내용을 확인할 수 있는 간단한 실습 과제를 제공하고, 과제를 해결한 뒤 확인할 수 있도록 정답과 해설도 함께 제공한다.

## 전체 학습 구성

1. **FastAPI 기초**
   - 블로그 백엔드 API를 만들며 FastAPI의 핵심 기능을 학습한다.
2. **비동기 처리**
   - FastAPI에서 비동기 프로그래밍을 활용하는 방법을 학습한다.
3. **AI 모델 서빙**
   - AI 모델을 FastAPI API로 제공하는 방법을 학습한다.
4. **LangChain & LangGraph**
   - AI 애플리케이션과 상태 기반 워크플로를 구성하는 방법을 학습한다.
5. **AI Agent 개발 및 운영**
   - 앞선 내용을 바탕으로 AI Agent를 개발하고 운영한다.

## 1부: FastAPI 기초

1부의 목표는 데이터베이스, 회원가입, JWT 인증을 갖춘 블로그 백엔드 API를 구현하는 것이다.

### 목차

1. **강의 소개**
   1. 이 강의를 통해 얻게 되는 것
   2. 간단한 블로그 소개
   3. 전체 학습 흐름
2. **사전 학습 내용**
   1. 웹 개발 기초
   2. 가상환경
   3. 프로젝트 준비
3. **FastAPI 소개**
   1. FastAPI란 무엇인가
   2. FastAPI의 장점과 특징
   3. 자동 API 문서 확인하기
4. **FastAPI 기초**
   1. Path와 Query로 요청 받기
   2. Type Hints 적용하기
   3. Pydantic 기초
   4. Request Body 받기
   5. Header 받기
   6. 응답 만들기
   7. 예외 처리하기
5. **기본 CRUD 구현: 블로그**
   1. 블로그 데이터와 API 설계
   2. 게시글 생성하기
   3. 게시글 목록과 상세 조회하기
   4. 게시글 수정하기
   5. 게시글 삭제하기
6. **데이터베이스 활용: SQLite**
   1. 데이터베이스와 SQLite 소개
   2. SQLite 데이터베이스 준비하기
   3. FastAPI와 SQLite 연결하기
7. **SQLAlchemy ORM 활용**
   1. ORM과 SQLAlchemy 소개
   2. 모델 정의하기
   3. 세션으로 데이터 처리하기
   4. 블로그 CRUD에 ORM 적용하기
8. **회원가입 기능 구현**
   1. 사용자 데이터 설계
   2. 비밀번호 해싱
   3. 회원가입 API 구현
9. **로그인과 인증 구현: JWT**
   1. 인증과 JWT 이해하기
   2. 로그인 API 구현
   3. JWT로 보호된 API 만들기
10. **추가 학습: 화면 구성**
    1. Frontend의 역할
    2. HTML로 화면 구성하기
    3. 블로그 API와 화면 연결하기
11. **추가 학습: MySQL & PostgreSQL 설정**
    1. SQLite, MySQL, PostgreSQL 비교
    2. MySQL 설정하기
    3. PostgreSQL 설정하기
    4. 데이터베이스 연결 설정 바꾸기
12. **추가 학습: Pydantic 심화**
    1. `field_validator`로 입력값 검증하기
    2. `computed_field`로 계산된 필드 만들기
