def keywords(**kwargs):
    "Prints the keys and arguments passed through"
    for key in kwargs:
        print("{0}: {1} ".format(key, kwargs[key]))

def keywords_as_dict(**kwargs):
    "Returns the keyword arguments as a dict"
    return kwargs

if __name__ == "__main__":
    keywords(guido="Founder of Python", python="Used by NASA and Google")
    print(keywords_as_dict(guido="Founder of Python", python="Used by NASA "
                                                "and Google"))


def description(name, instructor, *students, **staff):
    """Print out a course description.
    name:           Name of the course
    instructor:     Name of the instructor
    *students, ...: List of student names (positional arguments)
    **staff, ...:   List of additional staff (keyword arguments)
    """
    print("=" * 40)
    print("Course Name:", name)
    print("Instructor:", instructor)
    print("-" * 40)
    for title, name in staff.items():
        print(title.capitalize(), ": ", name)# capitalize() is used to make starting letter of word capital
    print("{0:-^40}".format(" registered students "))
    for student in students:
        l_name, r_name = student.split(" ")
        print(l_name.capitalize(),r_name.capitalize())
        # print(student)


if __name__ == "__main__":
    description("Python 101",
                "Steve Holden",
                "Georgie Peorgie",
                "Mary Lamb",
                "Penny Rice",
                publisher="O'Reilly School of Technology",
                author="Python Software Foundation"
                )
    description("Django 101",
                "Jacob Kaplan-Moss",
                "baa-baa blacksheep",
                "mary contrary",
                "missy Muffet",
                "Peter piper",
                publisher="O'Reilly School of Technology",
                author="Django Software Foundation",
                editor="Daniel Greenfeld"
                )