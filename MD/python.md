# 실행

먼저 test.py, test.nom을 만들어 줍니다. </br>
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

