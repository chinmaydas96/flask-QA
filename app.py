from flask import Flask, render_template, request
import json

from question_papers import get_question_papers
from helpers import (
    refine_data,
    options,
    disease_map,
    organ_map,
    details,
    get_files,
    get_most_infected_organs,
    get_ranked_systems,
    get_secondary_system,
    get_circulatory_system,
    get_primary_endocrine,
    get_digestive_system
)
app = Flask(__name__, template_folder="templates")


@app.route('/')
def home_page():
    return render_template('home.html')


@app.route('/questions/male')
def questions_male():
    return render_template('questions.html', question_papers=get_question_papers('male'), options=options)


@app.route('/questions/female')
def questions_female():
    return render_template('questions.html', question_papers=get_question_papers('female'), options=options)


@app.route('/visualize', methods=['POST', 'GET'])
def visualize():
    if request.method == 'POST':
        data_form = request.form.get('data')
        if data_form:
            data = json.loads(data_form)
            data = refine_data(data)
            infected_areas = []
            infected_issues = []
            for value in data:
                infected_areas.append((value[0], disease_map[value[0]], value[1]))
                infected_issues.append((value[0], organ_map[value[0]], value[1]))

            infected_organs = []
            infected_organs.append(get_most_infected_organs(infected_areas[:]))
            infected_organs.append(get_secondary_system())
            infected_organs.append(get_circulatory_system())
            infected_organs.append(get_primary_endocrine())
            infected_organs.append(get_digestive_system())
            infected_systems = get_ranked_systems(infected_areas[:])

            infected_issues = get_files(infected_issues[:])
            return render_template('organs.html', infected_areas=infected_areas, infected_issues=infected_issues, infected_systems=infected_systems, infected_organs=infected_organs, details=details)
        else:
            return render_template('home.html')
    else:
        infected_areas = [
            ('Dopamine:Dopamine', '',
             20), ('Adrenals:Adrenal_Hypo-function', 'ADRENALS', 20),
            ('Adrenals:Adrenal_Hyper-function', 'ADRENALS',
             20), ('Parasympathetic_Nervous_System:Parasympathetic_Nervous_System', '', 18),
            ('Thyroid:Hypothyroidism', 'THYROID', 17), ('Liver:Liver',
                                                        'LIVER', 16), ('Parathyroid:Parathyroid', 'PARATHYROID', 14),
            ('Lungs:Lungs', 'LUNGS', 14), ('Stomach:Hyperacidity_Dyspepsia',
                                           'STOMACH', 13), ('Gaba_Glutamate:Gaba_Glutamate', '', 13),
            ('Kidneys:Kidneys', 'KIDNEYS',
             12), ('Sympathetic_Nervous_System:Sympathetic_Nervous_System', '', 11),
            ('Small_Intestine:Ilium', 'SMALL_INTESTINE', 11), ('Glycemia:Glycemia-Hyper',
                                                               '', 11), ('Thyroid:Hyperthyroidism', 'THYROID', 10),
            ('Small_Intestine:Jejunum', 'SMALL_INTESTINE', 9), ('Testes:Testes',
                                                                'TESTES', 7), ('Pituitary:Pituitary', 'PITUITARY', 7),
            ('Stomach:Hypoacidity', 'STOMACH', 6), ('Small_Intestine:Duodenum',
                                                    'SMALL_INTESTINE', 5), ('Serotonin:Serotonin', '', 3),
            ('Heart:Heart', 'HEART', 3), ('Hypothalamus:Hypothalamus',
                                          'HYPOTHALAMUS', 2), ('Glycemia:Glycemia-Hypo', '', 0)
        ]

        infected_issues = [
            ('Dopamine:Dopamine', 'Dopamine',
             20), ('Adrenals:Adrenal_Hypo-function', 'ADRENALS', 20),
            ('Adrenals:Adrenal_Hyper-function', 'ADRENALS',
             20), ('Parasympathetic_Nervous_System:Parasympathetic_Nervous_System', 'Parasympathetic_Nervous_System', 18),
            ('Thyroid:Hypothyroidism', 'THYROID', 17), ('Liver:Liver',
                                                        'LIVER', 16), ('Parathyroid:Parathyroid', 'PARATHYROID', 14),
            ('Lungs:Lungs', 'LUNGS', 14), ('Stomach:Hyperacidity_Dyspepsia',
                                           'STOMACH', 13), ('Gaba_Glutamate:Gaba_Glutamate', 'Gaba_Glutamate', 13),
            ('Kidneys:Kidneys', 'KIDNEYS', 12), ('Sympathetic_Nervous_System:Sympathetic_Nervous_System',
                                                 'Sympathetic_Nervous_System', 11),
            ('Small_Intestine:Ilium', 'SMALL_INTESTINE', 11), ('Glycemia:Glycemia-Hyper',
                                                               'E', 11), ('Thyroid:Hyperthyroidism', 'THYROID', 10),
            ('Small_Intestine:Jejunum', 'SMALL_INTESTINE', 9), ('Testes:Testes',
                                                                'TESTES', 7), ('Pituitary:Pituitary', 'PITUITARY', 7),
            ('Stomach:Hypoacidity', 'STOMACH', 6), ('Small_Intestine:Duodenum',
                                                    'SMALL_INTESTINE', 5), ('Serotonin:Serotonin', 'Serotonin', 3),
            ('Heart:Heart', 'HEART', 3), ('Hypothalamus:Hypothalamus',
                                          'HYPOTHALAMUS', 2), ('Glycemia:Glycemia-Hypo', 'F', 0)
        ]

        infected_organs = []
        infected_organs.append(get_most_infected_organs(infected_areas[:]))
        infected_organs.append(get_secondary_system())
        infected_organs.append(get_circulatory_system())
        infected_organs.append(get_primary_endocrine())
        infected_organs.append(get_digestive_system())
        infected_systems = get_ranked_systems(infected_areas[:])


        infected_issues = get_files(infected_issues[:])
        return render_template('organs.html', infected_areas=infected_areas, infected_issues=infected_issues, infected_systems=infected_systems, infected_organs=infected_organs, details=details)
        
    return render_template('home.html')

if __name__ == '__main__':
    app.run()
