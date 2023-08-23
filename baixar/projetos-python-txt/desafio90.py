aluno = dict()
aluno['nome']=str(input('Nome: '))
aluno['media']=float(input('Media: '))
if aluno['media']>=7:
    aluno['situação']='Aprovada'
else:
     aluno['situação']='Reprovada'
for k, v in aluno.items():
     print(f'{k} é igual {v}')