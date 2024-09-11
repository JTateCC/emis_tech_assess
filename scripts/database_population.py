def insert_dataframe_to_db(session, df, model_class):
    records = df.to_dict(orient='records')
    try:
        session.bulk_insert_mappings(model_class, records)
        session.commit()

    # not ideal and handle duplicates in future work
    except Exception:
        session.rollback()

