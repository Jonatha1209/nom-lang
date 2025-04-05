import nom as nom
manage = nom.NomFileManager("test.nom")
print(manage.read())
manage.write("nickname", "Ali", "string")
manage.update("age", 29)
manage.save()
