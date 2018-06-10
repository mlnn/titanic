import pandas
data = pandas.read_csv('titanic.csv', index_col='PassengerId')

x_test = data[['ColumnName_1', 'ColumnName_2']].as_matrix()

Result_DataFrame = pd.DataFrame()
result_Matrix = model.predict(x_test)
Result_DataFrame ['_PRICE_'] = Matrix
Result_DataFrame.to_csv('result.csv', index=False)