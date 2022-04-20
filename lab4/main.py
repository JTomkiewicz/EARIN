import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


def main() -> None:
    # store column names
    colNames = ['duration', 'protocol_type', 'service', 'flag', 'src_bytes',
                'dst_bytes', 'land', 'wrong_fragment', 'urgent', 'hot', 'num_failed_logins',
                'logged_in', 'num_compromised', 'root_shell', 'su_attempted', 'num_root',
                'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds',
                'is_host_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate',
                'srv_serror_rate', 'rerror_rate', 'srv_rerror_rate', 'same_srv_rate',
                'diff_srv_rate', 'srv_diff_host_rate', 'dst_host_count', 'dst_host_srv_count',
                'dst_host_same_srv_rate', 'dst_host_diff_srv_rate', 'dst_host_same_src_port_rate',
                'dst_host_srv_diff_host_rate', 'dst_host_serror_rate', 'dst_host_srv_serror_rate',
                'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'label']

    # read both txt files
    trainFile = pd.read_csv('KDDTrain+.txt', header=None, names=colNames)
    testFile = pd.read_csv('KDDTest+.txt', header=None, names=colNames)

    # dimensions
    print(f'training set dim: {trainFile.shape}')
    print(f'test set dim: {testFile.shape}')

    # distributions
    print('training set - label distribution:')
    print(trainFile['label'].value_counts())

    print('test set - label distribution:')
    print(testFile['label'].value_counts())

    # categories distribution for: protocol_type (col #2), service (col #3), flag (col #4)
    print('training set:')
    for colName in trainFile.columns:
        if trainFile[colName].dtypes == 'object':
            uniqueCategory = len(trainFile[colName].unique())
            print(f'feature {colName} has {uniqueCategory} categories')

    print('test set:')
    for colName in testFile.columns:
        if testFile[colName].dtypes == 'object':
            uniqueCategory = len(testFile[colName].unique())
            print(f'feature {colName} has {uniqueCategory} categories')

    # categorical features into 2D np array
    categoricalCol = ['protocol_type', 'service', 'flag']

    trainCategoricalValues = trainFile[categoricalCol]
    testCategoricalValues = testFile[categoricalCol]

    # protocol type
    uniqueProtocol = sorted(trainFile.protocol_type.unique())
    string1 = 'Protocol_type_'
    uniqueProtocol2 = [string1 + x for x in uniqueProtocol]

    # service
    uniqueService = sorted(trainFile.service.unique())
    string2 = 'service_'
    uniqueService2 = [string2 + x for x in uniqueService]

    # flag
    uniqueFlag = sorted(trainFile.flag.unique())
    string3 = 'flag_'
    uniqueFlag2 = [string3 + str(x) for x in uniqueFlag]

    # merge together
    dumcols = uniqueProtocol2 + uniqueService2 + uniqueFlag2

    # do it for test set
    uniqueServiceTest = sorted(testFile.service.unique())
    uniqueService2Test = [string2 + x for x in uniqueServiceTest]
    dumcolsTest = uniqueProtocol2 + uniqueService2Test + uniqueFlag2

    # categorical features into numbers
    categoricalValuesEncTrain = trainCategoricalValues.apply(
        LabelEncoder().fit_transform)

    categoricalValuesEncTest = testCategoricalValues.apply(
        LabelEncoder().fit_transform)

    # one-hot-encoding
    enc = OneHotEncoder()

    categoricalValuesEncencTrain = enc.fit_transform(categoricalValuesEncTrain)
    catDataTrain = pd.DataFrame(
        categoricalValuesEncencTrain.toarray(), columns=dumcols)

    categoricalValuesEncencTest = enc.fit_transform(
        categoricalValuesEncTest)
    catDataTest = pd.DataFrame(
        categoricalValuesEncencTest.toarray(), columns=dumcolsTest)

    # add 6 missing columns to test set
    trainService = trainFile['service'].tolist()
    testService = testFile['service'].tolist()
    difference = list(set(trainService) - set(testService))
    string = 'service_'
    difference = [string + x for x in difference]

    for col in difference:
        catDataTest[col] = 0

    # add encoded categorical columns to dataframe
    newTrainFile = trainFile.join(catDataTrain)
    newTrainFile.drop('flag', axis=1, inplace=True)
    newTrainFile.drop('protocol_type', axis=1, inplace=True)
    newTrainFile.drop('service', axis=1, inplace=True)

    newTestFile = testFile.join(catDataTest)
    newTestFile.drop('flag', axis=1, inplace=True)
    newTestFile.drop('protocol_type', axis=1, inplace=True)
    newTestFile.drop('service', axis=1, inplace=True)

    # split dataset for 4 smaller datasets (0 - normal, 1 - DoS, 2 - Probe, 3 - R2L, 4 - U2R)


if __name__ == '__main__':
    main()
