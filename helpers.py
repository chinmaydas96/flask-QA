
options = [
    {'value': 2, 'text': 'Yes'},
    {'value': 1, 'text': 'Sometimes'},
    {'value': 0, 'text': 'No'}
]


def get_primary_endocrine():
    endocrine_system = ['ADRENALS', 'PITUITARY',
                        'THYROID', 'TESTES', 'HYPOTHALAMUS']
    endocrine_list = []
    for esystem in endocrine_system:
        endocrine_list.append((esystem, ''))
    return endocrine_list


def get_digestive_system():
    endocrine_system = ['SMALL_INTESTINE', 'STOMACH']
    endocrine_list = []
    for esystem in endocrine_system:
        endocrine_list.append((esystem, ''))
    return endocrine_list


def get_secondary_system():
    endocrine_system = ['LIVER', 'KIDNEYS', 'PARATHYROID']
    endocrine_list = []
    for esystem in endocrine_system:
        endocrine_list.append((esystem, ''))
    return endocrine_list


def get_circulatory_system():
    endocrine_system = ['LUNGS', 'HEART']
    endocrine_list = []
    for esystem in endocrine_system:
        endocrine_list.append((esystem, ''))
    return endocrine_list


disease_map = {
    'Adrenals:Adrenal_Hyper-function': 'ADRENALS',
    'Adrenals:Adrenal_Hypo-function': 'ADRENALS',
    'Ovaries:Ovaries': 'OVARIES',
    'Pituitary:Pituitary': 'PITUITARY',
    'Small_Intestine:Duodenum': 'SMALL_INTESTINE',
    'Small_Intestine:Ilium': 'SMALL_INTESTINE',
    'Testes:Testes': 'TESTES',
    'Sympathetic_Nervous_System:Sympathetic_Nervous_System': '',
    'Glycemia:Glycemia-Hypo': '',
    'Small_Intestine:Jejunum': 'SMALL_INTESTINE',
    'Gaba_Glutamate:Gaba_Glutamate': '',
    'Heart:Heart': 'HEART',
    'Kidneys:Kidneys': 'KIDNEYS',
    'Serotonin:Serotonin': '',
    'Lungs:Lungs': 'LUNGS',
    'Hypothalamus:Hypothalamus': 'HYPOTHALAMUS',
    'Parasympathetic_Nervous_System:Parasympathetic_Nervous_System': '',
    'Thyroid:Hyperthyroidism': 'THYROID',
    'Glycemia:Glycemia-Hyper': '',
    'Liver:Liver': 'LIVER',
    'Stomach:Hyperacidity_Dyspepsia': 'STOMACH',
    'Thyroid:Hypothyroidism': 'THYROID',
    'Dopamine:Dopamine': '',
    'Stomach:Hypoacidity': 'STOMACH',
    'Parathyroid:Parathyroid': 'PARATHYROID'
}

organ_map = {
    'Adrenals:Adrenal_Hyper-function': 'ADRENALS',
    'Adrenals:Adrenal_Hypo-function': 'ADRENALS',
    'Ovaries:Ovaries': 'OVARIES',
    'Pituitary:Pituitary': 'PITUITARY',
    'Small_Intestine:Duodenum': 'SMALL_INTESTINE',
    'Small_Intestine:Ilium': 'SMALL_INTESTINE',
    'Testes:Testes': 'TESTES',
    'Sympathetic_Nervous_System:Sympathetic_Nervous_System': 'Sympathetic_nervous_system',
    'Glycemia:Glycemia-Hypo': 'Glycemia',
    'Small_Intestine:Jejunum': 'SMALL_INTESTINE',
    'Gaba_Glutamate:Gaba_Glutamate': 'Gaba_glutamate',
    'Heart:Heart': 'HEART',
    'Kidneys:Kidneys': 'KIDNEYS',
    'Serotonin:Serotonin': 'Serotonin',
    'Lungs:Lungs': 'LUNGS',
    'Hypothalamus:Hypothalamus': 'HYPOTHALAMUS',
    'Parasympathetic_Nervous_System:Parasympathetic_Nervous_System': 'Parasympathetic_nervous_system',
    'Thyroid:Hyperthyroidism': 'THYROID',
    'Glycemia:Glycemia-Hyper': 'Glycemia',
    'Liver:Liver': 'LIVER',
    'Stomach:Hyperacidity_Dyspepsia': 'STOMACH',
    'Thyroid:Hypothyroidism': 'THYROID',
    'Dopamine:Dopamine': 'Dopamine',
    'Stomach:Hypoacidity': 'STOMACH',
    'Parathyroid:Parathyroid': 'PARATHYROID'
}

system_map = {
    'ADRENALS': 'Primary Endocrine System',
    'OVARIES': 'Primary Endocrine System',
    'PITUITARY': 'Primary Endocrine System',
    'SMALL_INTESTINE': 'Digestive System',
    'TESTES': 'Primary Endocrine System',
    'Sympathetic_Nervous_System:Sympathetic_Nervous_System': 'Neuroendocrine System',
    'Glycemia:Glycemia-Hypo': 'Digestive System',
    'Gaba_Glutamate:Gaba_Glutamate': 'Neuroendocrine System',
    'HEART': 'Circulatory System',
    'KIDNEYS': 'Secondary Endocrine System',
    'Serotonin:Serotonin': 'Neuroendocrine System',
    'LUNGS': 'Circulatory System',
    'HYPOTHALAMUS': 'Primary Endocrine System',
    'Parasympathetic_Nervous_System:Parasympathetic_Nervous_System': 'Neuroendocrine System',
    'THYROID': 'Primary Endocrine System',
    'Glycemia:Glycemia-Hyper': 'Digestive System',
    'LIVER': 'Secondary Endocrine System',
    'STOMACH': 'Digestive System',
    'Dopamine:Dopamine': 'Neuroendocrine System',
    'PARATHYROID': 'Secondary Endocrine System',
}

details = ['info', 'supplements', 'nutriants', 'diagnosis', 'genetics']
short_details = ['i', 's', 'n', 'd', 'g']


def refine_data(data):
    refined_data = []
    for data_key in data.keys():
        sum = 0
        for value in data[data_key]:
            sum = sum + int(value)
        refined_data.append((data_key.strip(), sum))
    refined_data.sort(key=lambda x: x[1])
    refined_data.reverse()
    return refined_data


def get_most_infected_organs(data):
    infected_organ_data = []
    while data:
        i = data[0]
        value = i[1]
        if value:
            same = [item for item in data if item[1] == value]
            sum_value = 0
            sum_count = 0
            for index in same:
                sum_value += index[2]
                data.remove(index)
                sum_count += 1
            infected_organ_data.append((value, sum_value/sum_count))
        else:
            data.remove(i)
    infected_organ_data.sort(key=lambda x: x[1])
    infected_organ_data.reverse()
    return infected_organ_data


def get_ranked_systems(data):
    infected_organ_data = []
    while data:
        i = data[0]
        value = i[1]
        if not value:
            value = i[0]
        same = [item for item in data if item[1] == value or item[0] == value]
        sum_value = 0
        sum_count = 0
        for index in same:
            sum_value += index[2]
            data.remove(index)
            sum_count += 1
        infected_organ_data.append((value, sum_value/sum_count))

    infected_organ_data.sort(key=lambda x: x[1], reverse=True)
    return refine_system_data(infected_organ_data)


systems_code = {
    'Primary Endocrine System': 3,
    'Digestive System': 4,
    'Neuroendocrine System': None,
    'Secondary Endocrine System': 1,
    'Circulatory System': 2
}


def refine_system_data(data):
    system = {}
    for i in data:
        key = i[0]
        value = system_map[key]
        if value in system.keys():
            system[value]['sum'] = system[value]['sum'] + i[1]
            system[value]['count'] = system[value]['count'] + 1
            if ':' in i[0]:
                organ = i[0].split(':')[0]
            else:
                organ = i[0]

            if organ not in system[value]['list']:
                system[value]['list'].append(organ)
        else:
            system[value] = {}
            system[value]['sum'] = i[1]
            system[value]['count'] = 1
            if ':' in i[0]:
                organ = i[0].split(':')[0]
            else:
                organ = i[0]
            system[value]['list'] = [organ]

    system_score = []
    for i, v in system.items():
        s_code = systems_code.get(i)
        system_score.append((i, v['sum']/v['count'], v['list'], s_code))

    system_score.sort(key=lambda x: x[1], reverse=True)
    return system_score


def get_files(infected_areas):
    transformed_data = []
    traversed_data = []
    for area in infected_areas:
        data = []
        for detail in short_details:
            f = open("disease_info/{0}_{1}.html".format(area[0], detail), "r")
            file_data = f.read()
            f.close()
            data.append(file_data)
        if area[0].split(':')[0] == 'Glycemia':
            if 'Glycemia' not in traversed_data:
                transformed_data.append(
                    (area[0].split(':')[1], 'Glycemia', data))
                traversed_data.append('Glycemia')
        else:
            if area[1] not in traversed_data:
                traversed_data.append(area[1])
                transformed_data.append((area[0].split(':')[1], area[1], data))
    return transformed_data
