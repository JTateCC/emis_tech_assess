def insert_dataframe_to_db(session, df, model_class):

    for _, row in df.iterrows():
        # Create an instance of the model class for each row
        model_instance = model_class(**row.to_dict())
        session.add(model_instance)
    session.commit()


