import copy
class University:
    def __init__(self, name: str, location: str, students: str):
        self.name = name
        self.location = location
        self.students = students

class OpenUniversity(University):
    def __init__(self, name: str, location: str, students: str, courses: dict):
        super().__init__(name, location, students)
        self.courses = copy.deepcopy(courses)

    def get_course_name_max_students(self):
        max = 0
        biggest_course = ''
        for course in self.courses:
            if int(self.courses[course]) > max:
                max = int(self.courses[course])
                biggest_course = course
        return biggest_course

def map_universities(text_file):
    with open(text_file, 'r') as f:
        sum = 0
        li_universities = []
        line = f.readline()
        while line:
            li_line = line.split(',')
            uni_name = li_line[0].strip()
            uni_location = li_line[1].strip()
            uni_type = li_line[2].strip().split()
            uni_students = uni_type[0]
            if len(uni_type) >= 2 and uni_type[1] == 'courses:':
                courses_di = {}
                while True:
                    line = f.readline()
                    course = line.split(',')
                    if len(course) == 1 and course[0] == 'done courses\n':
                        uni_obj = OpenUniversity(uni_name, uni_location, uni_students, courses_di)
                        break
                    uni_course_name = course[0].strip()
                    uni_course_students = course[1].strip()
                    courses_di[course[0].strip()] = course[1].strip()
            else:
                uni_obj = University(uni_name, uni_location, uni_students)
            sum += int(uni_students)
            li_universities.append(uni_obj)
            line = f.readline()
        uni_count = len(li_universities)
        for uni in li_universities:
            if uni.__class__.__name__ == 'OpenUniversity':
                print(f'for {uni.name} University the course with max students is:'
                      f' {uni.get_course_name_max_students()}')
        print(f'sum of students: {sum}')











file_name = 'universities_data'
map_universities(file_name)
