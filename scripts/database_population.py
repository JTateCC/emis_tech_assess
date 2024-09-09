def insert_dataframe_to_db(session, df, model_class):


    records = df.to_dict(orient='records')
    session.bulk_insert_mappings(model_class, records)
    session.commit()

