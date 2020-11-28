# kiosk_clone
 Cloning a kiosk system for a fast-food shop.

###웹페이지 파일 설명
- menuRegister: 메인페이지(메뉴관리)에 해당합니다.
- premium, whoppers, chickenBurgers, drinks, sides, desserts: 메뉴 카테고리에 해당합니다. 생성한 메뉴의 카드들이 각 페이지에 저장됩니다.
- inputFormCombo, inputFormSingle: 카드 생성을 위한 입력 폼입니다. 탭을 이용해 두 가지 데이터를 한꺼번에 서버로 보내게 하려 합니다. submit 타입 버튼을 사용하기보다는 딕셔너리를 자바스크립트 함수로 서버에 보내게 하려고 합니다.

###진행중인 작업
- [x] menuRegister.html 페이지와 css 틀 만들기 (구글 검색하며 작업하기 쉽도록 우선 html로 제작)
- [x] 라우트에 각 페이지 등록하기
- [x] inputFormCombo.html, inputFormSingle.html 페이지와 css 틀 만들기 
- [x] 카드 생성을 위한 클릭버튼을 a 태그와 css로 구현하기
- [x] inputFormSingle에 양식 제출을 위한 javascript(jQuery) 적용하기
- [x] 더미 데이터 db에 입력하기
- [x] 샘플로 사용할 메뉴 이미지들 캡처 후 일정한 크기로 자르기
- [x] css를 통해, label 요소 이용해서 디자인된 팝업창 구현하기 + 일정 영역에만 스크롤 적용시키기

###남은 작업
####웹페이지 동작 관련
- [ ] 현재 a태그로 구현한 카테고리 버튼을 radio input을 이용한 tab으로 바꾸기
- [ ] premium, whoppers, chickenBurgers, drinks, sides, desserts 페이지를 div로 바꾸어 menuRegister 내로 통합하기
- [ ] inputFormSingle(default로 노출)과 inputFormCombo를 하나로 합치고 radio button을 이용한 tab 적용
- [ ] menuRegister, inputForm
- [ ] inputForm이 팝업창 내에 표시되게 하기
- [ ] inputForm 내에서 inputFormCombo와 inputFormSingle의 내용이 탭 형태로 함께 들어가게 하기
- [ ] javascript를 통해, (menuType === '프리미엄' or '와퍼' or '치킨버거')에 대해서 isCombo = true 적용 
- [ ] javascript를 통해, isCombo일 경우에는 inputFormCombo와 inputFormSingle이 모두 submit, !isCombo이면 inputFormSingle만 submit
- [ ] db로부터 메뉴 데이터 읽어오기 
- [ ] 읽어온 메뉴 데이터를 바탕으로, menuType별로 각 카테고리에 메뉴 저장
- [ ] 메뉴 카드를 클릭하면 inputForm 팝업창에 해당 메뉴 데이터가 뜨게 하기
- [ ] inputForm 상에서 수정하기
- [ ] 클라이언트(javascript) 및 백엔드 상에서, ObjectId를 이용해 수정 반영하기 (?)

####제출서식 관련
- [ ] html을 pug로 바꾸고 세부모듈로 분할하기
- [ ] css를 scss로 바꾸고 세부모듈로 분할하기
- [ ] 라우트를 Node.js로 바꾸기
- [ ] flask에서 Node.js로 db와의 연결방식 바꾸기
- [ ] 변수명 양식 최종 점검(camel case, under bar 등등)
