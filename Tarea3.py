from faker import Faker

fake = Faker()
# hacer un for 200 veces que genere un número random del 1 al 100 y luego un random del 1 al 4
# sin repetidos
# no se debe repetir:
data = [[1, 3], [10, 2], [32, 1], [55, 4], [86, 3], [10, 1]]
x = 0
while(x < 100):
    curso = fake.random_int(min=0, max=4)
    alumno = fake.random_int(min=1, max=99)
    if [alumno, curso] not in data:
        x += 1
        print(
            f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES({alumno}, {curso});')
        data.append([alumno, curso])
