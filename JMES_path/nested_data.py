import jmespath

data = {
    'reservations': [
        {
            'instances': [
                {
                    'type': 'small',
                    'state': {'name': 'running'},
                    'tags': [
                        {'Key': 'Name', 'Values': ['Web']},
                        {'Key': 'version', 'Values': ['1']},
                    ],
                },
                {
                    'type': 'large',
                    'state': {'name': 'stopped'},
                    'tags': [
                        {'Key': 'Name', 'Values': ['Web']},
                        {'Key': 'version', 'Values': ['1']},
                    ],
                },
            ],
        },
        {
            'instances': [
                {
                    'type': 'medium',
                    'state': {'name': 'terminated'},
                    'tags': [
                        {'Key': 'Name', 'Values': ['Web']},
                        {'Key': 'version', 'Values': ['1']},
                    ],
                },
                {
                    'type': 'xlarge',
                    'state': {'name': 'running'},
                    'tags': [
                        {'Key': 'Name', 'Values': ['DB']},
                        {'Key': 'version', 'Values': ['1']},
                    ],
                },
            ],
        },
    ],
}

# print(jmespath.search("reservations[?instances[?state.name==`running`].tags[?Key==`Name`].Values[?contains(`Web`)]][0].instances[?type==`small`].tags[?Key==`Name`].Values[0]", data)) # ["Web"]
# print(jmespath.search("reservations[].instances[].[tags[?Key=='Name'].Values[] | [0], type, state.name]", data))
print(
    jmespath.search(
        "reservations[].instances[].{first_tag: tags[?Key=='Name'].Values[] | [0], type: type, state_name: state.name}",
        data,
    ),
)
