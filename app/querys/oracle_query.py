def query_dataset_example(id_cia:str):
    
    oracle_query = f'''
    SELECT
        EX.*
    FROM
        DW_DATASET_EXAMPLE EX
    WHERE
        EX.ID_CIA = {id_cia}
    '''
    return oracle_query