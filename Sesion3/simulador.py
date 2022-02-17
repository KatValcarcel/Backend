from faker import Faker
from faker.providers import person, internet

objFaker = Faker()
objFaker.add_provider(person)
objFaker.add_provider(internet)

# print(fake.first_name_nonbinary())
# print(fake.free_email())

cursos = ['COMUNICACION', 'CTA', 'INGLES', 'FRENCH']

for curso in cursos:
    print(f"INSERT INTO CURSOS (nombre) VALUES ('{curso}');")

for x in range(100):
    print(
        f"INSERT INTO ALUMNOS (nombre, apellido, correo) VALUES ('{objFaker.first_name()}','{objFaker.last_name()}','{objFaker.free_email()}');")


alumno = objFaker.random_int(min=1, max=100)
curso = objFaker.random_int(min=1, max=4)
alumno_curso = [[1, 3], [10, 2], [32, 1], [55, 4], [86, 3], [10, 1]]

x = 0
while x < 200:
    curso = objFaker.random_int(min=1, max=4)
    alumno = objFaker.random_int(min=1, max=100)
    if [alumno, curso] not in alumno_curso:
        x += 1
        print(
            f'INSERT INTO ALUMNOS_CURSOS (ALUMNO_ID, CURSO_ID) VALUES({alumno}, {curso});')
        alumno_curso.append([alumno, curso])
