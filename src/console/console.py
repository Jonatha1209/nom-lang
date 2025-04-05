import nom
file_Massanger = nom.NomFileManager("data.nom")
s=input("Hello!, What your name? ")
file_Massanger.read()
file_Massanger.write(f"name_{s}",value=f"nom{s}",type_="string")
file_Massanger.save()
