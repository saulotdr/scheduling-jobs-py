from fastjsonschema import compile as compile_schema

""" @throws JsonSchemaException """
schema = compile_schema({
    "$schema": "http://json-schema.org/draft-07/schema#",
    "title": "Scheduling Jobs Array",
    "description": "Lista com pŕoximos jobs a serem executados",
    'type': 'array',
    'required': ['ID', 'Descrição', 'Data Máxima de conclusão', 'Tempo estimado'],
    'properties': {
        'ID': {
            'description': 'Identificador do job',
            'type': 'number',
            'minimum': 0
        },
        'Descrição': {
            'description': 'Descrição do job',
            'type': 'string'
        },
        'Data Máxima de conclusão': {
            'description': 'Data máxima para execução do job',
            'type': 'string',
            'format': 'date'
        },
        'Tempo estimado': {
            'description': 'Duração estimada do job',
            'type': 'string'
        }
    }
})

# """ @throws JsonSchemaException """
# window = compile_schema({
#     "$schema": "http://json-schema.org/draft-07/schema#",
#     "title": "Scheduling Jobs Array",
#     "description": "Lista com pŕoximos jobs a serem executados",
#     'type': 'array',
#     'required': ['ID', 'Descrição', 'Data Máxima de conclusão', 'Tempo estimado'],
#     'properties': {
#         'ID': {
#             'description': 'Identificador do job',
#             'type': 'number',
#             'minimum': 0
#         },
#         'Descrição': {
#             'description': 'Descrição do job',
#             'type': 'string'
#         },
#         'Data Máxima de conclusão': {
#             'description': 'Data máxima para execução do job',
#             'type': 'string'
#         },
#         'Tempo estimado': {
#             'description': 'Duração estimada do job',
#             'type': 'string'
#         }
#     }
# })
