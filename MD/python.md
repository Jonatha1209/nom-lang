# 실행

먼저 test.py를 만들어 줍니다. </br>
그리고 다음과 같이 작성합니다. </br>

```python
import main as nom
manage = nom.NomFileManager("test.nom")
print(manage.read())
manage.write("nickname", "Ali", "string")
manage.save()
```

매우 간단합니다. </br>
먼저 manage는 Nomfile manager입니다. </br>
저장 삭제등을 하는 매니저입니다. </br>
먼저 manage.read()를 출력하는건, 그냥 parse한 값을 read해 출력해준다는 뜻입니다. </br>
아직 nom 파일을 만들지 않았으니 그냥 {}가 나올겁니다. </br>

### manage.write
--------------------------------

다음은 manage.write 입니다. write는 총 세가지의 인자를 가집니다 </br>

|key|value|type|
|-----|-----|-----|
| 키 | 값 | 타입|

키는 nom 파일에 저장될 이름입니다. json file로 따지면</br>

```json
{
  "name" : "hi"
}
```

에서 name 부분에 해당됩니다. </br>
다음은 value 입니다. </br>
json file의 "hi" 부분에 해당되는 곳입니다. </br>
마지막으로 type 입니다.</br>
integer,string,float... 등등 value의 타입을 지정하는 곳입니다.</br>

### manage.save
--------------------------------
저장해주는 앱니다. 얘 없으면 write 같은거 다 무시됨</br>

### manage.write
--------------------------------
