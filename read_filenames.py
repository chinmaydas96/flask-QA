from os import listdir
from os.path import isfile, join

male_systems = ['Testes']
female_systems = ['Ovaries']


def get_disease_files(gender):
    mypath = './disease_info/'
    onlyfiles = [f.split('.html')[0][:-2]
                 for f in listdir(mypath) if isfile(join(mypath, f))]

    refined_files = []
    onlyfiles = sorted(list(dict.fromkeys(onlyfiles)))
    for filename in onlyfiles:
        filename = filename.split(':')
        if gender == 'male' and filename[0] in female_systems:
            continue
        elif gender == 'female' and filename[0] in male_systems:
            continue
        refined_files.append((filename[0], filename[1]))

    return refined_files


def get_disease_details(gender):

    related_files = get_disease_files(gender)

    detail_map = []
    for filename in related_files:
        detail_map.append({
            'title': filename[0],
            'disease': filename[1],
        })

    return detail_map