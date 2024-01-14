from config import *
 
if __name__ == "__main__":
    src_path = "dataset_svm"
    sigs = os.listdir(src_path)
    random.shuffle(sigs)
    
    train_set = sigs[:len(sigs)//3*2]
    test_set = sigs[len(sigs)//3*2:]

    # Make labels and features
    train_features = []
    train_label = []
    for signame in train_set:
        sig = np.loadtxt(os.path.join(src_path, signame), dtype=np.float32)
        train_features.append(sig)
        train_label.append(int(signame.split("raw")[0])//400-1)

    test_features = []
    test_label = []
    for signame in test_set:
        sig = np.loadtxt(os.path.join(src_path, signame), dtype=np.float32)
        test_features.append(sig)
        test_label.append(int(signame.split("raw")[0])//400-1)
    
    train_label = np.array(train_label)
    train_features = np.array(train_features)
    test_features = np.array(test_features)
    test_label = np.array(test_label)


    clf = svm.SVC(C=6, gamma=0.05,max_iter=-1)
    clf.fit(train_features, train_label)
    
    
    #Test on Training data
    train_result = clf.predict(train_features)
    precision = sum(train_result == train_label)/train_label.shape[0]
    print('Training precision: ', precision)
    
    
    #Test on test data
    test_result = clf.predict(test_features)
    precision = sum(test_result == test_label)/test_label.shape[0]
    print('Test precision: ', precision)
