for chunk in pd.read_csv('Measurement_info.csv',sep=',',
                         dtype={'Station code':'int8','Item code':'int8','Instrument status':'int8',
                                'Average value':'float16','Measurement date':'string'},chunksize=10000):
    
    # zip the data
    data = list(zip(chunk['Measurement date'],chunk['Average value'],chunk['Instrument status'],
                       chunk['Item code'],chunk['Station code']))
    
    # insert data into db
    try:
        cur.executemany(measurement_insert_query,data)
        conn.commit()
        print('success')
    
    except (sql.Error,sql.Warning) as e:
        conn.close()
        print(e)
