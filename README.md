# **코드스테이츠 AI/빅 데이터 부트캠프 5번째 프로젝트**

## 1. 코드스테이츠 AI/빅 데이터 부트캠프 섹션 6 프로젝트입니다.  
코드 스테이츠 AI/빅 데이터 부트캠프에서 약 2주간(22.02.15 ~ 22.02.25) 진행한 자유 주제 프로젝트입니다.

## 2. 이 프로젝트의 주제는 '어투별 문장 생성기'입니다.  
특징적인 어투를 가진 몇 그룹의 텍스트를 모아서 분석해, 어투에 맞는 문장을 생성하는 것이 목표입니다. 특징적인 어투는 인터넷에 작성되는 가벼운 내용의 twitter, 번역투와 독특한 어미를 사용하는 성경, 문장을 나열하고 축약어를 잘 사용하지 않는 판결문을 사례로 삼았으며, 이를 분석해보고 이 차이는 무엇때문인지 확인하는 것까지 포함됩니다.

## 3. 이 프로젝트의 목표는 '지금껏 배운 다양한 것들을 동시에 활용해보자'입니다.  
기존 프로젝트의 기한이 약 5일로, 각 프로젝트마다 활용할 것들이 어느 정도 정해져있었던 반면, 이번 프로젝트는 상대적으로 기한이 길어 배운 것들을 조합해 활용하고자 하는 목표를 가지고 시작하였습니다. 배웠던 방법과 사용하지 않았던 방법을 고루 하는 것을 기대하고 진행하였습니다.

## 4. 프로젝트의 진행 순서는 크게 '데이터 수집 - 데이터 분석 - 사전학습된 모델을 활용한 딥 러닝'입니다.  
각 과정에서 3)의 목표를 달성하기 위해 다양한 것을 활용하고자 하였습니다. 구체적인 내용은 각 문서를 참조해주시면 감사하겠습니다. 프로젝트는 파일의 순서대로 진행하였습니다.

## 5. 이 프로젝트를 진행하며 느낀 한계점은 다음과 같습니다.  
  1. 주제의 잦은 변경
    - 다양한 문제(충분한 양의 데이터를 확보하지 못함, 외부 패키지의 지원 종료, 흥미도 낮음 등)로 인해 프로젝트를 진행하지 못하고 바꾼 주제가 4개로, 시간과 에너지의 낭비가 과도함.  
  2. twitter의 대용량 데이터를 구하지 못함. 기존에 생각해둔 방법들이 모두 불가능해서 한정적인 시즌의 데이터만을 가져옴. twitter의 api를 통해 모으는 방법은 느리고 한계가 있었으나 다른 방법이 없었음.  
  3. DB 적재를 실행하지 않음
    - 초기 기획 중엔 DB를 활용해 데이터를 수집할 때 활용하려 했으나, 만약 이 것이 실제 업무라면 굳이 데이터를 적재하는 과정을 가지는 것이 너무 비효율적일 것이라 진행하지 않음. 그러나 경험 측면에선 그럼에도 불구하고 적재하는 것이 좋지 않았을까 하는 아쉬움이 있음.
  4. 토큰화 작업에서 Kkma를 쓰지 못함
    - Okt보다 더 복잡하고 세부적인 분류가 가능한 Kkma는 추정컨대 트윗 데이터의 이모지로 인해 인코딩이 불가능해서 사용하지 못함. 인코딩 자체에도 시간이 오래 걸리기도 해서 다른 방법을 시간 내에 찾는 것보단 단순한 Okt로 진행하기로 결정. 분석이 만족스럽지 못했음.
  5. 딥 러닝을 진행할 때 로컬 GPU를 활용하지 못함
    - tensorflow에서 GPU를 인식하게 하는 것을 실패함. 딥 러닝에 시간이 많이 소비될 것을 알기에 GPU를 인식시키고 싶었으나, 몇 번의 시도 후 로컬로 전부를 학습하는 것은 포기했음. 만약 빠르게 해결할 수 있었다면 더 빠르고 많은 학습이 가능해 프로젝트 과정에 큰 도움이 될 수 있을 것이지만, 그러지 못해 epoch를 각 5회 정도만 시도한 점이 아쉬움. 프로젝트가 끝난 후 전부 재설치 및 시작을 시도할 예정이었고, 현시점 설치가 완료되었음.
  6. 배포를 진행하지 못함
    - 모델을 저장하고 불러오는 과정에서 오류가 발생해, 최초 기대한 수준으로 프로젝트를 완성하지 못함.
