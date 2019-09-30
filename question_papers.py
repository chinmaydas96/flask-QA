from read_filenames import get_disease_details

def get_question_papers(gender):

    disease_details = get_disease_details(gender)
    for paper in disease_details:
        questions = []
        with open("disease_info/{0}:{1}_q.html".format(paper['title'], paper['disease']), "r") as f:
            for line in f:
                if line:
                    line = line.split('.')[-1]
                    questions.append(line)
        paper['questions'] = questions

    return disease_details
