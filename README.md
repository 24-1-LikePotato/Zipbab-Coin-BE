# Zipbab-Coin-BE

1. 브랜치 운영 방식
  - `main` : 최종본
  - `develop` : 개발하면서 코드 모으는 곳, 여기로 PR 날리기
  - `feat` : 기능을 개발하면서 각자가 사용할 브랜치 
      ex) feat/#이슈번호-구현하려는 기능, feat/#1 - 로그인 
      git checkout -b ‘feat/#{이슈번호}-{기능단위(스네이크 케이스 사용)}’ 
 
2. 커밋 컨벤션
  - `feat` : 새로운 기능 구현
  - `fix` : 버그, 오류 해결
  - `chore` : 동작에 영향 없는 코드 or 변경 없는 변경사항(주석 추가 등) or 파일명, 폴더명 수정 or 파일, 폴더 삭제 or 디렉토리 구조 변경
  - `refactor` : 전면 수정, 코드 리팩토링
  - `docs` : README나 WIKI 등의 문서 수정
  - `merge`: 다른 브랜치와 병합 
      ex) git commit -m "feat: #1 로그인 구현" 
  
