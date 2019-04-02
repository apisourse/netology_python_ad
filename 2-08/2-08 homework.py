from pprint import pprint
import psycopg2
import json

# Представим, что это тянется из фала Config
database = 'postgres'
user = 'artempakhomov'
password = 'milk0990'
host = 'localhost'


def create_db():
    with psycopg2.connect(database=database, user=user, password=password, host=host) as conn:
        with conn.cursor() as curs:
            curs.execute('''
                            DROP TABLE IF EXISTS "public"."Course";
                            CREATE TABLE "public"."Course" (
                              "id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY (
                                INCREMENT 1
                                MINVALUE  1
                                MAXVALUE 2147483647
                                START 1
                                ),
                              "name" character varying(100) COLLATE "pg_catalog"."default" NOT NULL
                            );
                            ALTER TABLE "public"."Course" ADD CONSTRAINT "Course_pkey" PRIMARY KEY ("id");
                            
                            DROP TABLE IF EXISTS "public"."Student";
                            CREATE TABLE "public"."Student" (
                              "id" int4 NOT NULL GENERATED BY DEFAULT AS IDENTITY (
                                INCREMENT 1
                                MINVALUE  1
                                MAXVALUE 2147483647
                                START 1
                                ),
                              "name" character varying(100) COLLATE "pg_catalog"."default" NOT NULL,
                              "gpa" numeric(10,2),
                              "birth" timestamptz(0)
                            );
                            ALTER TABLE "public"."Student" ADD CONSTRAINT "Student_pkey" PRIMARY KEY ("id");
                            ''')


def add_student(student):  # просто создает студента
    id = student['id']
    name = student['name']
    gpa = student['gpa']
    birth = student['birth']
    with psycopg2.connect(database=database, user=user, password=password, host=host) as conn:
        with conn.cursor() as curs:
            curs.execute('INSERT INTO \"Student\" VALUES (%s, %s, %s, %s);', (int(id), name, float(gpa), birth,))


def get_student(student_id):  # получает студента по id
    with psycopg2.connect(database=database, user=user, password=password, host=host) as conn:
        with conn.cursor() as curs:
            curs.execute(
                'SELECT \"Student\".\"name\", \"Student\".birth FROM \"Student\" WHERE \"public\".\"Student\".\"id\" = %s',
                (int(student_id),))
            print(curs.fetchall())


def add_students(courses, course_id, students):  # создает студентов и записывает их на курс
    for x in courses:
        c_id = x['id']
        c_name = x['name']
        conn = psycopg2.connect(database=database, user=user, password=password, host=host)
        curs = conn.cursor()
        curs.execute('INSERT INTO \"Course\" VALUES (%s, %s);', (int(c_id), c_name,))
        conn.commit()
    print('courses data add & commit')
    for i in students:
        id = i['id']
        name = i['name']
        birth = i['birth']

        conn = psycopg2.connect(database=database, user=user, password=password, host=host)
        curs = conn.cursor()
        curs.execute('INSERT INTO \"Student\" VALUES (%s, %s, %s, %s);', (int(id), name, float(course_id), birth,))
        conn.commit()
    print('students data add & commit')


def get_students(course_id):  # возвращает студентов определенного курса
    with psycopg2.connect(database=database, user=user, password=password, host=host) as conn:
        with conn.cursor() as curs:
            curs.execute(
                '''
                SELECT
                    \"Student\".\"id\",
                    \"Student\".\"name\",
                    \"Course\".\"name\" AS course 
                FROM
                    \"Student\"
                    LEFT JOIN \"Course\" ON \"Student\".gpa = "Course"."id"
                WHERE
	                \"Student\".gpa = %s
                ''', (course_id,)
            )
            print(curs.fetchall())


if __name__ == '__main__':
    def import_data():
        def import_studets(file):
            with open(file, encoding="utf-8") as s_datafile_load:
                s_json_data = json.load(s_datafile_load)
                return s_json_data

        def import_courses(file):
            with open(file, encoding="utf-8") as c_datafile_load:
                c_json_data = json.load(c_datafile_load)
                return c_json_data

        s = import_studets("Student.json")
        c = import_courses("Course.json")

        return s, c

    create_db()
    # add_student(student=import_data()[0]['Student'][7])
    add_students(courses=import_data()[1]['Course'], course_id=1, students=import_data()[0]['Student'])
    # get_student(student_id=3)
    get_students(course_id=1)
