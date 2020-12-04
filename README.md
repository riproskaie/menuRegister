# kiosk_clone
 Cloning a kiosk system for a fast-food shop.

###웹페이지 설명
- menuRegister: 메인페이지(메뉴관리)에 해당합니다.

###div 설명
- premium, whoppers, chickenBurgers, drinks, sides, desserts: 생성한 메뉴의 카드들이 각 페이지에 저장됩니다.
- inputFormCombo, inputFormSingle: 카드 생성을 위한 입력 폼입니다. 탭을 이용해 두 가지 데이터를 한꺼번에 서버로 보내게 하려 합니다. html에서 미리 정의된 submit 타입 버튼을 사용하기보다는, 딕셔너리를 자바스크립트 함수로 서버에 보내게 하려고 합니다.

###진행중인 작업
- [x] 검은고딕 폰트를 전체 적용이 아닌 요소별 세부적용으로 바꾸기
- [x] menuRegister.html 페이지와 css 틀 만들기 (구글 검색하며 작업하기 쉽도록 우선 html로 제작)
- [x] 라우트에 각 페이지 등록하기
- [x] inputFormCombo.html, inputFormSingle.html 페이지와 css 틀 만들기 
- [x] 카드 생성을 위한 클릭버튼을 a 태그와 css로 구현하기
- [x] inputFormSingle에 양식 제출을 위한 javascript(jQuery) 적용하기
- [x] 더미 데이터 db에 입력하기
- [x] 샘플로 사용할 메뉴 이미지들 캡처 후 일정한 크기로 자르기
- [x] css를 통해, label 요소 이용해서 디자인된 팝업창 구현하기 + 일정 영역에만 스크롤 적용시키기
- [x] 현재 a태그로 구현한 카테고리 버튼을 radio input을 이용한 tab으로 바꾸기
- [x] premium, whoppers, chickenBurgers, drinks, sides, desserts 페이지를 div로 바꾸어 menuRegister 내로 통합하기
- [x] menuRegister 페이지 내에 inputForm 팝업창을 hidden div 형태로 포함시키기 
- [x] inputForm이 팝업창 내에 표시되게 하기
- [x] 스크롤바 css 디자인 적용 (선행작업자 코드 그대로 사용)
- [x] 팝업창 테두리 색(베이지) 입히기 (가능하나 예쁘지 않음. 흰색으로 할지 검토)
- [x] inputFormCombo에서 default 사이드/음료수 선택 라디오버튼을 제품사진으로 디자인 (힘들면 그냥 체크박스로) 
- [x] inputFormSingle(default로 노출)과 inputFormCombo를 하나로 합치기 
- [x] menuRegister 내의 메뉴표시 영역만 scroll되게 하기
- [x] 팝업창과 메인페이지 합침 확인
- [x] radio button을 이용한 inputFormSingle/inputFormCombo tab버튼 적용
- [x] db로부터 메뉴 데이터 읽어오기 (Flask 상으로는 가능함 확인. ajax 정상작동 확인)
- [x] 팝업창에 inputForm 들어가게 하기. tab버튼은 팝업창 상단 고정 (디자인 깨짐으로 어려움 겪는 중)
- [x] 팝업창을 취소하면 폼이 비워지도록 처리
- [x] 메뉴등록 (+)버튼을 여러 카테고리에서 재활용할 수 있도록 처리
- [x] 메뉴카드가 (+) 버튼의 앞으로 왼쪽 위에서부터 누적되게 하기 (.before() 메소드 활용)
- [x] 메뉴카드와 (+)버튼을 grid로 표시되게 하기
- [x] 메뉴카드와 (+)버튼을 메인 페이지에 합치기
- [x] 메뉴등록/메뉴수정 함수 작동 여부에 따라 팝업창의 타이틀을 '메뉴등록'/'메뉴수정'으로 변경
- [x] 삭제버튼을 누를 경우 제출 과정이 복잡해질 것을 고려, '단종' 라디오 버튼으로 구현함 
- [x] 메뉴 단종 라디오버튼을 '예'로 클릭할 경우, '정말로 삭제할지' 모달창 띄워 확인. 취소시 자동으로 '아니오'.
- [x] 필수입력항목에는 p.lab에 :after를 적용해서 빨간 글씨로 필수입력란임을 표시해주기
- [x] javascript를 통해, (menuType === '프리미엄' or '와퍼' or '치킨버거')에 대해서 세트메뉴 미입력시 경고창 뜨도록 
- [x] url 뒤에 #a 등의 찌꺼기가 붙는 문제 해결
- [x] 팝업창 종료 시 .dim이 활성화되어 남아있는 문제 해결
- [x] css 서식 통일
- [x] 가로폭이 750px을 넘어가면 서식 깨지지 않고 scroll되도록 함
- [x] 버겨류일 경우에는 inputFormCombo와 inputFormSingle이 (2초 정도의 time interval을 두고) 모두 submit, 그 외에는 inputFormSingle만 submit
- [x] submit() 함수로 db에 데이터 전달

###남은 작업
####웹페이지 동작 관련
- [ ] showMenu() 함수 구현하기(db로부터 읽어온 메뉴 데이터를 바탕으로, menuType별로 각 카테고리에 메뉴 카드를 .append())
- [ ] isDiscontinued인 아이템은 서버상으로는 남아있되 jQuery상으로 .remove() 하기 
- [ ] isSoldOut인 카드는 자동으로 흑백 + sold표시 (javascript + css 이용) - 서식은 구현해둠
- [ ] isDiscounted인 경우에는 SALE 표시 - 서식은 구현해둠
- [ ] 메뉴 카드를 클릭하면 inputForm 팝업창에 해당 메뉴 데이터가 뜨게 해서 수정창으로 활용하기

- [ ] 사이드/음료는 라디오버튼을 통해 선택하되, ObjectId 값을 서버로 보내게 하기 
- [ ] 클라이언트(javascript) 및 백엔드 상에서, ObjectId를 이용해 수정 반영하기 (?)
- [ ] 가능하면 x축 방향으로도 스크롤이 되게 할 것 (창을 줄이니까 사이트가 깨짐)

####제출서식 관련
- [ ] html을 pug로 바꾸고 세부모듈로 분할하기
- [ ] css를 scss로 바꾸고 세부모듈로 분할하기
- [ ] 라우트를 Node.js로 바꾸기
- [ ] flask에서 Node.js로 db와의 연결방식 바꾸기
- [ ] 변수명 양식 최종 점검(camel case, under bar 등등)
