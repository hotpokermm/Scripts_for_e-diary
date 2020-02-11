import random
from datacenter.models import Mark, Chastisement, Lesson, Subject, Schoolkid, Teacher, Commendation

def fix_marks(schoolkid):
    child = Schoolkid.objects.get(full_name__contains = schoolkid)
    bad_marks = Mark.objects.filter(schoolkid = child, points__lte = 3)
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    return print("Оценок ниже четвёрки: ", Mark.objects.filter(schoolkid = schoolkid, points__lte = 3).count())


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.filter(schoolkid = schoolkid)
    
    for chastisement in chastisements:
        chastisement.delete()
    return print(f"Замечания ученика {0} удалены", schoolkid)


def create_commendation(schoolkid, subject):
    commendation = ['Молодец!', 'Гораздо лучше, чем я ожидал!', 'Ты меня приятно удивил!', 'Замечательно!', 'Я вижу, как ты стараешься!', 'Великолепно!', 'Я тобой горжусь!']
    child = Schoolkid.objects.get(full_name__contains = schoolkid)
    lessons = Lesson.objects.filter(year_of_study = child.year_of_study, group_letter = child.group_letter, subject__title = subject)
    number_of_lessons = lessons.count() - 1
    last_lesson = lessons[number_of_lessons]
    Commendation.objects.create(text = random.choice(commendation), created = last_lesson.date, schoolkid = child, subject = last_lesson.subject, teacher = last_lesson.teacher)
    