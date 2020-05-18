from fastjsonschema import compile as compile_schema, validate as validate_schema

""" @throws JsonSchemaException """
schema = compile_schema({
    'type': 'array',
    "items": {
        "type": "object",
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
                'type': 'string'
            },
            'Tempo estimado': {
                'description': 'Duração estimada do job',
                'type': 'string',
                'pattern': '\\d.+hora|horas'
            }
        }
    }
})

def validate(payload):
    schema(payload)