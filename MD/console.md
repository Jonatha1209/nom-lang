먼저 console에서 사용하실거면, src\console에 있는 console.py를 실행시키면 됩니다. </br>
nom_config는 절대 건드리지 말아주세요!!!! </br>
먼저 .nomrc 파일에서 설정을 다뤄봅시다. </br>

# nomrc config 

일단 먼저 [DEFAULT] 설정을 건드려주셔야 합니다</br>
```
[DEFAULT]
default_file = "test.nom"
prompt_color = "cyan"
auto_save = true
default_table = "users"
```

먼저 default_table 변수는 to-sql 커맨드를 쓸때 기본으로 나오는 sql database라고 보시면 됩니다. </br>
다음, prompt_color는 터미널 색상입니다. 대충 cyan, green 같은 영어 색상을 쓰셔야합니다. </br>
일단 기본으론 cyan (하늘색)으로 진행됩니다. </br>

다음은 auto_save 입니다.</br>
nom 언어는 자동 세이브가 꺼져있기에 update 또는  write를 한 후엔 save를 해줘야합니다. </br>
하지만 save를 하지않고 그대로 한 사람들이 있을 수도 있기에, DEFAULT 설정을 auto_save = true로 해놨습니다. </br>

console.py를 실행 시키고 help 커맨드를 누른 후,  명령어들을 써보세요!
