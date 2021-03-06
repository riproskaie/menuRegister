# kiosk_clone
 Cloning a kiosk system for a fast-food shop.

###웹페이지 설명
- menuRegister: 메인페이지(메뉴관리)에 해당합니다.
- 구현방식: jQuery, Ajax를 Node.js와 연동시킬 예정. html을 pug로, css를 scss로 변환할 예정.

###div 설명
- premium, whoppers, chickenBurgers, drinks, sides, desserts: 생성한 메뉴의 카드들이 각 페이지에 저장됩니다.
- inputFormCombo, inputFormSingle: 카드 생성을 위한 입력 폼입니다. 탭을 이용해 두 가지 데이터를 한꺼번에 서버로 보내게 하려 합니다. html에서 미리 정의된 submit 타입 버튼을 사용하기보다는, 딕셔너리를 자바스크립트 함수로 서버에 보내게 하려고 합니다.

###진행중인 작업
####11월 17일
- [x] 검은고딕 폰트를 전체 적용이 아닌 요소별 세부적용으로 바꾸기
- [x] menuRegister.html 페이지와 css 틀 만들기 (구글 검색하며 작업하기 쉽도록 우선 html로 제작)
- [x] 라우트에 각 페이지 등록하기 (그동안 페이지 구성이 바뀌었으므로 수정 필요함)
- [x] 스크롤바 css 디자인 적용 (선행작업자 코드 그대로 사용)

####11월 19일
- [x] inputFormCombo.html, inputFormSingle.html 페이지와 css 틀 만들기 
- [x] 카드 생성을 위한 클릭버튼을 a 태그와 css로 구현하기
- [x] inputFormSingle에 양식 제출을 위한 javascript(jQuery) 적용하기
- [x] 더미 데이터 db에 입력하기 (flask 이용함)

####11월 20일
- [x] 샘플로 사용할 메뉴 이미지들 캡처 후 일정한 크기로 자르기

####11월 21일~11월 23일
- [x] css를 통해, label 요소 이용해서 디자인된 팝업창 구현하기 + 일정 영역에만 스크롤 적용시키기
- [x] 현재 a태그로 구현한 카테고리 버튼을 radio input을 이용한 tab으로 바꾸기

#### 11월 24일
- [x] premium, whoppers, chickenBurgers, drinks, sides, desserts 페이지를 div로 바꾸어 menuRegister 내로 통합하기

#### 11월 25일~11월 29일 (여기서 어려움을 겪음)
- [x] menuRegister 페이지 내에 inputForm 팝업창을 hidden div 형태로 포함시키기  
- [x] inputForm이 팝업창 내에 표시되게 하기

####11월 30일~12월 1일
- [x] 팝업창 테두리 색(베이지) 입히기 (가능하나 예쁘지 않음. 흰색으로 할지 검토)
- [x] inputFormCombo에서 default 사이드/음료수 선택 라디오버튼을 제품사진으로 디자인 (힘들면 그냥 체크박스로) -> 기각(12월 1일)
- [x] inputFormSingle(default로 노출)과 inputFormCombo를 하나로 합치기 
- [x] menuRegister 내의 메뉴표시 영역만 scroll되게 하기
- [x] 팝업창과 메인페이지 합침 확인
- [x] radio button을 이용한 inputFormSingle/inputFormCombo tab버튼 적용

####12월 2일
- [x] db로부터 메뉴 데이터 읽어오기 (Flask 상으로는 가능함 확인. ajax 정상작동 확인)
- [x] 팝업창에 inputForm 들어가게 하기. tab버튼은 팝업창 상단 고정 (디자인 깨짐으로 어려움 겪는 중)
- [x] 팝업창을 취소하면 폼이 비워지도록 처리
- [x] 메뉴등록 (+)버튼을 여러 카테고리에서 재활용할 수 있도록 처리
- [x] 메뉴카드가 (+) 버튼의 앞으로 왼쪽 위에서부터 누적되게 하기 (.before() 메소드 활용)
- [x] 메뉴카드와 (+)버튼을 grid로 표시되게 하기
- [x] 메뉴카드와 (+)버튼을 메인 페이지에 합치기
- [x] 메뉴등록/메뉴수정 함수 작동 여부에 따라 팝업창의 타이틀을 '메뉴등록'/'메뉴수정'으로 변경

###12월 3일
- [x] javascript를 통해, (menuType === '프리미엄' or '와퍼' or '치킨버거')에 대해서 세트메뉴 미입력시 경고창 뜨도록 
- [x] 삭제버튼을 누를 경우 제출 과정이 복잡해질 것을 고려, '단종' 라디오 버튼으로 구현함 
- [x] 메뉴 단종 라디오버튼을 '예'로 클릭할 경우, '정말로 삭제할지' 모달창 띄워 확인. 취소시 자동으로 '아니오'.
- [x] 필수입력항목에는 p.lab에 :after를 적용해서 빨간 글씨로 필수입력란임을 표시해주기

### 12월 4일
- [x] url 뒤에 #a 등의 찌꺼기가 붙는 문제 해결
- [x] 팝업창 종료 시 .dim이 활성화되어 남아있는 문제 해결
- [x] 가로폭이 750px을 넘어가면 서식 깨지지 않고 scroll되도록 함
- [x] 버거류일 경우에는 inputFormCombo와 inputFormSingle이 (2초 정도의 time interval을 두고) 모두 submit, 그 외에는 inputFormSingle만 submit
- [x] 할인가 표시 이펙트를 css상으로 구현하기 

### 12월 5일 
- [x] css 서식 통일 (소문자에 하이픈)
- [x] submit() 함수로 db에 데이터 전달 (array, boolean을 db로 전달 시 문제 해결)
- [x] ObjectId 내부값 추출 (인코더를 시도해보다가 str 형변환으로 해결함. Node.js에서는 달라질 수도 있음)
- [x] showMenu() 함수 구현하기 (db로부터 읽어온 메뉴 데이터를 바탕으로, menuType별로 각 카테고리에 메뉴 카드를 .append())

### 12월 6일
- [x] 메뉴 카드를 클릭하면 _id 값을 매개로 inputForm 팝업창에 해당 메뉴 데이터가 뜨게 해서, 수정창으로 활용하기
- [x] 메뉴수정창에 단품과 세트의 경우가 제대로 올라오는지 확인하기
- [x] showMenu()에서 가격란(붉은글씨)에 천의 자리마다 점 찍기 (Stack Overflow에 소개된 외부함수 이용). 할인가에도 적용함
- [x] isDiscontinued인 아이템은 서버상으로는 남아있되 jQuery상으로 .remove() 하기
- [x] POST를 응용해 수정 반영하기 (Node.js 상으로는 따로 구현이 필요함)
- [x] 상품 이미지 하단 일부(음료 등) 잘림 -> .menu-name 옆에 <br> 추가해서 해결

###남은 작업
##### showMenu() 
- [x] 자바스크립트 - (백엔드상으로) 코카콜라(R)와 프렌치프라이(R)를 찾아 objectId값을 side와 drink에 저장한다 (조회가 안되면 ""를 할당한다) - 12.07
- [x] 자바스크립트 - isSoldOut인 카드는 자동으로 흑백 + sold표시 (javascript + css 이용) -> toggleClass로 해결함 - 12.07
- [x] 자바스크립트 - isDiscounted인 경우에는 SALE 표시 -> toggleClass로 해결함 - 12.07
- [x] 자바스크립트 - 메뉴 수정 시 입력당시의 체크박스 일부가 지워지는 문제 -> nonAllergen과 allergen이 모두 ingredients에 체크 반영되어야하는데 nonAllergen만 js상으로 체크해주고 있는 것을 발견. 해결함 - 12.07
- [x] 자바스크립트 - 브라우저 js에서 '수정'요청 시, 알레르기비유발 물질을 2번 누적시켜 전달하는 경우가 있음 (jQuery 인풋체크박스 each.()가 두 번 돈다) -> each 문 안에 반복감지시 return false하여 해결 - 12.07

#### 로직 효율성/기타 편의사항 관련
- [x] 자바스크립트 - 입력/수정 폼에서 탭이 단품으로 default로 클릭되게 하기 - 12.07
- [x] 자바스크립트 - default 값이 0일 경우, 이를 지운 채로 submit을 누르면 경고창이 뜨지 않고 submit된다. 
-> 이런 경우에도 자동으로 0이 서버에 입력되게는 해 놓았으나, 경고창 문제는 해결되지 않았다. 
- [x] 자바스크립트, 백엔드 - 사이드와 음료를 ObjectId 자료형인 상태로 get할 경우 나머지 메뉴들도 화면에 표시되지 않음 -> 문자열화하여 해결함. Node.js에서는 어떨지? - 12.07

- [ ] 숫자가 아닌 값을 입력할 경우, 해당 값은 형변환이 일어나 NaN이 된다. (수정이 가능하긴 하나, 인풋 차원에서 이런 잘못된 입력을 막아둔다면?) 
- [ ] 클릭된 카테고리 탭에 따라 메뉴등록 폼의 메뉴유형에도 자동으로 체크가 되게 할지? (구현시간 여유가 있다면 하는 게 좋긴 하나, 번잡하며 오류 위험이 있다)
- [ ] 도메인 url 서식 검증할지? (외부 함수 사용하면 쉬울 듯하나, 어차피 사용자가 찾아들어가 수정이 가능하므로 애매... 시간여유가 있다면 하자.)
- [ ] 반복되는 ajax get success를 없애고 한번만 되게 하기 (어려움. 내 수준에서 아예 ajax 없이 하기는 역량밖)
- [ ] 할인가는 원가보다 싸서는 안 될텐데 별도의 alert를 띄워야 하나? (현재는 이럴 경우 최종 할인가가 마이너스로 뜨지만 글자가 깨지거나 하지는 않는다. 수정은 가능하므로 치명적인 glitch는 아니다)
 
####제출서식 관련
- [x] html을 pug로 바꾸기 - 12.07
- [x] css를 scss로 바꾸기 - 12.07
- [x] 라우트 설정하기 - 12.07
- [ ] 그리드 확인용 불필요한 css 지우기
- [ ] flask에서 Node.js로 db와의 연결방식 바꾸기
- [ ] 변수명 양식 최종 점검(camel case, under bar 등등)
